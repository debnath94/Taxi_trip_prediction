# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 16:31:53 2023

@author: debna
"""

import numpy as np
import pickle
from pickle import load
import streamlit as st
import scipy. stats as stats
from sklearn.ensemble import RandomForestRegressor

df = load(open('taxi.pickle', 'rb'))


st.title("Uber Fare analysis")


trip_duration = st. number_input("trip_duration [mins]", value = 0)

distance_traveled = st. number_input("distance_traveled [Km]", value = 0)

num_of_passengers = st. number_input("num_of_passengers", value = 0)

fare = st. number_input("fare", value = 0)

tip = st. number_input("tip", value = 0)

miscellaneous_fees = st. number_input("miscellaneous_fees", value = 0)

surge_applied = st. radio("surge_applied", ["Yes","No"])
if surge_applied == "Yes":
    surge_applied = 1
elif surge_applied == "No":
    surge_applied = 0

if st. button("Predict"):
    query_point = np. array([trip_duration, distance_traveled, num_of_passengers, fare, tip, miscellaneous_fees, surge_applied])
    query_point = query_point. reshape(1, -1)
    prediction = df.predict(query_point)
    st.write("The predicted fare is", prediction[0])


































