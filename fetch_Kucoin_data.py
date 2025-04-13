# %%
import ccxt
import time
import pandas as pd
api_key = '***************'
api_secret = '************'
api_passphase = '*******'
exchange = ccxt.kucoin({
    'api_key':api_key,
    'secret': api_secret,
    'passphase': api_passphase
})
# Function to get order book data
def fetch_order_book(symbol='XRP/USDT'):
    order_book = exchange.fetch_order_book(symbol)
    return order_book

# Fetch order book for XRP/USDT
order_book = fetch_order_book('XRP/USDT')
# Collecting order book data every second and storing it
def collect_data(symbol='XRP/USDT', duration=60):
    data = []
    start_time = time.time()
    
    while time.time() - start_time < duration:
        order_book = fetch_order_book(symbol)
        timestamp = time.time()
        # Add timestamp to each order book entry
        data.append({
            'timestamp': timestamp,
            'bids': order_book['bids'],
            'asks': order_book['asks']
        })
        # Sleep for a second to avoid hitting rate limits
        time.sleep(1)
    
    # Convert collected data into a DataFrame
    df = pd.DataFrame(data)
    return df

# Collect data for 60 seconds
order_book_data = collect_data('XRP/USDT', 60)

# Display the collected data
print(order_book_data)




 # %%
