import streamlit as st
import pickle
import pandas as pd
import numpy as np
import sys
sys.path.append('../')
from utils.predict import *
from t1 import *


st.set_option('deprecation.showPyplotGlobalUse', False)
# setting the title of our app
st.title("Skin Permeability Model")


data = get_data()


option = st.radio("Select Smiles or Compound Form", ['Smiles', 'Compound'])
smiles_flag = False
if option == "Smiles":
    smiles_flag = True

    smiles = st.text_input('Enter your Compound in Smiles Structure', placeholder="C(=O)(N)N", value="C(=O)(N)N")
    st.write('The Smile you entered is: ', smiles)
else:
    compound_names = list(data['Name'].unique())
    compound = st.selectbox("Select Compound", compound_names)
    st.write('The Compound you entered is: ', compound)

st.sidebar.markdown("# Predict Permeability")


def get_compound(smiles_flag=False):
    # search the disease # removing three columns
    if smiles_flag:
        st.success("Permeability: not yet {}")
        # st.success("Permeability:\n {}".format(extract_descriptors(compound)))
    else:        
        # search for compound
        compound_df = data[data['Name'] == compound]
    
        predicted = predict_permeability(compound_df)

        st.success("Permeability:\n {}".format(predicted))
    

st.button("Predict Permeability", on_click=get_compound, args=(smiles_flag, ))

# if not smiles is entered, we fetch the smile
if not smiles_flag:
    smiles = data[data['Name'] == compound]['SMILES'].values[0]
molecule_img = draw_molecule_matplotlib(smiles)
st.image(molecule_img, width=400)