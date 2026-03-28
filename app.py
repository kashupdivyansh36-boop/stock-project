import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt

st.title("📊 30+ Stock Comparison Dashboard")

# Default 30 stocks (India example)
default_stocks = "RELIANCE.NS,TCS.NS,INFY.NS,HDFCBANK.NS,ICICIBANK.NS,SBIN.NS,ITC.NS,LT.NS,HCLTECH.NS,WIPRO.NS,AXISBANK.NS,KOTAKBANK.NS,BAJFINANCE.NS,ASIANPAINT.NS,MARUTI.NS,TITAN.NS,SUNPHARMA.NS,ULTRACEMCO.NS,ONGC.NS,NTPC.NS,POWERGRID.NS,TATAMOTORS.NS,JSWSTEEL.NS,COALINDIA.NS,INDUSINDBK.NS,ADANIENT.NS,ADANIPORTS.NS,BPCL.NS,BRITANNIA.NS,CIPLA.NS"

stocks_input = st.text_area("Enter Stocks (comma separated)", default_stocks)

period = st.selectbox("Select Time Period", ["1mo", "3mo", "6mo", "1y"])

if st.button("Show Data"):

    stocks = stocks_input.split(",")

    plt.figure(figsize=(12,6))

    st.subheader("📊 Combined Chart (All Stocks)")

    for stock in stocks:
        stock = stock.strip()

        data = yf.download(stock, period=period)

        if data.empty:
            continue

        prices = list(data['Close'].dropna())

        if len(prices) < 2:
            continue

        # Normalize data (VERY IMPORTANT for comparison)
        base = prices[0]
        normalized = [(p/base)*100 for p in prices]

        plt.plot(normalized, label=stock)

        # Show small summary
        change = ((prices[-1] - prices[0]) / prices[0]) * 100
        st.write(f"{stock} → {change:.2f}%")

    plt.legend(fontsize=6)
    plt.title("Stock Comparison (Normalized)")
    plt.xlabel("Days")
    plt.ylabel("Growth (%)")
    st.pyplot(plt)
