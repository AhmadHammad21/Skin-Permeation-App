import streamlit as st
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from rdkit import Chem
from rdkit.Chem import Draw
# fix CHEM mshan allah rdkit==2023.3.2


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

@st.cache_data
def get_data() -> pd.DataFrame:
    print("loading data")
    return pd.read_csv(dataset_path)


@st.cache_data
def get_data_cols() -> list:
    return pd.read_csv(dataset_cols_path).columns[3:]


@st.cache_data
def load_scaler():
    print("loading scaler")
    return pickle.load(open(scaler_filename, 'rb'))


@st.cache_data
def load_model():
    print("loading model")
    return pickle.load(open(model_filename, 'rb'))


all_data = get_data()

cols_used = get_data_cols()

model = load_model()

scaler = load_scaler()


def predict_permeability(compound_df: pd.DataFrame, new_smiles=False) -> float:
    if new_smiles:
        # exlcuding texpi
        temp_cols = cols_used[1:]
        
        column_indices = [all_data.columns.get_loc(col) - 1 for col in temp_cols]

        # we added index 0, since we added temperature (texpi), when generating this smile
        column_indices.insert(0, 0)
    
        # filtering on indices
        compound_df = np.array(compound_df)[column_indices]
        
    else:
        compound_df['Texpi'] = 310
        compound_df = compound_df[cols_used]
    
    compound_df = np.reshape(compound_df, (1, -1))
    scaled = scaler.transform(compound_df)
    
    predicted = model.predict(scaled)[0]
    predicted = round(predicted, 2)

    return predicted
    