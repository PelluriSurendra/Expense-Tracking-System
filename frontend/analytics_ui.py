import streamlit as st
from datetime import datetime
import requests
import pandas as pd


API_URL = "http://localhost:8000"


def analytics_tab():
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start Date", datetime(2024, 8, 1))

    with col2:
        end_date = st.date_input("End Date", datetime(2024, 8, 5))

    if st.button("Get Analytics"):
        payload = {
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d")
        }

        response = requests.post(f"{API_URL}/analytics/", json=payload)
        response = response.json()


        data = {
            "Category": list(response.keys()),
            "Total": [response[category]["total"] for category in response],
            "Percentage": [response[category]["percentage"] for category in response]
        }

        df = pd.DataFrame(data)
        df_sorted = df.sort_values(by="Percentage", ascending=False)

        st.title("Expense Breakdown By Category")

        st.bar_chart(data=df_sorted.set_index("Category")['Percentage'], width=0, height=0, use_container_width=True)

        df_sorted["Total"] = df_sorted["Total"].map("{:.2f}".format)
        df_sorted["Percentage"] = df_sorted["Percentage"].map("{:.2f}".format)

        st.table(df_sorted)

        # --- Fetch Monthly Budget ---
        # Use the month of the end_date for budget lookup
        year, month = end_date.year, end_date.month
        budget_resp = requests.get(f"{API_URL}/budget/{year}/{month}")
        if budget_resp.status_code == 200:
            budget_amount = budget_resp.json()["amount"]
        else:
            # If no budget set, default to 0 (or prompt user elsewhere)
            budget_amount = 0.0

        # --- Compute Totals ---
        total_spent = sum([response[c]["total"] for c in response])

        # --- Display Budget Progress ---
        if budget_amount > 0:
            st.markdown("### 📊 Budget vs. Actual Spending")
            percent_used = min(total_spent / budget_amount, 1.0)
            st.progress(percent_used)

            # Display numbers
            st.write(f"**Budget:** ₹{budget_amount:.2f}")
            st.write(f"**Spent:** ₹{total_spent:.2f}")
            st.write(f"**Remaining:** ₹{(budget_amount - total_spent):.2f}")

            # Alert if over budget
            if total_spent > budget_amount:
                st.error(f"⚠️ You have exceeded your budget by ₹{(total_spent - budget_amount):.2f}!")
            else:
                st.success("✅ You are within your budget.")
        else:
            st.info("ℹ️ No budget set for this month. Set one in the **Budget** tab.")

        
