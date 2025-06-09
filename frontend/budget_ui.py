import streamlit as st
import requests
from datetime import datetime

API_URL = "http://localhost:8000"

def budget_tab():
    st.header("📊 Monthly Budget Management")

    now = datetime.now()
    col1, col2 = st.columns(2)

    with col1:
        year = st.number_input("Year", min_value=2000, max_value=2100, value=now.year)

    with col2:
        month = st.selectbox("Month", list(range(1, 13)), index=now.month - 1)

    if st.button("Fetch Budget"):
        response = requests.get(f"{API_URL}/budget/{year}/{month}")
        if response.status_code == 200:
            budget = response.json()["amount"]
            st.success(f"Budget for {month}/{year} is ₹{budget:.2f}")
        elif response.status_code == 404:
            st.warning("No budget set for this month.")
        else:
            st.error("Failed to retrieve budget.")

    st.markdown("---")
    st.subheader("💾 Set / Update Budget")
    new_budget = st.number_input("Enter Budget Amount", min_value=0.0, step=100.0)

    if st.button("Save Budget"):
        payload = {
            "year": year,
            "month": month,
            "amount": new_budget
        }
        response = requests.post(f"{API_URL}/budget/", json=payload)
        if response.status_code == 200:
            st.success("Budget saved successfully.")
        else:
            st.error("Failed to save budget.")
