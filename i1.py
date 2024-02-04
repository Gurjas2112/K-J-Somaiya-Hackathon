import streamlit as st
import re

def validate_email(email):
    # Regular expression for validating email
    pattern = r"^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$"
    if re.match(pattern, email):
        return True
    else:
        return False

def main():
    # Set page title and favicon
    st.set_page_config(page_title="Student Performance Prediction", page_icon=":book:")

    # # Add custom CSS for background image
    # st.markdown(
    #     """
    #     <style>
    #     body {
    #         background-color: #f0f2f6;
    #         font-family: 'Arial', sans-serif;
    #     }
    #     .container {
    #         margin: 20px auto;
    #         padding: 20px;
    #         background-color: #ffffff;
    #         border-radius: 10px;
    #         box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    #     }
    #     .header {
    #         font-size: 20px;
    #         margin-bottom: 10px;
    #     }
    #     .input {
    #         margin-bottom: 10px;
    #         padding: 8px;
    #         border: 1px solid #ccc;
    #         border-radius: 5px;
    #         width: 100%;
    #     }
    #     .button {
    #         margin-top: 20px;
    #         padding: 10px 20px;
    #         background-color: #4CAF50;
    #         color: white;
    #         border: none;
    #         border-radius: 5px;
    #         cursor: pointer;
    #     }
    #     .button:hover {
    #         background-color: #45a049;
    #     }
    #     .selectbox {
    #         margin-bottom: 10px;
    #         padding: 8px;
    #         border: 1px solid #ccc;
    #         border-radius: 5px;
    #         width: 100%;
    #     }
    #     </style>
    #     """,
    #     unsafe_allow_html=True
    # )

    # Header
    st.markdown("<h1 class='header'>Welcome to Student Performance Prediction Model</h1>", unsafe_allow_html=True)

    # Form section
    with st.container():
        st.markdown("<h2 class='header'>User Information</h2>", unsafe_allow_html=True)
        name = st.text_input("Name", value="", help="Enter your name")
        age = st.number_input("Age", min_value=0, max_value=150, step=1, value=25, help="Enter your age")
        email = st.text_input("Email", value="", help="Enter your email")
        # Validate email on button click
        if st.button("Validate Email"):
            if validate_email(email):
                st.success("Valid email address!")
            else:
                st.error("Invalid email address. Please enter a valid email.")
        program = st.text_input("Program", value="", help="Enter your program")
        percentage = st.text_input("Percentage", value="", help="Enter your percentage")

    with st.container():
        st.markdown("<h3>Choose an Educational Resources</h3>", unsafe_allow_html=True)
        edu_res = ["Good", "Medium", "Satisfactory"]
        selected_option1 = st.selectbox("", edu_res)

    with st.container():
        st.markdown("<h3>Parents Education</h3>", unsafe_allow_html=True)
        parent_edu = ["Primary School", "High School", "Bachelor's Degree", "Master's Degree", "PhD"]
        selected_option2 = st.selectbox("", parent_edu)

    with st.container():
        st.markdown("<h3>Personality</h3>", unsafe_allow_html=True)
        personality = ["Extrovert", "Introvert", "Ambivert"]
        selected_option3 = st.selectbox("", personality)

    with st.container():
        ott_time = st.slider("Enter OTT time", 0, 6, 1)
        sm_time = st.slider("Enter social media time", 0, 6, 1)
        travel_time = st.slider("Enter travel time", 0, 6, 2)
        edu_vids_time = st.slider("Enter the time spent in educational videos", 0, 6, 2)
        game_time = st.slider("Enter game time", 0, 6, 2)
        extra_curri_time = st.slider("Enter the time spent in extra-curricular activities", 0, 6, 1)

    with st.container():
        st.markdown("<h4>AI Usage</h4>", unsafe_allow_html=True)
        ai_usage = ["Regular", "Ocassional", "Never"]
        selected_option4 = st.selectbox("", ai_usage)
        passion = st.radio("Do you enjoy what you are doing?", ["YES", "NO"])

    # Submit button
    submit_button = st.button("Submit")
    if submit_button:
        # Display submitted information
        st.success("Submitted Information")
        st.write(f"Name: {name}")
        st.write(f"Age: {age}")
        st.write(f"Email: {email}")
        st.write(f"Program: {program}")
        st.write(f"Percentage: {percentage}")
        st.write(f"Selected Education Option: {selected_option1}")
        st.write(f"Selected Parent's Education: {selected_option2}")
        st.write(f"Selected Personality: {selected_option3}")
        st.write(f"OTT Time: {ott_time}")
        st.write(f"Social Media Time: {sm_time}")
        st.write(f"Travel Time: {travel_time}")
        st.write(f"Educational Videos Time: {edu_vids_time}")
        st.write(f"Game Time: {game_time}")
        st.write(f"Extra-curricular Time: {extra_curri_time}")
        st.write(f"AI Usage: {selected_option4}")
        st.write(f"Passion about your doing: {passion}")

# if __name__ == "__main__":
main()


