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
    st.title("Welcome to My Simple Streamlit App")
    st.write("This is a basic Streamlit app with minimal CSS styling.")

    # Form section
    st.header("User Information")
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0, max_value=150, step=1, value=25)
    email = st.text_input("Email")
    program = st.text_input("Program")
    percentage = st.text_input("Percentage")
  

edu_res = ["Good", "Medium", "Satisfactory"]
# Create the dropdown for educational resources
selected_option1 = st.selectbox("Choose an option", edu_res)

# Process the selected option
# if selected_option1:
    # st.write("You selected:", selected_option1)

parent_edu = ["Primary School", "High School", "Bachelor's Degree", "Master's Degree", "PhD"]
# Create the radio button for parent's education
selected_option2 = st.radio("Parents Education", parent_edu)

# Process the selected option
if selected_option2:
    # st.write("You selected:", selected_option2)

    personality = st.radio("Choose an option", ["Extrovert", "Introvert", "Ambivert"])

    # passion = st.text_input()
    ott_time = st.slider("Enter OTT time", 0, 6, 1)
    sm_time = st.slider("Enter social media time", 0, 6, 1)
    travel_time = st.slider("Enter travel time", 0, 6, 2)
    edu_vids_time = st.slider("Enter the time spent in educatonal videos", 0, 6, 2)
    game_time = st.slider("Enter game time", 0, 6, 2)
    extra_curri_time = st.slider("Enter the time spent in extra-curricular activites", 0, 6, 1)
    ai_usage = st.checkbox("Regular", "Not Regular", "Never")

    # Submit button
    if st.button("Submit"):
        # Display submitted information
        st.success("Submitted Information")
        st.write(f"Name: {name}")
        st.write(f"Age: {age}")
        st.write(f"Email: {email}")
        # st.write(f"Program: {program}")
        # st.write(f"Percentage: {percentage}")

# if __name__ == "__main__":
    main()
