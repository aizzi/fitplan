import pandas as pd
import streamlit as st
from fitplan.exceptions import DatabaseError

class Athlete:
    """Model an athlete and associated actions"""

    def __init__(self, id=None, name=None, birthday=None):
        """Initialize an athlete."""
        self.id = id
        self.name = name
        self.birthday = birthday

    def __str__(self):
        return f'Athlete\nid = {self.id}\nname = {self.name}\nbirthday = {self.birthday}'

    def getAll(self, db=None):
        """Return a list of all the athletes in the database
        
        Parameters
        db = st.connection object to database

        Return
        users = pandas dataframe
        """
        users = pd.DataFrame()
        try:
            users = db.query('SELECT * FROM athletes;', ttl=0)
        except:
            raise DatabaseError("Unable to retrieve list of athletes from database.")
        return users
    
    def set(self, db=None, name=None):
        """Set the current session's athlete"""
        if name is not None:
            try:
                athlete = db.query(f'SELECT * FROM athletes WHERE name="{name}";', ttl=0)
            except:
                raise DatabaseError(f"Unable to retrieve athlete {name}.")
            self.id = athlete.loc[0]["id"]
            self.name = athlete.loc[0]["name"]
            self.birthday = athlete.loc[0]["birthday"]
        

