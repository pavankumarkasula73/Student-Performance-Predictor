import streamlit as st
import requests

# Streamlit App Title
st.title("🎓 Student Performance Predictor")

# Input fields for user
attendance = st.slider("Attendance (%)", 0, 100, 85)
assignments = st.slider("Assignment Score (%)", 0, 100, 90)
test_scores = st.slider("Test Scores (%)", 0, 100, 88)

# Button to predict grade
if st.button("Predict Grade"):
    try:
        # Prepare input data
        input_data = {
            "attendance": attendance,
            "assignments": assignments,
            "test_scores": test_scores
        }

        # Send request to Flask API
        response = requests.post("http://127.0.0.1:5000/predict", json=input_data)

        # Display the predicted grade
        if response.status_code == 200:
            predicted_grade = response.json().get('predicted_grade')
            st.success(f"🎉 Predicted Grade: **{predicted_grade}**")
        else:
            st.error("Error occurred while fetching prediction. Try again!")

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
