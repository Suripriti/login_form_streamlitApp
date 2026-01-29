import streamlit as st
import pymysql
con=pymysql.connect(
    host="localhost",
    user="root",
    password="tiger",
    database="student_db" 
)
st.title("Add a student details")
a=st.number_input("Enter student id")
b=st.text_input("Enter student name")
c=st.number_input("Enter student age")
if st.button("OK"):
    st.success("student details added successfully") 
else: 
    st.error("not added")  
 option=st.selectbox("Select your option",["Insert","Update","Delete","Display"])
if option=="Insert":
    cursor=con.cursor()
    query="insert into student values(%s,%s,%s)"
    values=(a,b,c)
    cursor.execute(query,values)
    con.commit()
    st.success("student details added successfully")
elif option=="Update":
    cursor=con.cursor()
    query="update student set name=%s,age=%s where id=%s"
    values=(b,c,a)
    cursor.execute(query,values)
    con.commit()
    st.success("student details updated successfully")
elif option=="Delete":
    cursor=con.cursor()
    query="delete from student where id=%s"
    values=(a,)
    cursor.execute(query,values)
    con.commit()
    st.success("student details deleted successfully") 
elif option=="Display":
    cursor=con.cursor()
    query="select * from student"
    cursor.execute(query)
    data=cursor.fetchall()
    for row in data:
        st.write("ID:",row[0]," Name:",row[1]," Age:",row[2])


    