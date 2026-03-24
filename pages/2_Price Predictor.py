import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.set_page_config(page_title='House Price Prediction')

# Load Data
with open('df.pkl','rb') as file:
    df = pickle.load(file)

# Load Pipeline Model
with open('model.pkl','rb') as file:
    model = pickle.load(file)

st.header('🏠 Enter Property Details')

# Inputs
property_type = st.selectbox('Property Type', ['flat','house'])

sector = st.selectbox('Sector', sorted(df['sector'].unique()))

bedroom = st.selectbox('Number Of BedRoom', sorted(df['bedRoom'].unique()))
bathroom = st.selectbox('Number Of BathRoom', sorted(df['bathroom'].unique()))
balcony = st.selectbox('Number Of Balcony', sorted(df['balcony'].unique()))

agePossession = st.selectbox('Property Age', sorted(df['agePossession'].unique()))

built_up_area = st.number_input("Built Up Area", min_value=100.0)


Servant_room = st.selectbox('Servant Room', [0, 1])
storeroom = st.selectbox('Store Room', [0, 1])

furnishing_type = st.selectbox('Furnishing Type', sorted(df['furnishing_type'].unique()))
luxury_category = st.selectbox('Luxury category', sorted(df['luxury_category'].unique()))
floor_category = st.selectbox('Floor category', sorted(df['floor_category'].unique()))

# DataFrame
columns = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony', 'agePossession',
           'built_up_area', 'servant room', 'store room',
           'furnishing_type', 'luxury_category', 'floor_category']

data = [[property_type, sector, bedroom, bathroom, balcony, agePossession,
         built_up_area, Servant_room, storeroom,
         furnishing_type, luxury_category, floor_category]]

input_data = pd.DataFrame(data, columns=columns)

# Prediction
if st.button('Predict'):

    prediction = model.predict(input_data)[0]
    base_price = np.expm1(prediction)


    low_price = base_price * 0.9
    high_price = base_price * 1.1

    st.success(f"💰 Price Range: ₹ {low_price:.2f} Cr - ₹ {high_price:.2f} Cr")