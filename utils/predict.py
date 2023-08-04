import streamlit as st
import pickle
import pandas as pd
import numpy as np
import numpy 
from sklearn.preprocessing import StandardScaler

# file uploader

data = pd.read_csv('./data/final/clean_trial4.csv')

model_filename = "./models/LGBMRegressor_model.sav"
model = pickle.load(open(model_filename, 'rb'))


scaler_filename = pickle.load(open('./models/scaler.pkl', 'rb'))


def predict_permeability(compound_df):

    compound_df = np.reshape(compound_df, (1, -1))
    scaled = scaler_filename.transform(compound_df)
    
    predicted = model.predict(scaled)[0]
    predicted = round(predicted, 2)


    return predicted
    