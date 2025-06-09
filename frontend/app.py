import streamlit as st
from add_update_ui import add_update_tab
from analytics_ui import analytics_tab
from budget_ui import budget_tab
from analytics_by_month import analytics_months_tab



st.title("Expense Tracking System")

tab1, tab2,tab3,tab4 = st.tabs(["Add/Update", "Analytics","Budget","Analytics By Months"])

with tab1:
    add_update_tab()

with tab2:
    analytics_tab()

with tab3:
    budget_tab()

with tab4:
    analytics_months_tab()


