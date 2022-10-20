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
    "Prada": "0xA3D3A0c7D7Ed93Bbd087bBB69577857aC52ca8Ec",
    "DandG" : "0x0e67bed69550a19589E481e0AF911b9939405136",
    "Gucci" : "0x576e2eE34Ad4E1A9842446f7ca12e7CFA47B6d7D",
    "Tifannys" : " ",
    "Harrods" : " "
    
}

st.markdown("# Choose an account to get started:")
accounts = account_opt_dict.keys()
# st.write(accounts)
choice = st.selectbox("Select Brand:", options=accounts)
vendor = account_opt_dict[choice]
st.write(vendor)
st.write(choice)

buyer = "0x3129C700695F3408dE351dBD96d3B995909dF298"


Prada = {
    "Glasses_Dark_Rad":"https://gateway.pinata.cloud/ipfs/QmQjL3b2PBFmo3xqgnQWm59vEBVz2GQruH1oYxkHZwaFz2",
    "Shoe_Rad_Black":"https://gateway.pinata.cloud/ipfs/QmVimMJRoQoP2jFgUQkuHEkdieNKSuGmvASvijjLJdXhtS",
    "Bag_Grey":"https://gateway.pinata.cloud/ipfs/QmeDQySaM3qhHdwJFd7crdLQ3o1jG4urUcSNMigiY1E9g1",
    "Bag_Blue":"https://gateway.pinata.cloud/ipfs/QmUhgfWwwp1Ztzt3pG5vMT4Zu4g1yEyTf25eotwVydkXPc",
    "Bag_Beige":"https://gateway.pinata.cloud/ipfs/QmU4kG4QNsqWf7YWTaVUt2fqw1TsYU7Duiyy5qM2DU9Hcv",      
    "Shoe_Shiny_Choo":"https://gateway.pinata.cloud/ipfs/QmYSTuZUmGhBiKk1iZjnTrD6y6YJ9HC8Gy79djUaQEmLtQ" ,
    "Shoe_Chelsea":"https://gateway.pinata.cloud/ipfs/QmWt7XRzoyByexqdRuUi8PwjQz7fMSWBrhRNcFZVVHhhrJ"
        
},


DandG = {
    "Bag_White":"https://gateway.pinata.cloud/ipfs/QmbnakQtcyJfDdfMG89KQTVZkkbAY8KSRN5PB8Bdut5ZjL",
    "Bag_Leather":"https://gateway.pinata.cloud/ipfs/QmWnU6xGBhjYnm2nQB154vyjqMRyFe6Tgtgrg5cdKxDxLz",
    "Bag_Maroon":"https://gateway.pinata.cloud/ipfs/QmRAoXPfAftGdc9734ZCAYmk9n9VA972SXGuBaRCC2smio",
    "Glasses_Black_Gold":"https://gateway.pinata.cloud/ipfs/QmfWTNA1B2y85rUTGLrUgNRpeBWmUDHHXke7hA2oiwL11U",
    "Glasses_Pink":"https://gateway.pinata.cloud/ipfs/Qmd9TMYggGcgBrDDSWmthWCJWT38pxmYUoeUfLEphewnvP",
    "Glasses_DG_Chain":"https://gateway.pinata.cloud/ipfs/QmXiji3BDzPs27D7v2GTr3hhnk7ZYbpoBKR3fLownZyFVi",
    "Shoe_Sneakers":"https://gateway.pinata.cloud/ipfs/QmVx2BT6k3Ko8wwpQ8ipXMqX1WN6eiDoSG7YtB1B5izVoQ"
 
},      
 
Harrods = {
    "Jacket_Biker":"https://gateway.pinata.cloud/ipfs/QmR43LPfW4aweLSGk5yjJh3Wsk7dUq18TNeNyxX1tySeVF",
    "Jacket_Blazer":"https://gateway.pinata.cloud/ipfs/QmQceZmv7vwfRntB8r2b8cp7o5jaPUH94f1ZEFMqWgGvbS",
    "Jacket_Bomber":"https://gateway.pinata.cloud/ipfs/QmcYvSX2AMkMUGYLBNqpWyE13QN8KxqXGw4n2NoMU1rSow",
    "Jacket_Field":"https://gateway.pinata.cloud/ipfs/QmTFVcRVKWn6jGZkJ7zZmn3FYFvfZAcJSiCn5foDtq5rxt",
    "Jacket_Cafe_Racer":"https://gateway.pinata.cloud/ipfs/QmQ4WvDMvb7SLcbw6WRmFZcB2SMZ93Lac4DQPyPA7XvwVd", 
    "Glasses_Black_Ray":"https://gateway.pinata.cloud/ipfs/QmRoVwMejmuq1M4mk62meVNotYdjtiWGZVCVftmySZj5GT"
},
        
Gucci = {
      
    "Shoe_Gucci_Sneaker":"https://gateway.pinata.cloud/ipfs/QmfKiWeQgSu2qGgiQaUhaXYMUhfJVGkDydXWn9cE8k1Rps",
    "Shoe_Hightop":"https://gateway.pinata.cloud/ipfs/QmWGMTcMMSF8bebcz6ZC2oAHYB175g8w6turjEh9EBUe2a",
    "Shoe_CL_Red":"https://gateway.pinata.cloud/ipfs/QmX8dLLwBkBfzuWxC62aHrdWzTvVRLgeFAUcDeHa49UJ3Z",
    "Bag_Azure":"https://gateway.pinata.cloud/ipfs/QmUdBhaMekmpg9oQ3bb8zryuDdEAGsu3Q9WVSMibqnkHff", 
    "Bag_Pink":"https://gateway.pinata.cloud/ipfs/QmQeNbJGVNjR8Yx9fJnCHszdRwyYNH6Vxtdr7YMMBjVxv6",
    "Glasses_Pearl_Chain":"https://gateway.pinata.cloud/ipfs/QmZZLq93Emf3WPPKukAJVNPUgwUbjDxNAAHF2J813iBxZ9",
    "Glasses_Rose_Chain":"https://gateway.pinata.cloud/ipfs/QmdT38NtaXTPAHa4jtdoHLnFNLdxDx1q6nXwLXMmSYj8kM"
        
},

Tiffanys = {
    "Watches_Rolex":"https://gateway.pinata.cloud/ipfs/QmfKbjghewk34YU6yNTArchX6Lm25iz5WQ9qJRxrSodyzD",
    "Watches_Omega":"https://gateway.pinata.cloud/ipfs/QmaMdqhJ73CaQ6EGr9jBhVGvhq6NnnLkTVGCth9gCmenA8",
    "Watches_Patek_Philippe":"https://gateway.pinata.cloud/ipfs/QmRJhf6kFvMSzEA5TcgUM4GjLBig4ddEWKxeNt2pSG8F6E",
    "Watches_Tagheuer":"https://gateway.pinata.cloud/ipfs/QmWxFetLjU3vAT43U9RwxkN7utr3PUmTzMhCQUNQcmx22H",
    "Watches_Vacheron_Constantin":"https://gateway.pinata.cloud/ipfs/QmbqgGWo1CVVGD7k87CuHc54V1WWP6UyaTKSWWdz7hjr2T"
}
    

# items = {
#     "Nike" : ["../Resources/Images/wallet.png",
#                 "../Resources/Images/shoes.png"],
#     "Hi": [],
#     "here": [] 
# }
items  = {Prada,DandG,Harrods,Gucci,Tiffanys}



for i in items[choice]:
    st.image(i)
    if st.button(label = f"{i} buy now"):
# session_state.
# st.write(user_buying)

    
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
    #   st.write("end")
