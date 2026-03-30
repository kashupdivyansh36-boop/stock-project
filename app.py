import streamlit as st
import matplotlib.pyplot as plt

# Initialize session state (acts like array storage)
if "prices" not in st.session_state:
    st.session_state.prices = []

# Title
st.title("📊 Stock Price Tracker Dashboard")

# Input section
st.subheader("➕ Add Daily Stock Price")
price = st.number_input("Enter Price (₹)", min_value=0.0, step=1.0)

if st.button("Add Price"):
    st.session_state.prices.append(price)
    st.success(f"Added ₹{price}")

# Display prices
if st.session_state.prices:
    st.subheader("📋 Stored Prices")
    st.write(st.session_state.prices)

    # Plot graph
    st.subheader("📈 Price Chart")

    fig, ax = plt.subplots()
    ax.plot(st.session_state.prices, marker='o')
    ax.set_xlabel("Days")
    ax.set_ylabel("Price (₹)")
    ax.set_title("Stock Price Movement")

    st.pyplot(fig)

    # Analysis
    st.subheader("📊 Analysis")

    prices = st.session_state.prices
    avg_price = sum(prices) / len(prices)
    max_price = max(prices)
    min_price = min(prices)

    st.write(f"Average Price: ₹{avg_price:.2f}")
    st.write(f"Highest Price: ₹{max_price}")
    st.write(f"Lowest Price: ₹{min_price}")

    # Trend
    if prices[-1] > prices[0]:
        st.success("📈 Upward Trend")
    else:
        st.error("📉 Downward Trend")

else:
    st.info("No data added yet.")
