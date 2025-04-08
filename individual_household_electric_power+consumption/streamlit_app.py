import streamlit as st
import pandas as pd 
import numpy as np
import pickle 
from xgboost import XGBRegressor

# Load the model from the pickle file
with open ('xgb_model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title('Electricity power consumption prediction')
st.markdown('Excute the prediction by entering the values below')

# Input fields for the user to enter data
voltage = st.number_input('Voltage', min_value=0.0, max_value=300.0, value=240.0)
reactive_power = st.number_input('Global Reactive Power', min_value=0.0, max_value=5.0, value=0.2)
intensity = st.number_input('Global Intensity', min_value=0.0, max_value=30.0, value=4.0)
sub1 = st.number_input('Sub_metering_1', min_value=0.0, max_value=20.0, value=1.0)
sub2 = st.number_input('Sub_metering_2', min_value=0.0, max_value=20.0, value=1.0)
sub3 = st.number_input('Sub_metering_3', min_value=0.0, max_value=20.0, value=1.0)
year = st.number_input('Year', min_value=2000, max_value=2100, value=2010)
month = st.slider('Month', 1, 12, 6)
day = st.slider('Day', 1, 31, 15)
dayofweek = st.selectbox('Day of Week (0=Monday)', list(range(7)), index=0)
lag1 = st.number_input('Lag1', min_value=0.0, max_value=10.0, value=1.2)
Lag7 = st.number_input('Lag7', min_value=0.0, max_value=10.0, value=1.5)
rolling_mean_7 = st.number_input('Rolling mean_7', min_value=1.0, max_value=10.0, value=1.3)

# Excute the prediction
if st.button('Predict'):
    # Create a DataFrame with the input data
    input_df = pd.DataFrame({
        'Global_reactive_power': [reactive_power],
        'Voltage': [voltage],
        'Global_intensity': [intensity],
        'Sub_metering_1': [sub1],
        'Sub_metering_2': [sub2],
        'Sub_metering_3': [sub3],
        'Year': [year],
        'Month': [month],
        'Day': [day],
        'Dayofweek': [dayofweek],
        'Lag1': [lag1],
        'Lag7': [Lag7],
        'Rolling_Mean_7': [rolling_mean_7]
        })

    # Make the prediction
    prediction = model.predict(input_df)[0]

    # Display the prediction result
    st.success(f'The predicted electricity power consumption is: {prediction:2f} kW')