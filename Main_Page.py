import streamlit as st
import pickle
import pandas as pd
import numpy as np
from PIL import Image

st.set_page_config(
    page_title="Skin Permeability",
    page_icon="👋",
)
# setting the title of our app
st.title("Skin Permeability")


st.markdown("### Welcome to the Website! 👋")
st.markdown("Use AI and Machine Learning to predict the permeability of your compound.")

image = Image.open('./images/skin_permeablity.png')

st.image(image,  width=400)

st.sidebar.markdown("# Choose Smiles or Compound")
st.markdown("### Explore our Features using the Left Side Bar")

options_markdown = """
- You predict the permeability of compounds using compound names & smiles.
- On the left side bar, select either the smiles structure or compound name.
"""
st.markdown(options_markdown)
# see desaisiv dashboard and improve

