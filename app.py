import streamlit as st
import pandas as pd
from textblob import TextBlob
from datetime import datetime
import random

# Sample stock list
stocks = ["AAPL", "GOOGL", "TSLA", "AMZN", "MSFT"]

# Dummy sentiment score generator
def get_sentiment_score(stock):
    return random.uniform(-1, 1)

# Recommend based on sentiment
def recommend_stock():
    sentiment_scores = {stock: get_sentiment_score(stock) for stock in stocks}
    sorted_stocks = sorted(sentiment_scores.items(), key=lambda x: x[1], reverse=True)
    return sorted_stocks

# ----------------- Streamlit Dashboard --------------------
st.set_page_config(page_title="Stock Recommender", layout="wide")
st.title("📈 Stock Sentiment Recommender")

st.markdown("This tool recommends stocks to buy based on online sentiment analysis from platforms like Twitter, Reddit, and News.")

if st.button("🔍 Get Recommendations"):
    st.write("### Top Recommended Stocks Today:")
    top_stocks = recommend_stock()
    df = pd.DataFrame(top_stocks, columns=["Stock", "Sentiment Score"])
    st.dataframe(df.style.background_gradient(cmap='YlGn'))

st.markdown("---")
st.caption("🚧 Sentiment is randomly generated now. In the next steps, we’ll fetch real-time sentiment from Twitter, Reddit, and news.")
