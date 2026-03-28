import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt

# Title
st.title("📊 Stock Market Dashboard")

# Input
stock = st.text_input("Enter Stock Name (Example: RELIANCE.NS)", "RELIANCE.NS")

# Button
if st.button("Show Data"):

    # Fetch data
    data = yf.download(stock, period="10d")

    if data.empty:
        st.write("❌ Invalid stock name")
    else:
        # Convert to array (list)
        prices = list(data['Close'])

        # Show prices
        st.write("📋 Prices (Array):", prices)

        # Plot chart
        plt.figure()
        plt.plot(prices)
        plt.title(stock)
        plt.xlabel("Days")
        plt.ylabel("Price")
        st.pyplot(plt)

        # Analysis
        st.write("📉 Daily Analysis:")
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                st.write(f"Day {i+1}: Increased 📈")
            elif prices[i] < prices[i-1]:
                st.write(f"Day {i+1}: Decreased 📉")
            else:
                st.write(f"Day {i+1}: No Change ➖")

        # Percentage Change
        change = ((prices[-1] - prices[0]) / prices[0]) * 100
        st.write(f"📊 Percentage Change: {change:.2f}%")