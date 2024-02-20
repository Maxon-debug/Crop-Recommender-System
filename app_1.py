import streamlit as st 
import pandas as pd
import numpy as np
import os
import pickle
import warnings


#st.beta_set_page_config(page_title="Crop Recommender", page_icon="🌿", layout='centered', initial_sidebar_state="collapsed")

def load_model(modelfile):
	loaded_model = pickle.load(open(modelfile, 'rb'))
	return loaded_model

def main():
    # title
    html_temp = """
    <div>
    <h1 style="color:blue;text-align:LEFT;"> WAKULIMA PRIDE <h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    col1,col2  = st.columns([2,2])
    
    #with col1: 
        
       


    with col2:
        html_temp = """
        <div>
        <h2 style="color:red">
        DO YOU KNOW YOU CAN FIND OUT THE BEST CROP TO PLANT IN YOUR FARM??
        </h2>
        <h3 style="color:green">
        TRY THIS APP>>
        </h3>
        </div>
        """
        st.markdown(html_temp, unsafe_allow_html=True)
        N = st.number_input("Nitrogen", 1,10000)
        P = st.number_input("Phosporus", 1,10000)
        K = st.number_input("Potassium", 1,10000)
        temp = st.number_input("Temperature",0.0,100000.0)
        humidity = st.number_input("Humidity in %", 0.0,100000.0)
        ph = st.number_input("Ph", 0.0,100000.0)
        rainfall = st.number_input("Rainfall in mm",0.0,100000.0)

        feature_list = [N, P, K, temp, humidity, ph, rainfall]
        single_pred = np.array(feature_list).reshape(1,-1)
        
        if st.button('Predict'):

            loaded_model = load_model('model.pkl')
            prediction = loaded_model.predict(single_pred)
            col1.write('''
		    ## Results 🔍 
		    ''')
            col1.success(f"{prediction.item().title()} ARE THE BEST CROPS TO PLANT IN YOUR FARM UNDER THOSE CONDITIONS.")
      #code for html ☘️ 🌾 🌳 👨‍🌾  🍃

   
    hide_menu_style = """
    <style>
    #MainMenu {visibility: hidden;}
    </style>
    """

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

if __name__ == '__main__':
	main()
