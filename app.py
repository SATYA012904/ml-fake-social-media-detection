

import streamlit as st
import joblib
import pandas as pd
import numpy as np

# Load the trained model, scaler, and column names
try:
    model_rf = joblib.load('model_rf_FSD.pkl')
    scaler = joblib.load('scaler.pkl')
    columns = joblib.load('columns.pkl')
except FileNotFoundError:
    st.error("Model, scaler, or columns file not found. Please ensure 'model_rf_FSD.pkl', 'scaler.pkl', and 'columns.pkl' are in the same directory.")
    st.stop()

st.set_page_config(layout='wide') # Use wide layout for better spacing

# --- Custom CSS for styling ---
st.markdown("""
<style>
/* General styling */
body {
    font-family: 'Roboto', sans-serif;
    color: #333;
    background-color: #f0f2f6;
}

/* Header styling */
h1 {
    color: #007bff; /* Blue color for main title */
    text-align: center;
    font-size: 2.5em;
    margin-bottom: 20px;
}

/* Subheader styling */
h3 {
    color: #28a745; /* Green color for subheaders */
    font-size: 1.5em;
    margin-top: 20px;
    margin-bottom: 10px;
}

/* Markdown text styling */
.stMarkdown {
    color: #555;
}

/* Sidebar styling */
.css-1d391kg.e16z0u0b4 {
    background-color: #ffffff; /* White sidebar background */
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

/* Button styling */
.stButton>button {
    background-color: #007bff; /* Blue button */
    color: white;
    font-weight: bold;
    border-radius: 5px;
    padding: 10px 20px;
    border: none;
    cursor: pointer;
    transition: background-color 0.3s ease;
}
.stButton>button:hover {
    background-color: #0056b3;
}

/* Info/Error/Success messages */
.stAlert.info {
    background-color: #e0f7fa;
    color: #007bff;
    border-left: 5px solid #007bff;
}
.stAlert.error {
    background-color: #ffebee;
    color: #dc3545;
    border-left: 5px solid #dc3545;
}
.stAlert.success {
    background-color: #e8f5e9;
    color: #28a745;
    border-left: 5px solid #28a745;
}

/* Progress bar styling */
.stProgress > div > div > div > div {
    background-color: #007bff; /* Blue progress bar */
}

</style>
""", unsafe_allow_html=True)


st.title('🕵️‍♂️ Fake Social Media Account Detector')
st.markdown("This application uses a Machine Learning model to predict whether a social media account is fake or real based on various account features. Adjust the sliders and selections on the left to see the prediction change.")
st.write('---')

# Input fields for features, organized into columns for better layout
st.sidebar.header('Account Features')

# Grouping related inputs

st.sidebar.markdown('### Username Characteristics')
col1, col2 = st.sidebar.columns(2)
with col1:
    username_length = st.slider('Username Length', 1, 30, 10)
    digits_count = st.slider('Digits Count in Username', 0, 20, 3)
with col2:
    special_char_count = st.slider('Special Character Count in Username', 0, 10, 1)
    repeat_char_count = st.slider('Repeat Character Count', 0, 15, 0) # Made interactive
username_randomness = st.sidebar.selectbox('Username Randomness', [0, 1], format_func=lambda x: 'Random' if x==1 else 'Not Random')

st.sidebar.markdown('### Engagement & Activity')
col1, col2 = st.sidebar.columns(2)
with col1:
    spam_comments_rate = st.slider('Spam Comments Rate (0-1)', 0.0, 1.0, 0.1, 0.01)
    posts = st.number_input('Number of Posts', 0, 10000, 100)
with col2:
    generic_comment_rate = st.slider('Generic Comment Rate (0-1)', 0.0, 1.0, 0.05, 0.01)
    posts_per_day = st.slider('Posts Per Day', 0.0, 10.0, 1.0, 0.1)
engagement_rate = st.sidebar.slider('Engagement Rate', 0.0, 1.0, 0.05, 0.01)

st.sidebar.markdown('### Follower/Following Data')
col1, col2 = st.sidebar.columns(2)
with col1:
    followers = st.number_input('Followers Count', 0, 50000, 400)
with col2:
    following = st.number_input('Following Count', 0, 5000, 700)
follower_following_ratio = st.sidebar.slider('Follower/Following Ratio', 0.0, 5.0, 1.0, 0.1)

st.sidebar.markdown('### Account Details')
account_age_days = st.sidebar.number_input('Account Age (days)', 0, 3650, 365)
has_profile_pic = st.sidebar.selectbox('Has Profile Picture', [0, 1], format_func=lambda x: 'Yes' if x==1 else 'No')

# Made interactive
verified = st.sidebar.checkbox('Verified Account', value=False)
suspicious_links_in_bio = st.sidebar.checkbox('Suspicious Links in Bio', value=False)

platform = st.sidebar.radio('Platform', ['Facebook', 'Instagram', 'X'])

platform_facebook = 1 if platform == 'Facebook' else 0
platform_instagram = 1 if platform == 'Instagram' else 0
platform_x = 1 if platform == 'X' else 0

# Create a dictionary of all input features in the correct order as per 'columns.pkl'
input_data = {
    'has_profile_pic': has_profile_pic,
    'username_randomness': username_randomness,
    'followers': followers,
    'following': following,
    'follower_following_ratio': follower_following_ratio,
    'account_age_days': account_age_days,
    'posts': posts,
    'engagement_rate': engagement_rate,
    'posts_per_day': posts_per_day,
    'spam_comments_rate': spam_comments_rate,
    'generic_comment_rate': generic_comment_rate,
    'verified': int(verified), # Now interactive
    'suspicious_links_in_bio': int(suspicious_links_in_bio), # Now interactive
    'username_length': username_length,
    'digits_count': digits_count,
    'special_char_count': special_char_count,
    'repeat_char_count': repeat_char_count, # Now interactive
    'platform_Facebook': platform_facebook,
    'platform_Instagram': platform_instagram,
    'platform_X': platform_x
}

input_df = pd.DataFrame([input_data])
input_df = input_df[columns] # Reorder columns to match the training data

st.write('## Prediction Result')

if st.button('Predict Account Status', type='primary'):
    # Scale the input features
    scaled_input = scaler.transform(input_df)

    # Make prediction
    prediction = model_rf.predict(scaled_input)
    prediction_proba = model_rf.predict_proba(scaled_input)

    col1, col2 = st.columns(2)

    with col1:
        if prediction[0] == 1:
            st.error('### This account is likely **FAKE** 🤖')
        else:
            st.success('### This account is likely **REAL** ✅')

    with col2:
        st.metric(label='Probability of being Fake', value=f'{prediction_proba[0][1]*100:.2f}%')
        st.progress(prediction_proba[0][1], text=f"Fake probability: {prediction_proba[0][1]*100:.2f}%")
        st.metric(label='Probability of being Real', value=f'{prediction_proba[0][0]*100:.2f}%')
        st.progress(prediction_proba[0][0], text=f"Real probability: {prediction_proba[0][0]*100:.2f}%")

else:
    st.info('Click the button above to get a prediction.')