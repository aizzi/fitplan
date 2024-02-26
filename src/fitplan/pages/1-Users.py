import streamlit as st
from sqlalchemy.sql import text
import datetime

st.header("User's Management")

def execute_query(query=''):
    with st.session_state.db.session as s:
        q = text(query)
        s.execute(q)
        s.commit()

def get_users():
    try:
        st.session_state.users = st.session_state.db.query('SELECT * FROM users;', ttl=0)
    except Exception as error:
        st.write("Error: unable to read users from db.")

def add_user(user_name, birthday):
    st.write("add user")
    execute_query(f'INSERT INTO users (name, birthday) VALUES ("{user_name}", "{birthday}");')

# Create the USERS table if it does not exist
execute_query('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, birthday TEXT);')

# Add a user to the database
with st.form("new_user", clear_on_submit=True):
    st.write("Create a new user")
    col1, col2, col3 = st.columns(3)
    with col1:
        user_name = st.text_input("Name")
    with col2:
        birthday = st.date_input("Birthday", value=None, min_value=datetime.datetime(1900,1,1), max_value=datetime.datetime.now())
    with col3:
        submitted = st.form_submit_button("Submit")
    if submitted:
        add_user(user_name, birthday)

get_users()
st.dataframe(st.session_state.users, use_container_width=True, hide_index=True)
