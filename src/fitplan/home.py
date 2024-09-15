import streamlit as st
from fitplan.athlete import Athlete

st.set_page_config(
    page_title="FitPlan",
    page_icon=":weight_lifter:"
)

if "db" not in st.session_state:
    st.session_state["db"] = None
if "currentAthlete" not in st.session_state:
    st.session_state["currentAthlete"] = Athlete()

st.title("FitPlan - Personal Fitness Planner")

# Connect to database
st.session_state.db = st.connection('fitplan_db', type='sql')

def setCurrentAthlete():
    st.session_state.currentAthlete.set(
        db=st.session_state.db,
        name = st.session_state.athletes_selectbox
    )

# Prepare the sidebar
athletes = st.session_state.currentAthlete.getAll(st.session_state.db)
current_athlete = st.sidebar.selectbox(
    label="Athletes",
    options = athletes["name"],
    index = None,
    key = "athletes_selectbox",
    placeholder = "Select an Athlete",
    label_visibility="collapsed",
    on_change = setCurrentAthlete
)

#st.write(st.session_state)
st.header(f"Athlete: {st.session_state.currentAthlete.name}", divider=True)
