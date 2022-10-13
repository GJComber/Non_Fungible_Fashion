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

load_dotenv()

# Define and connect a new Web3 provider
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))

# Set Page Configuration
st.set_page_config(layout="wide", initial_sidebar_state='collapsed')

# Header and Title Screen
image = Image.open('../Resources/Images/LOGOHEADER.PNG')
col1, col2, col3 = st.columns([1,5,1])
with col1:
    st.write("")

with col2:
    st.image(image, width = 1000)

with col3:
    st.write("")
    
# st.markdown("<h1 style='text-align: center; color: white;'>ALL YOUR FAVOURITE BRANDS, IN-PERSON & ON THE BLOCKCHAIN:</h1>", unsafe_allow_html=True)

@st.cache(allow_output_mutation=True)
def load_contract():

    # Load the contract ABI
    with open(Path('../contracts/compiled/fashion_abi.json')) as f:
        fashion_abi = json.load(f)

    # Set the contract address (this is the address of the deployed contract)
    contract_address = os.getenv("SMART_CONTRACT_ADDRESS")

    # Get the contract
    contract = w3.eth.contract(
        address=contract_address,
        abi=fashion_abi
    )

    return contract

# Load the contract
contract = load_contract()

st.title("ALL YOUR FAVOURITE BRANDS, IN-PERSON & ON THE BLOCKCHAIN")
st.markdown("# Choose an account to get started:")
accounts = w3.eth.accounts
address = st.selectbox("Select Account", options=accounts)
artwork_uri = st.text_input("Select item Owner", options=accounts)
if st.button("Register your digital asset"):
    tx_hash = contract.functions.registerArtwork(address, artwork_uri).transact({'from': address, 'gas': 1000000})
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    st.write("Transaction receipt mined:")
    st.write(dict(receipt))
st.markdown("---")  

























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
