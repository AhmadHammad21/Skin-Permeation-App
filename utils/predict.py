import streamlit as st
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from rdkit import Chem
from rdkit.Chem import Draw


def draw_molecule_matplotlib(smiles):
    molecule = Chem.MolFromSmiles(smiles)
    if molecule is not None:
        img = Draw.MolToImage(molecule)
        return img
    else:
        print("Invalid SMILES string provided.")

# file uploader
dataset_path = './data/raw/DrugBank-descriptors.csv'

# for columns extraction
dataset_cols_path = './data/final/clean_trial4.csv'

model_filename = "./models/LGBMRegressor_model.sav"

scaler_filename = "./models/scaler.pkl"

# draw_molecule_matplotlib("C(=O)(N)N")

@st.experimental_memo
def get_data() -> pd.DataFrame:
    print("loading data")
    return pd.read_csv(dataset_path)


@st.experimental_memo
def get_data_cols() -> list:
    return pd.read_csv(dataset_cols_path).columns[3:]


@st.experimental_memo
def load_scaler():
    print("loading scaler")
    return pickle.load(open(scaler_filename, 'rb'))


@st.experimental_memo
def load_model():
    print("loading model")
    return pickle.load(open(model_filename, 'rb'))


cols_used = get_data_cols()

model = load_model()

scaler = load_scaler()


def predict_permeability(compound_df: pd.DataFrame) -> float:
    compound_df['Texpi'] = 310
    compound_df = compound_df[cols_used]
    
    compound_df = np.reshape(compound_df, (1, -1))
    scaled = scaler.transform(compound_df)
    
    predicted = model.predict(scaled)[0]
    predicted = round(predicted, 2)

    return predicted
    