import streamlit as st
import pandas as pd

# streamlit page config
st.set_page_config(
    page_title="Predict Students Adaptability Level",
    page_icon="🔥",
    layout="wide"
)

# declare global variable


# declare global function


# section one : display dataset
st.caption("Dataset")
df = pd.read_csv("students_adaptability_level_online_education.csv")
st.dataframe(df, use_container_width=True)

# section two : machine learning process
st.caption("Prediction")
with st.form(key="predict_form"):

    # first row
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        user_name = st.text_input("Student's complete name")
    with col2:
        gender = st.selectbox("Gender type of student", ("Boy", "Girl"))
    with col3:
        age = st.selectbox("Age range of the student", ("1-5", "11-15", "16-20", "21-25", "26-30"))
    with col4:
        education_level = st.selectbox("Education institution level", ("School", "College", "University"))
    with col5:
        institution_type = st.selectbox("Education institution type", ("Non Goverment", "Goverment"))

    # second row
    col6, col7, col8, col9, col10 = st.columns(5)
    with col6:
        it_student = st.selectbox("Studying as IT student or not", ("False", "True"))
    with col7:
        location = st.selectbox("Is student location in town", ("False", "True"))
    with col8:
        load_shedding = st.selectbox("Level of load shedding", ("False", "True"))
    with col9:
        financial_condition = st.selectbox("Financial condition of family", ("Poor", "Mid", "Rich"))
    with col10:
        internet_type = st.selectbox("Internet type used mostly in device", ("Mobile Data", "Wifi"))

    # third row
    col11, col12, col13, col14, col15 = st.columns(5)
    with col11:
        network_type = st.selectbox("Network connectivity type", ("2G", "3G", "4G"))
    with col12:
        class_duration = st.selectbox("Daily class duration", ("0", "1-3", "3-6"))
    with col13:
        self_lms = st.selectbox("Institution's own LMS availability", ("No", "Yes"))
    with col14:
        device = st.selectbox("Device used mostly in class", ("Mobile", "Tab", "Computer"))
    with col15:
        validation = st.selectbox("Validation", ("Disagree", "Agree"))
    
    # submit
    predict_button = st.form_submit_button("Predict Students Adaptability Level", use_container_width=True)
    
# section three : display result
if predict_button:
    st.success("SUCCESS")

# section fourth : result description
