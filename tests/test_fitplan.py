"""test_fitplan.py"""
from streamlit.testing.v1 import AppTest
import streamlit as st
from sqlalchemy.sql import text

def execute_query(db, query=''):
    with db.session as s:
        q = text(query)
        s.execute(q)
        s.commit()

def test_app_loading():
    """Verify that the application can start."""
    at = AppTest.from_file("src/fitplan/home.py").run()
    assert "FitPlan - Personal Fitness Planner" in at.title[0].value

def test_select_athlete():
    """Select the current athlete."""
    at = AppTest.from_file("src/fitplan/home.py")
    at.session_state.db = st.connection('memory_db', type='sql')
    execute_query(at.session_state.db, 'CREATE TABLE IF NOT EXISTS athletes (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, birthday TEXT);')
    execute_query(at.session_state.db, 'INSERT INTO athletes (name, birthday) VALUES ("Antonello", "1968/01/17"), ("Maria", "1970/04/23")')
    at.run()
    assert at.sidebar.selectbox(key="athletes_selectbox").value == None
    assert at.session_state.currentAthlete.name == None
    at.sidebar.selectbox(key="athletes_selectbox").select_index(0).run()
    assert at.sidebar.selectbox(key="athletes_selectbox").value == "Antonello"
    assert at.session_state.currentAthlete.name == "Antonello"
    at.sidebar.selectbox(key="athletes_selectbox").select_index(1).run()
    assert at.sidebar.selectbox(key="athletes_selectbox").value == "Maria"
    assert at.session_state.currentAthlete.name == "Maria"