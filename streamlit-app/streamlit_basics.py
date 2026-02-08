import streamlit as st 
import pandas as pd 
st.title("My First Streamlit App")
st.header("1.Display Text")
st.subheader("This is subheader")
st.markdown("Streamlit can interpret **Markdow**, which makes it easy to format text.")
st.write("Welcome to the internchip crash course on Streamlit!")
data = {
    "Name": ["Banafsha", "Ubhat", "Zainab"],
    "Age": [21,21,20],
    "Department": ["CAi","CAi","CAi",],
    "Salary":[80000,70000,60000,]
}
df = pd.DataFrame(data)
print(df)
st.subheader("Interactive DataFrame")
st.dataframe(df)
st.subheader("Static Table")
st.table(df.head(3))
st.success("Success! The data was cleaned correctly. (st.success)")
st.info("Tip: You can download the report as a CSV below. (st.info)")
st.warning("Warning: 5 rows contained missing values and were dropped. (st.warning)")
st.error("Error: Could not connect to the database. (st.error)")

st.button("Click Me")
if st.button("Click me"):
    st.success("You clicked the button")
if st.checkbox("Show Message"):
    st.dataframe(df) 

age = st.slider("Select your age", 0,100,25)
st.write("You are", age, "years old")

name = st.text_input("Enter your name",)
if name:
    st.write(f"My name is {name}")

status = st.radio("What is your internship status?", ("Active", "Completed"))
if status == "Active":
    st.info("Keep up the good work!")
elif status == "Completed":
    st.success("Congratulations!")

role = st.selectbox ("Choose your role:", ["Data Analyst", "Data Scientist", "ML Engineer", "BI Developer"]) 
skills = st.multiselect("What tools do you use?", ["Python","SQL","Tableu","PoweBI","Excel","R"])

st.write(f"You selected {len(skills)} skills:")
st.write(skills)

uploaded_data = st.file_uploader("Choose a dataset", type=["csv","xlsx"])
if uploaded_data is not None:
    try:
        df=pd.read_csv(uploaded_data)
        st.success("CSV file uploaded successfully")

        st.subheader("Data Preview")
        st.dataframe(df.head())
    except Exception as e:
        st.error(f"Error reading file: {e}")    

