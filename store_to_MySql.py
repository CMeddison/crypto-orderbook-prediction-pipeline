import mysql.connector
import time
from fetch_Kucoin_data import fetch_order_book

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="********",
    database="Kucoin_orderbook"
)
cursor = conn.cursor()

def get_last_price():
    """Fetch the last recorded price from the database."""
    cursor.execute("SELECT price FROM order_book ORDER BY timestamp DESC LIMIT 1")
    last_price = cursor.fetchone()
    if last_price and last_price[0] is not None:
        return float(last_price[0])
    return 0  # Default to 0 if no previous price exists

while True:
    order_book = fetch_order_book()  # Fetch order book data
    last_price = get_last_price()  # Get previous price from database

    if not order_book or 'bids' not in order_book or 'asks' not in order_book:
        print("⚠️ No order book data received. Skipping iteration.")
        time.sleep(1)
        continue

    # Extract bid and ask details
    best_bid_price = float(order_book['bids'][0][0]) if order_book['bids'] else 0
    best_ask_price = float(order_book['asks'][0][0]) if order_book['asks'] else 0
    bid_ask_spread = best_ask_price - best_bid_price if best_bid_price and best_ask_price else 0

    # Compute total bid and ask volumes
    total_bid_volume = sum(float(bid[1]) for bid in order_book['bids'])
    total_ask_volume = sum(float(ask[1]) for ask in order_book['asks'])

    # Compute volume imbalance
    volume_imbalance = (total_bid_volume - total_ask_volume) / (total_bid_volume + total_ask_volume) if (total_bid_volume + total_ask_volume) > 0 else 0

    # Compute mid-price
    mid_price = (best_bid_price + best_ask_price) / 2 if best_bid_price and best_ask_price else 0

    # Insert Bids (Buy Orders)
    for bid in order_book['bids']:
        price, amount = float(bid[0]), float(bid[1])
        total = price * amount
        price_movement = price - last_price
        price_movement_pct = (price_movement / last_price) * 100 if last_price != 0 else 0  # Avoid division by zero

        cursor.execute("""
            INSERT INTO order_book 
            (order_type, price, amount, total, best_bid_price, best_ask_price, bid_ask_spread, 
            total_bid_volume, total_ask_volume, volume_imbalance, mid_price, last_price, price_movement, price_movement_pct)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, ('buy', price, amount, total, best_bid_price, best_ask_price, bid_ask_spread, 
              total_bid_volume, total_ask_volume, volume_imbalance, mid_price, last_price, price_movement, price_movement_pct))

    # Insert Asks (Sell Orders)
    for ask in order_book['asks']:
        price, amount = float(ask[0]), float(ask[1])
        total = price * amount
        price_movement = price - last_price
        price_movement_pct = (price_movement / last_price) * 100 if last_price != 0 else 0

        cursor.execute("""
            INSERT INTO order_book 
            M(order_type, price, amount, total, best_bid_price, best_ask_price, bid_ask_spread, 
            total_bid_volume, total_ask_volume, volume_imbalance, mid_price, last_price, price_movement, price_movement_pct)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, ('sell', price, amount, total, best_bid_price, best_ask_price, bid_ask_spread, 
              total_bid_volume, total_ask_volume, volume_imbalance, mid_price, last_price, price_movement, price_movement_pct))

    conn.commit()
    print("✅ Order book updated.")

    time.sleep(1)  # Adjust sleep time as needed



