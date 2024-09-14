import pandas as pd
from fitplan.exceptions import DatabaseError

class Athlete:
    """Model an athlete and associated actions"""

    def __init__(self, id=None, name=None, birthday=None):
        """Initialize an athlete."""
        self.id = id
        self.name = name
        self.birthday = birthday

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

