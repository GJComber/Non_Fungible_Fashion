# Import Libraries
from secrets import choice
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
st.set_page_config(layout="centered", initial_sidebar_state='collapsed')

# Header and Title Screen
image = Image.open('../Resources/Images/LOGOHEADER.PNG')
col1, col2, col3 = st.columns([1,6,1])

with col1:
    st.write("")

with col2:
    st.image('../Resources/Images/LOGOHEADER.PNG')

with col3:
    st.write("")

# Setup for visualisations        
image_comparison(
img1="../Resources/Images/shoes.png",
img2="../Resources/Images/wallet.png",
label1="real fashion",
label2="digital assets"
)

st.markdown(
    """
    <h2 style='text-align: center'>
    ALL YOUR FAVOURITE BRANDS, IN-PERSON & ON THE BLOCKCHAIN
    </h2>
    """,
    unsafe_allow_html=True,
)

# Contract connectivity
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

# Account connection in UI
account_opt_dict = {
    "Nike": "0xA3D3A0c7D7Ed93Bbd087bBB69577857aC52ca8Ec",
    "Hi" : "0x0e67bed69550a19589E481e0AF911b9939405136",
    "here" : "0x576e2eE34Ad4E1A9842446f7ca12e7CFA47B6d7D"
    
}

st.markdown("# Choose an account to get started:")
accounts = account_opt_dict.keys()
# st.write(accounts)
choice = st.selectbox("Select Vendor:", options=accounts)
vendor = account_opt_dict[choice]
st.write(vendor)
st.write(choice)

buyer = "0x3129C700695F3408dE351dBD96d3B995909dF298"

items = {
    "Nike" : ["../Resources/Images/wallet.png",
                "../Resources/Images/shoes.png"],
    "Hi": [],
    "here": []
}

for i in items[choice]:
    st.image(i)
    if st.button(label = f"{i} buy now"):
        session_state.
    st.write(user_buying)

    
    # st.button(label='buy now')

# st.form("select item", options = items[choice])
# submitted = st.form_submit_button("Submit")
# if submitted:
#         st.session_state.items = items
#         item_list = [items]
#         st.image(item_list, width=400)
#         st.write("end")





# artwork_uri = st.text_input("Select item Owner", options=accounts)
# if st.button("Register your digital asset"):
#     tx_hash = contract.functions.registerArtwork(address, artwork_uri).transact({'from': address, 'gas': 1000000})
#     receipt = w3.eth.waitForTransactionReceipt(tx_hash)
#     st.write("Transaction receipt mined:")
#     st.write(dict(receipt))
# st.markdown("---")

# # Using "with" notation
# with st.sidebar:
#     st.image('../Resources/Images/LOGOHEADER.PNG')

# Image database saved harddrive

# --------
# url = "htts://www.google.com/Qlshdblabdl"
# img_dict = {
#     "img1": "Qlshdblabdl",
#     "img2": "sjdhbljda"
# }



# for i in img_dict.keys():
#     url + img_dict[i]
# uri = url + img_dict['img1']
# {data1, "shoes",
# data2, "pther"
# }
# if st.form('Check out this!'):
#     user_choice = st.button
#     st.image(user_choice)
# if "visibility" not in st.session_state:
#     st.session_state.visibility = "visible"
#     st.session_state.disabled = False

# st.write('Access catalogue')
# with st.form("option choice", clear_on_submit=False):
#     catalogue_choice = st.selectbox(label='here options', 
#     options= dataset)
#     # Every form must have a submit button.
#     submitted = st.form_submit_button("Submit")
#     if submitted:
#         st.session_state.catalogue_choice = catalogue_choice
#         item_list = [catalogue_choice]
#         st.image(item_list, width=400)
#         st.write("end")





















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
