import streamlit as st
import pickle
import pandas as pd
import numpy as np


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

model_filename = "./models/LGBMRegressor_model.sav"
model = pickle.load(open(model_filename, 'rb'))


scaler_filename = pickle.load(open('./models/scaler.pkl', 'rb'))


title = st.text_input('Enter your Compound in Smiles Structure', placeholder="C(=O)(N)N")
st.write('The Smile you entered is: ', title)

st.sidebar.markdown("# Smiles")

# def predict_permeability():
#     # search the disease # removing three columns
#     compound_df = data[data['Compound'] == compound].iloc[0, 3:].values
  
#     compound_df = np.reshape(compound_df, (1, -1))
#     scaled = scaler_filename.transform(compound_df)
    
#     predicted = model.predict(scaled)[0]
#     predicted = round(predicted, 2)


#     st.success("Permeability:\n {}".format(predicted))
    

# st.button("Predict Permeability", on_click=predict_permeability)
