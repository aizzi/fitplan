"""test_fitplan.py"""
from streamlit.testing.v1 import AppTest

def test_app_loading():
    at = AppTest.from_file("src/fitplan/fitplan.py").run()
    assert "FitPlan - Personal Fitness Planner" in at.title[0].value