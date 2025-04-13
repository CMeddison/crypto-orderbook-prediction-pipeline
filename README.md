# crypto-orderbook-prediction-pipeline
  A work-in-progress data pipeline that pulls real-time order book data from KuCoin's crypto exchange API, stores it in a MySQL database, and prepares the data for future predictive modeling
## 📌 Project Goals

- Connect to KuCoin's API and extract live order book data
- Store raw data in MySQL for analysis and modeling
- Build a foundational pipeline for crypto price trend prediction

## 🛠️ Tools & Technologies

- Python
- KuCoin API
- MySQL
- SQLAlchemy / MySQL Connector
- Pandas

## 🧠 What's Working

- Real-time data pull from KuCoin
- JSON parsing and transformation
- Database connection and storage of order book data

## 🔄 Next Steps

- Data cleaning and normalization
- Feature engineering (e.g. spread, volume imbalance)
- Train/test split for predictive modeling
- Build LSTM/ARIMA or ML model

## 📁 Structure

- `data_pipeline.py` – Script to fetch and store data from KuCoin
- `schema.sql` – SQL schema for MySQL table structure
- `requirements.txt` – List of required libraries

## 🙋‍♀️ About Me

I'm Chioma Margret Eddison, a Data Analyst passionate about building real-world data pipelines and using data to solve impactful problems.  
📍 Hamilton, Canada | [LinkedIn](https://www.linkedin.com/in/chioma-eddison-37748b310/)
