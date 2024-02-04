import streamlit as st

def main():
    # Set page title and favicon
    st.set_page_config(page_title="Student Performance Prediction", page_icon=":book:")

    # Add custom CSS for background image
    st.markdown(
        """
        <style>
        body {
            background-image: url('./img/pad.png');
            background-size: cover;
            font-family: 'Coming Soon';
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Header
    st.title("Welcome Student Performance Prediction Model")
    # st.write("This is a basic Streamlit app with minimal CSS styling.")

    # Form section
    st.header("User Information")
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0, max_value=150, step=1, value=25)
    email = st.text_input("Email")
    program = st.text_input("Program")
    percentage = st.text_input("Percentage")

    edu_res = ["Good", "Medium", "Satisfactory"]
    selected_option1 = st.selectbox("Choose an Educational Resources", edu_res)

    parent_edu = ["Primary School", "High School", "Bachelor's Degree", "Master's Degree", "PhD"]
    selected_option2 = st.selectbox("Parents Education", parent_edu)

    personality = ["Extrovert", "Introvert", "Ambivert"]
    selected_option3 = st.selectbox("Personality", personality)

    ott_time = st.slider("Enter OTT time", 0, 6, 1)
    sm_time = st.slider("Enter social media time", 0, 6, 1)
    travel_time = st.slider("Enter travel time", 0, 6, 2)
    edu_vids_time = st.slider("Enter the time spent in educational videos", 0, 6, 2)
    game_time = st.slider("Enter game time", 0, 6, 2)
    extra_curri_time = st.slider("Enter the time spent in extra-curricular activities", 0, 6, 1)
    ai_usage = ["Regular", "Sometimes", "Never"]
    selected_option4 = st.selectbox("AI Usage", ai_usage)
    passion = st.radio("Do you enjoy what you are doing?", ["YES", "NO"])

    # Submit button
    if st.button("Submit"):
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

if __name__ == "__main__":
    main()
