# Import Libraries
import streamlit as st
from PIL import Image
from pathlib import Path
from streamlit_image_comparison import image_comparison
import streamlit.components.v1 as components
import os
import json
from web3 import Web3
from dotenv import load_dotenv
import base64

# Set Page Configuration
st.set_page_config(layout="wide", initial_sidebar_state='collapsed')

# background
# image_file = Image.open('../project3/Resources/Images/background2.png')
# def add_bg_from_local(image_file):
#     with open(image_file, "rb") as image_file:
#         encoded_string = base64.b64encode(image_file.read())
#     st.markdown(
#     f"""
#     <style>
#     .stApp {{
#         background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
#         background-size: cover
#     }}
#     </style>
#     """,
#     unsafe_allow_html=True
#     )
# add_bg_from_local('../project3/Resources/Images/background2.png')

# Header and Title Screen
image = Image.open('../project3/Resources/Images/LOGOHEADER.PNG')
col1, col2, col3 = st.columns([1,5,1])
with col1:
    st.write("")

with col2:
    st.image(image, width = 1000)

with col3:
    st.write("")
    
st.title("ALL YOUR FAVOURITE BRANDS, IN-PERSON & ON THE BLOCKCHAIN")
st.markdown("# Choose an account to get started:")
accounts = w3.eth.accounts
address = st.selectbox("Select Account", options=accounts)
st.markdown("---")  
# st.markdown("<h1 style='text-align: center; color: white;'>ALL YOUR FAVOURITE BRANDS, IN-PERSON & ON THE BLOCKCHAIN:</h1>", unsafe_allow_html=True)