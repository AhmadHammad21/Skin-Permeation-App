import streamlit as st
import pickle
import pandas as pd
import numpy as np
import sys
sys.path.append('../')
from utils.predict import *
import os
print("Files", os.listdir())
from convert_java_to_python import extract_descriptors


st.set_option('deprecation.showPyplotGlobalUse', False)
# setting the title of our app
st.title("Skin Permeability Model")


data = get_data()


option = st.radio("Select Smiles or Compound Form", ['Smiles', 'Compound'])
smiles_flag = False
if option == "Smiles":
    smiles_flag = True

    smiles = st.text_input('Enter your Compound in Smiles Structure', placeholder="C(=O)(N)N", value="C(=O)(N)N")
else:
    compound_names = list(data['Name'].unique())
    compound = st.selectbox("Select Compound", compound_names)

st.sidebar.markdown("# Predict Permeability")


# if not smiles is entered, we fetch the smile
# else we get extract clean smiles and descriptors
if not smiles_flag:
    smiles = data[data['Name'] == compound]['SMILES'].values[0]
else:
    smiles, descriptors = extract_descriptors(smiles)


def get_compound(smiles_flag=False):
    # search the disease # removing three columns
    if smiles_flag:
        # list of descriptors
        compound_df = descriptors
    else:        
        # search for compound
        compound_df = data[data['Name'] == compound]
    
    predicted = predict_permeability(compound_df, new_smiles=smiles_flag)

    st.success("Permeability:\n {}".format(predicted))


st.button("Predict Permeability", on_click=get_compound, args=(smiles_flag, ))

# drawing image of compound
molecule_img = draw_molecule_matplotlib(smiles)
st.image(molecule_img, width=400)