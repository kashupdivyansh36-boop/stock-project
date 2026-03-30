import streamlit as st
import matplotlib.pyplot as plt

# ---------------- ARRAY STORAGE ----------------
if "stocks" not in st.session_state:
    st.session_state.stocks = {}

st.title("📊 Stock Price Tracker (Time-Based Analysis)")

# ---------------- INPUT ----------------
st.sidebar.header("➕ Add Stock Data")

stock_name = st.sidebar.text_input("Enter Stock Name")
price = st.sidebar.number_input("Enter Price (₹)", min_value=0.0)

if st.sidebar.button("Add Price"):
    if stock_name:
        if stock_name not in st.session_state.stocks:
            st.session_state.stocks[stock_name] = []  # ARRAY

        st.session_state.stocks[stock_name].append(price)  # INSERT
        st.success(f"Added ₹{price} to {stock_name}")
    else:
        st.error("Enter stock name!")

# ---------------- DISPLAY ----------------
if st.session_state.stocks:

    selected_stock = st.selectbox(
        "📌 Select Stock",
        list(st.session_state.stocks.keys())
    )

    prices = st.session_state.stocks[selected_stock]  # ARRAY

    # ---------------- TIME FILTER ----------------
    st.subheader("⏳ Select Time Range")

    time_option = st.selectbox(
        "Choose Analysis Period",
        ["1 Day", "5 Days", "1 Month", "3 Months", "6 Months", "1 Year"]
    )

    # Map time to number of days
    time_map = {
        "1 Day": 1,
        "5 Days": 5,
        "1 Month": 30,
        "3 Months": 90,
        "6 Months": 180,
        "1 Year": 365
    }

    days = time_map[time_option]

    # ---------------- ARRAY SLICING ----------------
    if len(prices) >= days:
        filtered_prices = prices[-days:]   # LAST N DAYS
    else:
        filtered_prices = prices[:]        # ALL DATA

    st.subheader(f"📋 Data for Last {len(filtered_prices)} Days")
    st.write(filtered_prices)

    # ---------------- GRAPH ----------------
    st.subheader("📈 Price Chart")

    fig, ax = plt.subplots()
    ax.plot(filtered_prices, marker='o')
    ax.set_title(f"{selected_stock} ({time_option})")
    ax.set_xlabel("Days")
    ax.set_ylabel("Price (₹)")

    st.pyplot(fig)

    # ---------------- ANALYSIS ----------------
    st.subheader("📊 Analysis")

    total = 0
    for p in filtered_prices:   # ARRAY LOOP
        total += p

    avg = total / len(filtered_prices)

    st.write(f"Average Price: ₹{avg:.2f}")
    st.write(f"Highest Price: ₹{max(filtered_prices)}")
    st.write(f"Lowest Price: ₹{min(filtered_prices)}")

    # ---------------- PRICE CHANGE ----------------
    st.subheader("📉 Daily Change")

    for i in range(1, len(filtered_prices)):
        change = filtered_prices[i] - filtered_prices[i-1]
        st.write(f"Day {i} → Day {i+1}: ₹{change}")

    # ---------------- TREND ----------------
    if filtered_prices[-1] > filtered_prices[0]:
        st.success("📈 Uptrend")
    else:
        st.error("📉 Downtrend")

else:
    st.info("No data available")
