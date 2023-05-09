import tensorflow as tf
import numpy as np
import streamlit as st

st.title("Etherum Price Prediction Application")

model = tf.keras.saving.load_model("Price_Prediction")

day_1 = st.number_input('Enter a first day price')
day_2 = st.number_input('Enter a second day price')
day_3 = st.number_input('Enter a third day price')
day_4 = st.number_input('Enter a fourth day price')
day_5 = st.number_input('Enter a fifth day price')
day_6 = st.number_input('Enter a sixth day price')
day_7 = st.number_input('Enter a seventh day price')

price_list = np.array([[day_1], [day_2], [day_3], [day_4], [day_5], [day_6], [day_7]])
prices = price_list.reshape(1, -1, 1)

if st.button('Price is'):
    prediction_price = model.predict(prices)
    prediction_price = prediction_price[0][0]

    def get_upper_lower(price):
       std_dev = np.std(prices)
       interval = 1.96 * std_dev 
       preds_mean = np.mean(prices)
       lower, upper = preds_mean - interval, preds_mean + interval
       return lower, upper

    lower, upper = get_upper_lower(price=price_list)
    array = [prediction_price, lower, upper]

    st.title("Predicted Ethereum Price: {0:.2f} \nMinimum Price Range:{1:.2f} \nMaximum Price Range:{2:.2f}".format(*array))

