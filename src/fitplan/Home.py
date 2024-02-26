import streamlit as st

st.set_page_config(
    page_title="FitPlan",
    page_icon=":weight_lifter:"
)

if "db" not in st.session_state:
    st.session_state["db"] = None
if "users" not in st.session_state:
    st.session_state["users"] = None

st.title("FitPlan - Personal Fitness Planner")

# Connect to database
st.session_state.db = st.connection('fitplan_db', type='sql')