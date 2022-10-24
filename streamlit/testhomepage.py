# Import Libraries
import io
from secrets import choice
import streamlit as st
from PIL import Image
from pathlib import Path
from streamlit_image_comparison import image_comparison
import streamlit.components.v1 as components
import os
import io
import json
from web3 import Web3
from dotenv import load_dotenv
import base64
from pinata import pin_file_to_ipfs, convert_data_to_json, pin_json_to_ipfs

load_dotenv()

# load in images and MetaData from json
with open('all_data.json') as all_data:
   json.load('all_data.json')



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

# Setup for visualisations with image slider     
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



# Load the contract
@st.cache(allow_output_mutation=True)
def load_contract():

    # Load the contract ABI
    with open(Path('../contracts/compiled/certificate_abi.json')) as f:
        contract_abi = json.load(f)

    # Set the contract address (this is the address of the deployed contract)
    contract_address = Web3.toChecksumAddress(os.getenv("SMART_CONTRACT_ADDRESS"))


    # Get the contract
    contract = w3.eth.contract(
        address=contract_address,
        abi=contract_abi
    )

    return contract

# Load the contract
contract = load_contract()

# Account connections in UI
# Vendors accounts and vendorlist for selection
account_opt_dict = { 
    "Prada": "0xA3D3A0c7D7Ed93Bbd087bBB69577857aC52ca8Ec",
    "DandG" : "0x0e67bed69550a19589E481e0AF911b9939405136",
    "Gucci" : "0x576e2eE34Ad4E1A9842446f7ca12e7CFA47B6d7D",
    "WatchSwiss" : " 0x7fa3d65D65ec94BED3eaEEf0019c9b84E0e63d9A ",
    "Harrods" : " 0xD9E0727CBD11023837d3d812Fc42E0154dC9FDa6 "
    
}



if 'brand' not in st.session_state:
    st.session_state.brand = ''

st.markdown("# Choose an account to get started:")
accounts = account_opt_dict.keys()
# st.write(accounts)
choice = st.selectbox("Select Brand:", options=accounts)


vendor = account_opt_dict[choice]
brand = choice  

all_data.choice



st.write(choice, "uses this wallet to pay into")
st.write(vendor)
selection = ()
img_list = []
# Customers account (as would be selected during Login process)
buyer = "0x3129C700695F3408dE351dBD96d3B995909dF298"

st.write("### Exclusive selections from the ",brand, "designer range" )


url = "https://gateway.pinata.cloud/ipfs/"




# sharing addresses with Web3 for transacting
address = w3.eth.accounts[0]
buyer = Web3.toChecksumAddress(address)

# for i in all_data.choice:
#     i.name
# Displaying products with a BuyNow button to activate transaction and NFT creation for selected product
#for i in items[choice]:
for i in all_data.choice:    
    st.image(i.image)
    if st.button(label="Buy now", key = {i}):
        ipfs_hash = pin_file_to_ipfs(i)
        item_uri = f"ipfs://{ipfs_hash}"
        token_json = {
            "name": i.name,
            "image": item_uri,
            "description": i.description
        }
        json_data = convert_data_to_json(token_json)

    # Pin the json to IPFS with Pinata
        json_ipfs_hash = pin_json_to_ipfs(json_data)

        tx_hash = contract.functions.awardCertificate(
        buyer,
        json_ipfs_hash
        ).transact({'from': buyer, 'gas': 1000000})
        receipt = w3.eth.waitForTransactionReceipt(tx_hash)
        st.write("Transaction Complete. Your product is being despatched Express Delivery:") 
        st.write(' <---- see  NFT Receipt Details')
        st.sidebar.write('## NFT and Transaction receipt mined')
        #st.sidebar.write(dict(receipt))
        st.write(item_uri)
        st.sidebar.image(i)
        
    st.markdown("---")

    # st.session_state.the_image = Image.open(io.BytesIO(st.session_state.artifact.binary)) st.session_state.img_byte_arr = io.BytesIO(st.session_state.artifact.binary)







