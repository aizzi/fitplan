import streamlit as st
from fitplan.athlete import Athlete
from fitplan.exceptions import DatabaseError
from sqlalchemy.sql import text
import pandas as pd
import pytest

def execute_query(db, query=''):
    with db.session as s:
        q = text(query)
        s.execute(q)
        s.commit()

def test_athlete_init():
    """The Athlete is empty until instantiated"""
    athlete = Athlete()
    assert athlete.id == None
    assert athlete.name == None
    assert athlete.birthday == None

def test_athlete_getAll():
    """Returns all the athletes in the database"""
    athletes = pd.DataFrame()
    db = st.connection('memory_db', type='sql')
    execute_query(db, 'CREATE TABLE IF NOT EXISTS athletes (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, birthday TEXT);')
    execute_query(db, 'INSERT INTO athletes (name, birthday) VALUES ("A1", "B1"), ("A2", "B2")')
    athlete = Athlete()
    athletes = athlete.getAll(db)
    # Check that all the expected athletes are returned
    assert athletes.loc[0]["name"] == "A1"
    assert athletes.loc[0]["birthday"] == "B1"
    assert athletes.loc[1]["name"] == "A2"
    assert athletes.loc[1]["birthday"] == "B2"
    # Check that nothing else is returned
    assert athletes.shape[0] == 2
    # Check no database
    db = st.connection('no_db', type='sql')
    with pytest.raises(DatabaseError):
        athlete.getAll(db)
