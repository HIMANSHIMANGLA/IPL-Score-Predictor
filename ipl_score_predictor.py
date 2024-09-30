import math
import numpy as np
import pickle
import streamlit as st

# Set page configuration
st.set_page_config(page_title='IPL Score Predictor', layout='centered')

# Load the ML model
filename = 'ml_model.pkl'
model = pickle.load(open(filename, 'rb'))

# Custom CSS for improved UI
st.markdown(
    """
    <style>
    /* General Page Styling */
    .stApp {{
        background-image: url("https://png.pngtree.com/thumb_back/fh260/background/20230714/pngtree-d-illustration-of-a-cricket-stadium-with-a-front-view-and-image_3857836.jpg");
        background-attachment: fixed;
        background-size: cover;
        color: #87CEEB;
    }}

    /* Make input fields stand out */
    .stNumberInput, .stSelectbox {{
        background-color: #87CEEB;
        border-radius: 10px;
        padding: 10px;
        font-size: 18px;
    }}

    /* Style the header */
    h1 {{
        color: #FFD700;
        font-family: 'Arial Black', sans-serif;
        font-size: 3em;
        text-shadow: 2px 2px 5px black;
    }}

    /* Style the buttons */
    .stButton>button {{
        background-color: #FFA500;
        color: white;
        font-size: 20px;
        border-radius: 10px;
        padding: 10px 20px;
        box-shadow: 2px 2px 5px #333;
    }}

    /* Style the error messages */
    .stAlert {{
        background-color: rgba(255, 0, 0, 0.2);
        color: red;
        border: 2px solid red;
        border-radius: 5px;
        padding: 10px;
    }}

    /* Footer Styling */
    footer {{
        text-align: center;
        margin-top: 30px;
    }}

    footer p {{
        color: white;
    }}

    footer a {{
        color: #FFD700;
        font-weight: bold;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Title of the app
st.markdown("<h1 style='text-align: center;'>IPL Score Predictor</h1>", unsafe_allow_html=True)

# Description section with collapsible expander
with st.expander("Description"):
    st.info("""
       The IPL Score Predictor is a machine learning project designed to forecast the first-inning scores of IPL matches. It leverages a dataset containing detailed ball-by-ball data from IPL seasons 2008 to 2020, applying various regression algorithms such as RandomForest, XGBoost, and others to identify patterns and improve prediction accuracy. The project features a user-friendly web application built with Streamlit, allowing users to input match parameters like overs, runs, and wickets for real-time score predictions.
    """)

# Create two columns for overs and runs input
col1, col2 = st.columns(2)

with col1:
    # Current overs input
    overs = st.number_input('Enter the Current Over', min_value=5.1, max_value=19.5, value=5.1, step=0.1)
    if overs - math.floor(overs) > 0.5:
        st.error('Please enter valid over input as one over only contains 6 balls')

with col2:
    # Current runs input
    runs = st.number_input('Enter Current runs', min_value=0, max_value=354, step=1, format='%i')

# Select batting and bowling teams
batting_team = st.selectbox('Select the Batting Team', 
                            ('Chennai Super Kings', 'Delhi Daredevils', 'Kings XI Punjab', 
                             'Kolkata Knight Riders', 'Mumbai Indians', 'Rajasthan Royals', 
                             'Royal Challengers Bangalore', 'Sunrisers Hyderabad'))

bowling_team = st.selectbox('Select the Bowling Team', 
                            ('Chennai Super Kings', 'Delhi Daredevils', 'Kings XI Punjab', 
                             'Kolkata Knight Riders', 'Mumbai Indians', 'Rajasthan Royals', 
                             'Royal Challengers Bangalore', 'Sunrisers Hyderabad'))

# Show error if both teams are the same
if bowling_team == batting_team:
    st.error('Bowling and Batting teams should be different')

# Prepare the team encoding for prediction
team_encoding = {'Chennai Super Kings': [1, 0, 0, 0, 0, 0, 0, 0],
                 'Delhi Daredevils': [0, 1, 0, 0, 0, 0, 0, 0],
                 'Kings XI Punjab': [0, 0, 1, 0, 0, 0, 0, 0],
                 'Kolkata Knight Riders': [0, 0, 0, 1, 0, 0, 0, 0],
                 'Mumbai Indians': [0, 0, 0, 0, 1, 0, 0, 0],
                 'Rajasthan Royals': [0, 0, 0, 0, 0, 1, 0, 0],
                 'Royal Challengers Bangalore': [0, 0, 0, 0, 0, 0, 1, 0],
                 'Sunrisers Hyderabad': [0, 0, 0, 0, 0, 0, 0, 1]}

prediction_array = team_encoding[batting_team] + team_encoding[bowling_team]

# Wickets slider input
wickets = st.slider('Enter Wickets fallen till now', 0, 9)

# More inputs for runs and wickets in the last 5 overs
col3, col4 = st.columns(2)

with col3:
    runs_in_prev_5 = st.number_input('Runs scored in the last 5 overs', min_value=0, max_value=runs, step=1, format='%i')

with col4:
    wickets_in_prev_5 = st.number_input('Wickets taken in the last 5 overs', min_value=0, max_value=wickets, step=1, format='%i')

# Add the numerical data to the prediction array
prediction_array += [runs, wickets, overs, runs_in_prev_5, wickets_in_prev_5]
prediction_array = np.array([prediction_array])

# Predict the score
if st.button('Predict Score'):
    predict = model.predict(prediction_array)
    predicted_score = int(round(predict[0]))

    # Display the predicted score
    st.markdown(f"""
    <div style='text-align: center; padding: 20px; border: 3px solid #FFA500; border-radius: 10px; background-color: rgba(255, 255, 255, 0.8);'>
        <h2 style='color: #000;'>Predicted Match Score: <strong>{predicted_score-5} to {predicted_score+5}</strong></h2>
    </div>
    """, unsafe_allow_html=True)

# Footer with IPL branding
st.markdown("""
<footer>
    <p>Powered by IPL Score Predictor | <a href="https://www.iplt20.com" target="_blank">Visit IPL Official Website</a></p>
</footer>
""", unsafe_allow_html=True)
