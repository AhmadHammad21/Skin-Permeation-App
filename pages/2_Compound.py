import streamlit as st
import pickle
import pandas as pd
import numpy as np
from ..utils.predict import predict_permeability

# setting the title of our app
# st.title("Skin Permeability")

# st.markdown("### Welcome to the Website")
# st.sidebar.markdown("# Choose Smiles or Compound")
# st.markdown("### Explore our Features using the Left Side Bar")

# options_markdown = """
# You predict the permeability of compounds using compound names & smiles.
# """
# st.markdown(options_markdown)

# file uploader

data = pd.read_csv('./data/final/clean_trial4.csv')

compound_names = list(data['Compound'].unique())
compound = st.selectbox("Select Compound", compound_names)
st.write('The Compound you entered is: ', compound)
st.sidebar.markdown("# Compound")

def get_compound():
    # search the disease # removing three columns
    compound_df = data[data['Compound'] == compound].iloc[0, 3:].values
  
    compound_df = np.reshape(compound_df, (1, -1))

    predicted = predict_permeability(compound_df)

    st.success("Permeability:\n {}".format(predicted))
    

st.button("Predict Permeability", on_click=predict_permeability)
