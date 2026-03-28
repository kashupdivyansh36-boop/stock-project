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

    if data.empty:
        st.write("❌ Invalid stock name")
    else:
        # Clean data (best method)
        prices = list(data['Close'].dropna())

        # Check data
        st.write("Total Data Points:", len(prices))

        if len(prices) < 2:
            st.write("⚠ Not enough data")
        else:
            # Show prices
            st.subheader("📋 Prices (Array)")
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
            st.subheader("📉 Daily Analysis")
            for i in range(1, len(prices)):
                if prices[i] > prices[i-1]:
                    st.write(f"Day {i+1}: Increased 📈")
                elif prices[i] < prices[i-1]:
                    st.write(f"Day {i+1}: Decreased 📉")
                else:
                    st.write(f"Day {i+1}: No Change ➖")

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
