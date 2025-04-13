import mysql.connector
import pandas as pd

# Connect to MySQL
conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="********",
    database="Kucoin_orderbook"
)
cursor = conn.cursor()

# Fetch all data
query = "SELECT * FROM kucoin_orderbook.order_book;"
df = pd.read_sql(query, conn)

conn.close()

#...print(df.describe())
import matplotlib.pyplot as plt
# Fill missing values with median of each column
cols_to_fill = ["best_bid_price", "best_ask_price", "bid_ask_spread", "total_bid_volume", "total_ask_volume", "volume_imbalance", "mid_price"]
df[cols_to_fill] = df[cols_to_fill].fillna(df[cols_to_fill].median())

# Confirm missing values are fixed
#print("\nMissing Values After Fix:")
print(df.isnull().sum())
df.to_csv("clean_order_book.csv", index=False)


plt.hist(df["price_movement"], bins=50, color='blue', alpha=0.7)
plt.xlabel("Price Movement")
plt.ylabel("Frequency")
plt.title("Distribution of Price Movements")
plt.show()
import seaborn as sns

sns.boxplot(x=df["bid_ask_spread"])
plt.title("Bid-Ask Spread Distribution")
plt.show()

print(df["price_movement"].value_counts())





