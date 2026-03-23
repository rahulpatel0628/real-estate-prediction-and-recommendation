import streamlit as st
import pandas as pd
import numpy as np
import pickle
st.set_page_config(page_title='House Price Prediction')

#Load DataSet
with  open('df.pkl','rb') as file:
    df=pickle.load(file)

#Load Model
with  open('model.pkl','rb') as file:
    model=pickle.load(file)

#Take Inputs From Users
st.header('Enter your inputs')

#property_type
property_type=st.selectbox('Property Type',['flat','house'])

#sector
sector=st.selectbox('Sector',sorted(df['sector'].unique().tolist()))

#bedroom
bedroom=float(st.selectbox('Number Of BedRoom',sorted(df['bedRoom'].unique().tolist())))

#bathroom
bathroom=float(st.selectbox('Number Of BathRoom',sorted(df['bathroom'].unique().tolist())))

#balcony
balcony=st.selectbox('Number Of Balcony',sorted(df['balcony'].unique().tolist()))

#agePossession
agePossession=st.selectbox('Property Age',sorted(df['agePossession'].unique().tolist()))

#Builtup area
built_up_area=float(st.number_input("Built Up Area"))

#Servant Room
Servant_room=float(st.selectbox('Servant Room',[0.0,1.1]))

#Store Room
storeroom=float(st.selectbox('Number Of Store Room',[0.0,1.1]))

#'furnishing_type'
furnishing_type=st.selectbox('Furnishing Type',sorted(df['furnishing_type'].unique().tolist()))

#'luxury_category'
luxury_category=st.selectbox('Luxury category',sorted(df['luxury_category'].unique().tolist()))

#'floor_category'
floor_category=st.selectbox('Floor category',sorted(df['floor_category'].unique().tolist()))

columns=['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony', 'agePossession',
               'built_up_area', 'servant room', 'store room','furnishing_type', 'luxury_category',
               'floor_category']
data=[[property_type,sector,bedroom,bathroom,balcony,agePossession,built_up_area,Servant_room,
          storeroom,furnishing_type,luxury_category,floor_category]]
input_data=pd.DataFrame(data,columns=columns)


if st.button('Predict'):
    base_price=np.round(np.expm1(model.predict(input_data))[0],2)
    low_price=np.abs(base_price - 0.10)
    high_price=np.abs(base_price + 0.10)
    st.text(f"The Price Of {property_type} is Between {low_price} Cr and {high_price} Cr")



