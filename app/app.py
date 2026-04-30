import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

import streamlit as st
from src.predict import predict_price
import json

with  open('models/columns.json','r') as f:
    columns = json.load(f)
locations = [col.replace('location_','') for col in columns if 'location_'in col]

st.set_page_config(page_title='ValueNest AI', layout ='centered')

st.title('ValueNest AI')
st.markdown('### Predict House Prices Instantly')
st.markdown('-----------')
st.write('Enter details to predict House Price')

#inputs
col1, col2 = st.columns(2)
with col1:
    total_sqft = st.number_input('Total Square Feet',min_value=300,max_value=10000,value=1000)

    bath = st.number_input('Bathrooms',min_value=1,max_value=10,value=2)

with col2:
    balcony = st.number_input('Balocnies',min_value=0,max_value=5,value=1)

    bhk = st.number_input('BHK',min_value=1,max_value=10,value=2)

location = st.selectbox('Select Location(e.g., Whitefield)',sorted(locations))

#button
if st.button('Predict Price'):
        price = predict_price(total_sqft, bath, balcony, bhk, location)

        st.success(f'Estimated Price : {price:.2f} Lakhs Rupees')

        st.info('Note:Prediction is based on historical data(~8 years old)')


st.sidebar.title('About')

st.sidebar.info("""
                
                This app Predicts House Price using Machine Learning.

                Model Used:
                - XGBoost (tuned)

                Features:
                - Area(sqft)
                - Location
                - BHK
                - Bathrooms
                - Balcony
""")