import pandas as pd
import numpy as np
import streamlit as st
import pickle
from PIL import Image

import pickle

# Correctly load the model
with open('reg_model.pkl', 'rb') as file:
    regressor = pickle.load(file)

# The model is now available as 'regressor'

def prediction(Present_Price, Kms_Driven, Owner, no_year,
               Fuel_Type_Diesel, Fuel_Type_Petrol, Seller_Type_Individual,
               Transmission_Manual):   
    
    # Making a prediction using the trained model
    pred = regressor.predict(
        [[Present_Price, Kms_Driven, Owner, no_year,
          Fuel_Type_Diesel, Fuel_Type_Petrol, Seller_Type_Individual,
          Transmission_Manual]]
    )
    
    # Print and return the predicted value
    print(pred)
    return pred


def main(): 
      # giving the webpage a title 
    st.title("Car Price Prediction") 
      
    # here we define some of the front end elements of the web page like  
    # the font and background color, the padding and the text to be displayed 
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Streamlit Car Price Prediction ML App </h1> 
    </div> 
    """
      
    # this line allows us to display the front end aspects we have  
    # defined in the above code 
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # the following lines create text boxes in which the user can enter  
    # the data required to make the prediction 
     
    Present_Price = st.text_input("Present Price", "Type Here") 
    Kms_Driven = st.text_input("Kms", "Type Here") 
    Owner = st.text_input("Owner", "Type Here")
    no_year = st.text_input("No of years", "Type Here") 
    Fuel_Type_Diesel = st.text_input("Diesel Fuel Type", "Type Here") 
    Fuel_Type_Petrol = st.text_input("Petrol Fuel Type", "Type Here") 
    Seller_Type_Individual = st.text_input("Seller Type", "Type Here")
    Transmission_Manual = st.text_input("Transmission Manual", "Type Here")
    result ="" 

    if st.button("Predict"): 
        result = prediction(Present_Price, Kms_Driven, Owner, no_year, Fuel_Type_Diesel, Fuel_Type_Petrol, Seller_Type_Individual, Transmission_Manual) 
    st.success('The output is {}'.format(result)) 
     
if __name__=='__main__': 
    main() 