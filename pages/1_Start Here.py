import streamlit as st
import pickle
import pandas as pd
import numpy as np
import sys
from utils.predict import *
from t1 import *

# file uploader
st.set_page_config(
    page_title="Skin Permeability",
    page_icon="👋",
)
st.set_option('deprecation.showPyplotGlobalUse', False)
# setting the title of our app
st.title("Skin Permeability Model")

sys.path.append('../')


data = get_data()


option = st.radio("Select Smiles or Compound Form", ['Smiles', 'Compound'])
smiles_flag = False
if option == "Smiles":
    smiles_flag = True

    compound = st.text_input('Enter your Compound in Smiles Structure', placeholder="C(=O)(N)N", value="C(=O)(N)N")
    st.write('The Smile you entered is: ', compound)
else:
    compound_names = list(data['Name'].unique())
    compound = st.selectbox("Select Compound", compound_names)
    st.write('The Compound you entered is: ', compound)

st.sidebar.markdown("# Predict Permeability")


def get_compound(smiles_flag=False):
    # search the disease # removing three columns
    if smiles_flag:
        
        st.success("Permeability:\n {}".format(extract_descriptors(compound)))
    else:        
        # search for compound
        compound_df = data[data['Name'] == compound]
    
        predicted = predict_permeability(compound_df)

        st.success("Permeability:\n {}".format(predicted))
    

st.button("Predict Permeability", on_click=get_compound, args=(smiles_flag, ))

if smiles_flag:
    molecule_img = draw_molecule_matplotlib(compound)
    st.image(molecule_img, width=400)