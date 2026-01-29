import streamlit as st
from mysql import connector
conn=connector.connect(
    host="localhost",
    user="root",
    password="tiger",
 
)
print("connecton established:",conn.is_connected())
# create the database
cursor=conn.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS registration_db")
print("database created")
# connect database
conn=connector.connect(
    host="localhost",
    user="root",
    password="tiger",
    database="registration_db"
)
cursor=conn.cursor()
print("connected to database:",conn.is_connected())

#create the table
cursor.execute("CREATE TABLE IF NOT EXISTS registration (username varchar(225), password VARCHAR(50))")

st.sidebar.title("Menu")
option = st.sidebar.radio(
"Choose page",
["registration", "login"]
)
#navigation 
if option == "registration":
    st.write("You selected registration page.")
    st.title("User Registration")
    with st.form("login_form"):
      username=st.text_input("Username:")
      pwd=st.text_input("Password:", type="password")
      login=st.form_submit_button("Login")
      if login:
        cursor=conn.cursor()
        query="INSERT INTO registration (username,password) VALUES (%s,%s)"
        values=(username,pwd)
        cursor.execute(query,values)
        conn.commit()
        st.success("User registered successfully")  
        st.balloons()
      else:
        st.error("Registration failed")
elif option == "login":
    st.write("You selected login page.")




