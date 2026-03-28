import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt

# Title
st.title("📊 Stock Market Dashboard")

# Input
stock = st.text_input("Enter Stock Name (Example: RELIANCE.NS)", "RELIANCE.NS")

# Time period
period = st.selectbox("Select Time Period", ["1mo", "3mo", "6mo", "1y"])

# Button
if st.button("Show Data"):

    # Get data
    data = yf.download(stock, period=period)

    # Show raw data
    st.write("Raw Data:", data.tail())

    if data.empty:
        st.write("❌ Invalid stock name")
    else:
        # Clean data ONLY ONCE
        prices = list(data['Close'].dropna())

        # Check data
        st.write("Total Data Points:", len(prices))

        if len(prices) < 2:
            st.write("⚠ Not enough data")
        else:
            # Show prices
            st.subheader("📋 Prices")
            st.write(prices)

            # Chart
            st.subheader("📊 Price Chart")
            plt.figure()
            plt.plot(prices, marker='o')
            plt.title(stock)
            plt.xlabel("Days")
            plt.ylabel("Price")
            st.pyplot(plt)

            # Daily Analysis
          st.subheader("📊 Price Chart")

days = list(range(1, len(prices) + 1))

plt.figure()
plt.plot(days, prices, marker='o')
plt.title(stock)
plt.xlabel("Days")
plt.ylabel("Price")
st.pyplot(plt)

            # Summary
            st.subheader("📊 Summary")

            avg = sum(prices) / len(prices)
            max_price = max(prices)
            min_price = min(prices)

            st.write(f"Average Price: {avg:.2f}")
            st.write(f"Highest Price: {max_price:.2f}")
            st.write(f"Lowest Price: {min_price:.2f}")

            # Percentage Change
            if prices[0] != 0:
                change = ((prices[-1] - prices[0]) / prices[0]) * 100
                st.write(f"📈 Percentage Change: {change:.2f}%")
