import streamlit as st

st.title("Simple Sales Dashboard")
st.selectbox("Select Month:", ["January", "February", "March", "April"], key="month")
sales = {
    "January": 1200,
    "February": 1500,
    "March": 900,
    "April": 2000
}
st.metric("Total Sales", sales[st.session_state.get("month", "January")])
st.bar_chart(sales, use_container_width=True)

