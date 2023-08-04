import streamlit as st
import pickle
import pandas as pd
import numpy as np
import sys
sys.path.append('../')
from utils.predict import predict_permeability


# file uploader
st.set_page_config(
    page_title="Skin Permeability",
    page_icon="👋",
)
# setting the title of our app
st.title("Skin Permeability Model")

dataset_path = './data/final/clean_trial4.csv'

@st.experimental_memo
def get_data() -> pd.DataFrame:
    return pd.read_csv(dataset_path)

data = get_data()

model_filename = "./models/LGBMRegressor_model.sav"
model = pickle.load(open(model_filename, 'rb'))

scaler_filename = pickle.load(open('./models/scaler.pkl', 'rb'))


option = st.radio("Select Smiles or Compound Form", ['Smiles', 'Compound'])
smiles_flag = False
if option == "Smiles":
    smiles_flag = True

    title = st.text_input('Enter your Compound in Smiles Structure', placeholder="C(=O)(N)N")
    st.write('The Smile you entered is: ', title)
else:
    compound_names = list(data['Compound'].unique())
    compound = st.selectbox("Select Compound", compound_names)
    st.write('The Compound you entered is: ', compound)
st.sidebar.markdown("# Predict Permeability")


def get_compound(smiles_flag=False):
    # search the disease # removing three columns
    if smiles_flag:
        pass

    
    # search for compound
    compound_df = data[data['Compound'] == compound].iloc[0, 3:].values
  
    compound_df = np.reshape(compound_df, (1, -1))

    predicted = predict_permeability(compound_df)

    st.success("Permeability:\n {}".format(predicted))
    

st.button("Predict Permeability", on_click=get_compound, args=(smiles_flag))
