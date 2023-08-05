import streamlit as st
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# file uploader
dataset_path = './data/final/clean_trial4.csv'

model_filename = "./models/LGBMRegressor_model.sav"

scaler_filename = "./models/scaler.pkl"


@st.experimental_memo
def get_data() -> pd.DataFrame:
    print("loading data")
    return pd.read_csv(dataset_path)


@st.experimental_memo
def load_scaler():
    print("loading scaler")
    return pickle.load(open(scaler_filename, 'rb'))


@st.experimental_memo
def load_model():
    print("loading model")
    return pickle.load(open(model_filename, 'rb'))


model = load_model()

scaler = load_scaler()


def predict_permeability(compound_df):

    compound_df = np.reshape(compound_df, (1, -1))
    scaled = scaler.transform(compound_df)
    
    predicted = model.predict(scaled)[0]
    predicted = round(predicted, 2)


    return predicted
    