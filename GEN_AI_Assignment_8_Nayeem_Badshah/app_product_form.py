import streamlit as st

st.sidebar.title("Product Form")
st.sidebar.text_input("Enter the product name:")
st.sidebar.selectbox("Select the product category:", ["Electronics", "Clothing", "Books", "Home & Kitchen"])
st.sidebar.number_input("Enter the product price:", min_value=0.0, step=0.01)

if st.sidebar.button("Submit Product Details"):
    st.sidebar.success("Product details submitted successfully!")
    st.sidebar.write("Product Name:", st.session_state.get("product_name", ""))
    st.sidebar.write("Product Category:", st.session_state.get("product_category", ""))
    st.sidebar.write("Product Price:", st.session_state.get("product_price", 0.0))