import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt

# Title
st.title("📊 Multi Stock Market Dashboard")

# Input multiple stocks
stocks_input = st.text_input(
    "Enter Stock Names (comma separated)",
    "RELIANCE.NS,TCS.NS,INFY.NS"
)

# Time period
period = st.selectbox("Select Time Period", ["1mo", "3mo", "6mo", "1y"])

# Button
if st.button("Show Data"):

    # Convert input into list
    stocks = stocks_input.split(",")

    for stock in stocks:
        stock = stock.strip()  # remove spaces

        st.subheader(f"📌 {stock}")

        # Fetch data
        data = yf.download(stock, period=period)

        if data.empty:
            st.write("❌ No data found")
            continue

        # Clean data
        prices = list(data['Close'].dropna())

        if len(prices) < 2:
            st.write("⚠ Not enough data")
            continue

        # Show prices
        st.write("Total Data Points:", len(prices))

        # Chart
        plt.figure()
        plt.plot(prices, marker='o')
        plt.title(stock)
        plt.xlabel("Days")
        plt.ylabel("Price")
        st.pyplot(plt)

        # Percentage Change
        if prices[0] != 0:
            change = ((prices[-1] - prices[0]) / prices[0]) * 100
            st.write(f"📈 Change: {change:.2f}%")

        # Summary
        avg = sum(prices) / len(prices)
        st.write(f"Average Price: {avg:.2f}")
