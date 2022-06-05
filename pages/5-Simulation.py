import streamlit as st
import pandas as pd
import numpy as np
import pickle
import sklearn


st.markdown("# Simulation")
st.sidebar.markdown("# Simulation")

picklefile = open("modeles/dt.pkl", "rb")
model = pickle.load(picklefile)

df=pd.read_csv('data/echantillon.csv') #Read our data dataset
st.write(df.head()) 