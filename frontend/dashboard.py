import requests
import streamlit as st

st.set_page_config(page_title="CSR Dashboard", page_icon="⚡", layout="wide")
API_URL = "http://127.0.0.1:8000"

st.title("⚡ CSR Naive Agent Control Panel")

tab1, tab2 = st.tabs(["Product Catalog", "Customer Lookup"])

with tab1:
    st.subheader("Catalog Management")
    try:
        res = requests.get(f"{API_URL}/products/")
        if res.status_code == 200:
            products = res.json()
            if products:
                st.dataframe(products, use_container_width=True)
            else:
                st.info("No products found. Run `make seed`.")
        else:
            st.error("Failed to load products.")
    except requests.exceptions.ConnectionError:
        st.error("Backend offline. Run `make backend`.")

with tab2:
    st.subheader("Customer Profile Lookup")
    cid = st.number_input("Customer ID", min_value=1, step=1)
    if st.button("Fetch Customer"):
        try:
            res = requests.get(f"{API_URL}/customers/{cid}")
            if res.status_code == 200:
                st.json(res.json())
            else:
                st.warning("Customer not found.")
        except requests.exceptions.ConnectionError:
            st.error("Backend offline.")
