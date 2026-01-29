import streamlit as st
# title
st.title("Student CRUD Application ")
st.divider()   

#header
st.header("Student Records Management")
st.divider()   

# subheader
st.subheader("Manage student records with ease")

# horizontal line
st.markdown("----------------------------------------")

#text method to display information
st.text("This application allows you to create, read, update, and delete student records.")
st.divider()   
#write method to provide additional details
st.write("Hello streamlit")    
st.write(123)
st.write(45.67)
st.write(["apple", "banana", "cherry"])     
st.write({"name": "John", "age": 21})
st.divider()   
st.markdown("### this is markdown" )
st.markdown("**Bold Text** and *Italic Text*")
st.markdown("> This is a blockquote")
st.markdown("- item 1\n- item 2")
st.markdown("<h3 style='color:red'>Red Text</h3>", unsafe_allow_html=True)
st.divider()   
# caption 
st.caption("This is a caption providing additional context.")
st.divider()   
#code method to display code snippets
st.code(""" def add(a,b):
    return a + b """, language='python')
st.divider()   
# latex method to render mathematical expressions
st.latex(r''' a^2 + b^2 = c^2 ''')
st.divider()   
# divider method to separate sections
st.divider()
#button method to create interactive buttons
if st.button("Click Me"):
    st.write("Button clicked!")
    st.success("You have successfully clicked the button. ✅")
    st.balloons()
else:
    st.write("Button not clicked yet.")   
    st.error("connection error") 
st.divider()       
#text input method to get user input   
name=st.text_input("Enter your name:")
if name=="" :
    st.warning("it can not be empty  ❌")
elif not name.isalpha():
    st.error("Please enter a valid name containing only alphabetic characters. ❌")    
else:  
    st.success(f"Hello, {name}!")  
st.divider()   
#text area method to get multi-line user input    
feedback=st.text_area("Enter your feedback:")
st.write("Your feedback:", feedback) 
st.divider()   
# checkbox method to create checkboxes
if st.checkbox("I agree to the terms and conditions"):
    st.write("Thank you for agreeing!")
st.divider()       
# radio buttons method to create radio buttons
gender=st.radio("Select your gender:", ("Male", "Female", "Other"))
st.write("You selected:", gender)
st.divider()   
# selectbox method to create a dropdown menu
course=st.selectbox("Select your course:", ("Math", "Science", "History"))
st.write("You selected:", course)
st.divider()   
# multiselect method to create a multi-select dropdown
hobbies=st.multiselect("Select your hobbies:", ("Reading", "Traveling", "Gaming", "Cooking"))
st.write("You selected:", hobbies)
st.divider()   
# slider method to create a slider for numerical input
age=st.slider("Select your age:", 0, 100, 25)
st.write("Your age is:", age)
st.divider()   
#file uploader method to upload files
uploaded_file=st.file_uploader("Upload your profile picture:")
if uploaded_file is not None:
    st.write("File uploaded successfully:", uploaded_file.name)
    st.image(uploaded_file)  
st.divider()        
#form method to create a form 

with st.form("student_form"):
    name=st.text_input("Student Name:")
    age=st.number_input("Student Age:", min_value=0, max_value=120, step=1)
    submitted=st.form_submit_button("Submit")
    if submitted:
        st.write("Form submitted successfully!")
        st.write("Student Name:", name)
        st.write("Student Age:", age)  
st.divider()             
with st.form("login_form"):
    username=st.text_input("Username:")
    pwd=st.text_input("Password:", type="password")
    login=st.form_submit_button("Login")
    if login:
        st.success("Loggin successfully!")
st.divider()        
#columns method to create multiple columns
col1, col2, col3=st.columns(3)
with col1:
    st.header("Column 1")
    st.write("This is column 1.")
with col2:
    st.header("Column 2")
    st.write("This is column 2.")
with col3:
    st.header("Column 3")
    st.write("This is column 3.") 
st.divider()   
#caption method to add captions to elements
container=st.container()
container.write("This is inside the container.")
container.button("click me")
st.divider()
#table method to display data in tabular format
data = {
    'Name': ['Anurag', 'Sumit', 'Rohit'],
    'Age': [21, 22, 20],
    'Course': ['B.Tech', 'M.Tech', 'BBA']
}
st.table(data)       
st.divider()
#sidebar method to create a sidebar
st.sidebar.title("Menu")
option = st.sidebar.selectbox(
"Choose page",
["Home", "About", "Contact"]
)
st.sidebar.write(f"You selected: {option}") 
@st.cache_data
def load_data():
    return [1, 2, 3, 4, 5]
data = load_data()
st.write("Cached data:", data)
