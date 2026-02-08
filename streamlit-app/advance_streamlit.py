import streamlit as st 
import pandas as pd 
st.title("My First dashboard Layout")
st.sidebar.title("This is side bar title")
st.sidebar.header("User Controls")

# username = st.sidebar.text_input("Enter your name")
# region = st.sidebar.selectbox("Select Region", ["North","South","East","West"])
# if username:
#     st.write(f"Hello **{username}**, showing data for: **{region}**")

# st.subheader("1. Key Metrics (Using Columns)")    
# col1,col2,col3 = st.columns(3)
# with col1:
#     st.metric(label="Total Sales", value="$50,000", delta="10%")
# with col2:
#     st.metric(label="Active Users", value="1,200", delta="-2%") 
# with col3:
#     st.metric(label="Customer Satisfaction", value="4.8/5", delta="0.2")  
        
data = {
    "Name": ["Banafsha", "Ubhat", "Zainab"],
    "Age": [21,21,20],
    "Department": ["CAi","CAi","CAi",],
    "Salary":[80000,70000,60000,]
}

df = pd.DataFrame(data)
tab1, tab2 = st.tabs(["Raw Data", "Notes"])
with tab1:
    st.dataframe(df)
with tab2:
    st.info("Note: Data was last updated on Dec 23rd.")    
# st.title ("The Problem: Variables reset on every click")

# count = 0
# st.write(f"The counter value is: {count}")
# if st.button("Add +1"):
#     count +=1
#     st.write(f"Button clicked Inside the 'if', count is {count}")
# st.error("Notice: The counter above never stays at 1 because the script resets!")    

if 'my_counter' not in st.session_state:
    st.session_state['my_counter']=0
st.write(f"The saved counter value is : **{st.session_state.my_counter}**")
if st.button("Add +1"):
    st.session_state.my_counter +=1
    st.write(f"Button clicked Insode the 'if', count is {st.session_state.my_counter}")
st.success("Notice:  Now the number grows beacuse Streamlit 'remembers' it!")






