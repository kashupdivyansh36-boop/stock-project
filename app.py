import streamlit as st
import matplotlib.pyplot as plt

# ---------------- ARRAY STORAGE ----------------
# stocks = { "TATA": [100,120,110] }
if "stocks" not in st.session_state:
    st.session_state.stocks = {}

st.title("📊 Stock Price Tracker (Array Based)")

# ---------------- INPUT ----------------
st.sidebar.header("➕ Add Stock Data")

stock_name = st.sidebar.text_input("Enter Stock Name")
price = st.sidebar.number_input("Enter Price (₹)", min_value=0.0)

# ---------------- INSERT INTO ARRAY ----------------
if st.sidebar.button("Add Price"):
    if stock_name:
        # Create array if not exists
        if stock_name not in st.session_state.stocks:
            st.session_state.stocks[stock_name] = []   # ARRAY CREATED

        # Insert into array
        st.session_state.stocks[stock_name].append(price)

        st.success(f"Added ₹{price} to {stock_name}")
    else:
        st.error("Enter stock name!")

# ---------------- DISPLAY ----------------
if st.session_state.stocks:

    selected_stock = st.selectbox(
        "Select Stock",
        list(st.session_state.stocks.keys())
    )

    # ARRAY FETCH
    prices = st.session_state.stocks[selected_stock]

    st.subheader("📋 Stored Prices (Array)")
    st.write(prices)

    # ---------------- ARRAY ITERATION ----------------
    st.subheader("📊 Price List")
    for i in range(len(prices)):
        st.write(f"Day {i+1}: ₹{prices[i]}")

    # ---------------- GRAPH ----------------
    st.subheader("📈 Graph")
    fig, ax = plt.subplots()
    ax.plot(prices, marker='o')
    st.pyplot(fig)

    # ---------------- ANALYSIS USING ARRAY ----------------
    st.subheader("📊 Analysis")

    total = 0
    for price in prices:   # ARRAY LOOP
        total += price

    avg = total / len(prices)

    st.write(f"Average Price: ₹{avg:.2f}")
    st.write(f"Max Price: ₹{max(prices)}")
    st.write(f"Min Price: ₹{min(prices)}")

    # ---------------- PRICE CHANGE ----------------
    st.subheader("📉 Daily Change")

    for i in range(1, len(prices)):
        change = prices[i] - prices[i-1]
        st.write(f"Day {i} → Day {i+1}: ₹{change}")

else:
    st.info("No data available")
