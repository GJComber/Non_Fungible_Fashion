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
from pinata import pin_file_to_ipfs, convert_data_to_json, pin_json_to_ipfs

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
# @st.cache(allow_output_mutation=True)
# def load_contract():

#     # Load the contract ABI
#     with open(Path('../contracts/compiled/fashion_abi.json')) as f:
#         fashion_abi = json.load(f)

#     # Set the contract address (this is the address of the deployed contract)
#     contract_address = os.getenv("SMART_CONTRACT_ADDRESS")

#     # Get the contract
#     contract = w3.eth.contract(
#         address=contract_address,
#         abi=fashion_abi
#     )

#     return contract

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

# Account connection in UI
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
brand = choice  # do ineed this?



st.write(choice, "uses this wallet to pay into")
st.write(vendor)
selection = ()
img_list = []
buyer = "0x3129C700695F3408dE351dBD96d3B995909dF298"

st.write("### Exclusive selections from the ",brand, "designer range" )


url = "https://gateway.pinata.cloud/ipfs/"
Prada_img_captions = ["Prada_Glasses_Dark_Rad", "Shoe_Rad_Black","Bag_Grey","Bag_Blue", "Bag_Beige","Shoe_Shiny_Choo","Shoe_Chelsea"]
Prada_img_list = [   
    "https://gateway.pinata.cloud/ipfs/QmQjL3b2PBFmo3xqgnQWm59vEBVz2GQruH1oYxkHZwaFz2", 
    "https://gateway.pinata.cloud/ipfs/QmVimMJRoQoP2jFgUQkuHEkdieNKSuGmvASvijjLJdXhtS",    
    "https://gateway.pinata.cloud/ipfs/QmeDQySaM3qhHdwJFd7crdLQ3o1jG4urUcSNMigiY1E9g1",
    "https://gateway.pinata.cloud/ipfs/QmUhgfWwwp1Ztzt3pG5vMT4Zu4g1yEyTf25eotwVydkXPc",
    "https://gateway.pinata.cloud/ipfs/QmU4kG4QNsqWf7YWTaVUt2fqw1TsYU7Duiyy5qM2DU9Hcv",      
    "https://gateway.pinata.cloud/ipfs/QmYSTuZUmGhBiKk1iZjnTrD6y6YJ9HC8Gy79djUaQEmLtQ",
    "https://gateway.pinata.cloud/ipfs/QmWt7XRzoyByexqdRuUi8PwjQz7fMSWBrhRNcFZVVHhhrJ"
]

Prada_Display_list = [
    "./Resources/Images/Prada Images/Bag_Beige.png",
    "./Resources/Images/Prada Images/Bag_Blue.png",
    "./Resources/Images/Prada Images/Bag_Grey.png",
    "./Resources/Images/Prada Images/Glasses_Dark_Rad.png",
    "./Resources/Images/Prada Images/Shoe_Chelsea.png",
    "./Resources/Images/Prada Images/Shoe_Rad_Black.png",
    "./Resources/Images/Prada Images/Shoe_Shiny_Choo.png"
]

Prada_gateway_dict = {
    "Glasses_Dark_Rad":"https://gateway.pinata.cloud/ipfs/QmQjL3b2PBFmo3xqgnQWm59vEBVz2GQruH1oYxkHZwaFz2",
    "Shoe_Rad_Black":"https://gateway.pinata.cloud/ipfs/QmVimMJRoQoP2jFgUQkuHEkdieNKSuGmvASvijjLJdXhtS",
    "Bag_Grey":"https://gateway.pinata.cloud/ipfs/QmeDQySaM3qhHdwJFd7crdLQ3o1jG4urUcSNMigiY1E9g1",
    "Bag_Blue":"https://gateway.pinata.cloud/ipfs/QmUhgfWwwp1Ztzt3pG5vMT4Zu4g1yEyTf25eotwVydkXPc",
    "Bag_Beige":"https://gateway.pinata.cloud/ipfs/QmU4kG4QNsqWf7YWTaVUt2fqw1TsYU7Duiyy5qM2DU9Hcv",      
    "Shoe_Shiny_Choo":"https://gateway.pinata.cloud/ipfs/QmYSTuZUmGhBiKk1iZjnTrD6y6YJ9HC8Gy79djUaQEmLtQ" ,
    "Shoe_Chelsea":"https://gateway.pinata.cloud/ipfs/QmWt7XRzoyByexqdRuUi8PwjQz7fMSWBrhRNcFZVVHhhrJ"
            
}




Prada = {
    "Glasses_Dark_Rad":"QmQjL3b2PBFmo3xqgnQWm59vEBVz2GQruH1oYxkHZwaFz2",
    "Shoe_Rad_Black":"QmVimMJRoQoP2jFgUQkuHEkdieNKSuGmvASvijjLJdXhtS",
    "Bag_Grey":"QmeDQySaM3qhHdwJFd7crdLQ3o1jG4urUcSNMigiY1E9g1",
    "Bag_Blue":"QmUhgfWwwp1Ztzt3pG5vMT4Zu4g1yEyTf25eotwVydkXPc",
    "Bag_Beige":"QmU4kG4QNsqWf7YWTaVUt2fqw1TsYU7Duiyy5qM2DU9Hcv",      
    "Shoe_Shiny_Choo":"QmYSTuZUmGhBiKk1iZjnTrD6y6YJ9HC8Gy79djUaQEmLtQ" ,
    "Shoe_Chelsea":"QmWt7XRzoyByexqdRuUi8PwjQz7fMSWBrhRNcFZVVHhhrJ"
        
}


DandG = {
    "Bag_White":"QmbnakQtcyJfDdfMG89KQTVZkkbAY8KSRN5PB8Bdut5ZjL",
    "Bag_Leather":"QmWnU6xGBhjYnm2nQB154vyjqMRyFe6Tgtgrg5cdKxDxLz",
    "Bag_Maroon":"QmRAoXPfAftGdc9734ZCAYmk9n9VA972SXGuBaRCC2smio",
    "Glasses_Black_Gold":"QmfWTNA1B2y85rUTGLrUgNRpeBWmUDHHXke7hA2oiwL11U",
    "Glasses_Pink":"Qmd9TMYggGcgBrDDSWmthWCJWT38pxmYUoeUfLEphewnvP",
    "Glasses_DG_Chain":"QmXiji3BDzPs27D7v2GTr3hhnk7ZYbpoBKR3fLownZyFVi",
    "Shoe_Sneakers":"QmVx2BT6k3Ko8wwpQ8ipXMqX1WN6eiDoSG7YtB1B5izVoQ"
 
} 

DandG_Display_list = [
    "./Resources/Images/DandG Images/Bag_Leather.png",
    "./Resources/Images/DandG Images/Bag_Maroon.png",
    "./Resources/Images/DandG Images/Bag_White.png",
    "./Resources/Images/DandG Images/Glasses_Black_Gold.png",
    "./Resources/Images/DandG Images/Glasses_DG_Chain.png",
    "./Resources/Images/DandG Images/Glasses_Pink.png",
    "./Resources/Images/DandG Images/Shoe_Sneakers.png"   
]
 
Harrods = {
    "Jacket_Biker":"QmR43LPfW4aweLSGk5yjJh3Wsk7dUq18TNeNyxX1tySeVF",
    "Jacket_Blazer":"QmQceZmv7vwfRntB8r2b8cp7o5jaPUH94f1ZEFMqWgGvbS",
    "Jacket_Bomber":"QmcYvSX2AMkMUGYLBNqpWyE13QN8KxqXGw4n2NoMU1rSow",
    "Jacket_Field":"QmTFVcRVKWn6jGZkJ7zZmn3FYFvfZAcJSiCn5foDtq5rxt",
    "Jacket_Cafe_Racer":"QmQ4WvDMvb7SLcbw6WRmFZcB2SMZ93Lac4DQPyPA7XvwVd", 
    "Glasses_Black_Ray":"QmRoVwMejmuq1M4mk62meVNotYdjtiWGZVCVftmySZj5GT"
}

Harrods_Display_list =[
    "./Resources/Images/Harrods Images/Glasses_Black_Ray.png",
    "./Resources/Images/Harrods Images/Jacket_Biker.png",
    "./Resources/Images/Harrods Images/Jacket_Blazer.png",
    "./Resources/Images/Harrods Images/Jacket_Bomber.png",
    "./Resources/Images/Harrods Images/Jacket_Cafe_Racer.png",
    "./Resources/Images/Harrods Images/Jacket_Field.png"
]   
   
Gucci = {
      
    "Shoe_Gucci_Sneaker":"QmfKiWeQgSu2qGgiQaUhaXYMUhfJVGkDydXWn9cE8k1Rps",
    "Shoe_Hightop":"QmWGMTcMMSF8bebcz6ZC2oAHYB175g8w6turjEh9EBUe2a",
    "Shoe_CL_Red":"QmX8dLLwBkBfzuWxC62aHrdWzTvVRLgeFAUcDeHa49UJ3Z",
    "Bag_Azure":"QmUdBhaMekmpg9oQ3bb8zryuDdEAGsu3Q9WVSMibqnkHff", 
    "Bag_Pink":"QmQeNbJGVNjR8Yx9fJnCHszdRwyYNH6Vxtdr7YMMBjVxv6",
    "Glasses_Pearl_Chain":"QmZZLq93Emf3WPPKukAJVNPUgwUbjDxNAAHF2J813iBxZ9",
    "Glasses_Rose_Chain":"QmdT38NtaXTPAHa4jtdoHLnFNLdxDx1q6nXwLXMmSYj8kM"
        
}


Gucci_Display_list = [
    "./Resources/Images/Gucci Images/Bag_Azure.png",
    "./Resources/Images/Gucci Images/Bag_Pink.png",
    "./Resources/Images/Gucci Images/Glasses_Pearl_Chain.png",
    "./Resources/Images/Gucci Images/Glasses_Rose_Chain.png",
    "./Resources/Images/Gucci Images/Shoe_CL_Red.png",
    "./Resources/Images/Gucci Images/Shoe_Gucci_Sneaker.png",
    "./Resources/Images/Gucci Images/Shoe_Hightop.png"
]


WatchSwiss = {
    "Watches_Rolex":"QmfKbjghewk34YU6yNTArchX6Lm25iz5WQ9qJRxrSodyzD",
    "Watches_Omega":"QmaMdqhJ73CaQ6EGr9jBhVGvhq6NnnLkTVGCth9gCmenA8",
    "Watches_Patek_Philippe":"QmRJhf6kFvMSzEA5TcgUM4GjLBig4ddEWKxeNt2pSG8F6E",
    "Watches_Tagheuer":"QmWxFetLjU3vAT43U9RwxkN7utr3PUmTzMhCQUNQcmx22H",
    "Watches_Vacheron_Constantin":"QmbqgGWo1CVVGD7k87CuHc54V1WWP6UyaTKSWWdz7hjr2T"
}
WatchSwiss_Display_list = [
    "./Resources/Images/WatchSwiss Images/Watches_Omega.png",
    "./Resources/Images/WatchSwiss Images/Watches_Patek_Philippe.png",
    "./Resources/Images/WatchSwiss Images/Watches_Rolex.png",
    "./Resources/Images/WatchSwiss Images/Watches_Tagheuer.png",
    "./Resources/Images/WatchSwiss Images/Watches_Vacheron_Constantin.png"   
]

items = {
"Prada" : 
    ["../Resources/Images/Prada Images/Bag_Beige.png",
    "../Resources/Images/Prada Images/Bag_Blue.png",
    "../Resources/Images/Prada Images/Bag_Grey.png",
    "../Resources/Images/Prada Images/Glasses_Dark_Rad.png",
    "../Resources/Images/Prada Images/Shoe_Chelsea.png",
    "../Resources/Images/Prada Images/Shoe_Rad_Black.png",
    "../Resources/Images/Prada Images/Shoe_Shiny_Choo.png"],
"DandG" :
    ["../Resources/Images/DandG Images/Bag_Leather.png",
    "../Resources/Images/DandG Images/Bag_Maroon.png",
    "../Resources/Images/DandG Images/Bag_White.png",
    "../Resources/Images/DandG Images/Glasses_Black_Gold.png",
    "../Resources/Images/DandG Images/Glasses_DG_Chain.png",
    "../Resources/Images/DandG Images/Glasses_Pink.png",
    "../Resources/Images/DandG Images/Shoe_Sneakers.png"],
"Harrods" :
    ["../Resources/Images/Harrods Images/Glasses_Black_Ray.png",
    "../Resources/Images/Harrods Images/Jacket_Biker.png",
    "../Resources/Images/Harrods Images/Jacket_Blazer.png",
    "../Resources/Images/Harrods Images/Jacket_Bomber.png",
    "../Resources/Images/Harrods Images/Jacket_Cafe_Racer.png",
    "../Resources/Images/Harrods Images/Jacket_Field.png"],
"Gucci" :
    ["../Resources/Images/Gucci Images/Bag_Azure.png",
    "../Resources/Images/Gucci Images/Bag_Pink.png",
    "../Resources/Images/Gucci Images/Glasses_Pearl_Chain.png",
    "../Resources/Images/Gucci Images/Glasses_Rose_Chain.png",
    "../Resources/Images/Gucci Images/Shoe_CL_Red.png",
    "../Resources/Images/Gucci Images/Shoe_Gucci_Sneaker.png",
    "../Resources/Images/Gucci Images/Shoe_Hightop.png"],
"WatchSwiss" :
    ["../Resources/Images/WatchSwiss Images/Watches_Omega.png",
    "../Resources/Images/WatchSwiss Images/Watches_Patek_Philippe.png",
    "../Resources/Images/WatchSwiss Images/Watches_Rolex.png",
    "../Resources/Images/WatchSwiss Images/Watches_Tagheuer.png",
    "../Resources/Images/WatchSwiss Images/Watches_Vacheron_Constantin.png"]   
}
address = w3.eth.accounts[0]
buyer = Web3.toChecksumAddress(address)

for i in items[choice]:
    st.image(i)
    if st.button(label="Buy now", key = {i}):
        ipfs_hash = pin_file_to_ipfs(i)
        item_uri = f"ipfs://{ipfs_hash}"
        token_json = {
            "name": choice,
            "image": item_uri
        }
        json_data = convert_data_to_json(token_json)

    # Pin the json to IPFS with Pinata
        json_ipfs_hash = pin_json_to_ipfs(json_data)

        tx_hash = contract.functions.awardCertificate(
        buyer,
        json_ipfs_hash
        ).transact({'from': buyer, 'gas': 1000000})
        receipt = w3.eth.waitForTransactionReceipt(tx_hash)
        st.write("Transaction receipt mined:")
        st.write(dict(receipt))
    st.markdown("---")


# products = { 
#     "Prada": Prada_Display_list,
#     "DandG" : DandG_Display_list,
#     "Gucci" : Gucci_Display_list,
#     "WatchSwiss" : WatchSwiss_Display_list,
#     "Harrods" : Harrods_Display_list
# }

# page = st.radio("Select to Purchase", options=products)
# st.image(products)

# if img_list= 'Prada':
#     st.image(
#     "./Resources/Images/Prada Images/Bag_Beige.png",
#     "./Resources/Images/Prada Images/Bag_Blue.png",
#     "./Resources/Images/Prada Images/Bag_Grey.png",
#     "./Resources/Images/Prada Images/Glasses_Dark_Rad.png",
#     "./Resources/Images/Prada Images/Shoe_Chelsea.png",
#     "./Resources/Images/Prada Images/Shoe_Rad_Black.png",
#     "./Resources/Images/Prada Images/Shoe_Shiny_Choo.png")
# elif img_list = "DandG":
#     st.image["./Resources/Images/DandG Images/Bag_Leather.png",
#     "./Resources/Images/DandG Images/Bag_Maroon.png",
#     "./Resources/Images/DandG Images/Bag_White.png",
#     "./Resources/Images/DandG Images/Glasses_Black_Gold.png",
#     "./Resources/Images/DandG Images/Glasses_DG_Chain.png",
#     "./Resources/Images/DandG Images/Glasses_Pink.png",
#     "./Resources/Images/DandG Images/Shoe_Sneakers.png" ]
# elif img_list  = "Harrods":
#     st.image["./Resources/Images/Harrods Images/Glasses_Black_Ray.png",
#     "./Resources/Images/Harrods Images/Jacket_Biker.png",
#     "./Resources/Images/Harrods Images/Jacket_Blazer.png",
#     "./Resources/Images/Harrods Images/Jacket_Bomber.png",
#     "./Resources/Images/Harrods Images/Jacket_Cafe_Racer.png",
#     "./Resources/Images/Harrods Images/Jacket_Field.png"] 
# elif img_list = "Gucci":
#     st.image[ "./Resources/Images/Gucci Images/Bag_Azure.png",
#     "./Resources/Images/Gucci Images/Bag_Pink.png",
#     "./Resources/Images/Gucci Images/Glasses_Pearl_Chain.png",
#     "./Resources/Images/Gucci Images/Glasses_Rose_Chain.png",
#     "./Resources/Images/Gucci Images/Shoe_CL_Red.png",
#     "./Resources/Images/Gucci Images/Shoe_Gucci_Sneaker.png",
#     "./Resources/Images/Gucci Images/Shoe_Hightop.png"]
# else img_list = "WatchSwiss":
#     st.image[ "./Resources/Images/WatchSwiss Images/Watches_Omega.png",
#     "./Resources/Images/WatchSwiss Images/Watches_Patek_Philippe.png",
#     "./Resources/Images/WatchSwiss Images/Watches_Rolex.png",
#     "./Resources/Images/WatchSwiss Images/Watches_Tagheuer.png",
#     "./Resources/Images/WatchSwiss Images/Watches_Vacheron_Constantin.png" ]

# for i in img_list:
#     st.image(img_list[i])
#     if st.button(label = "click here to buy now"):
#         selection=image(img_list[i])
      
#st.image(img_list,width = 50)



items = () 
# Brands  = {Prada,DandG,Harrods,Gucci,Tiffanys}

# for brand in Brands:
#     img_dict = img_dict[Brands]

# items = {
#     "Nike" : ["../Resources/Images/wallet.png",
#                 "../Resources/Images/shoes.png"],
#     "Hi": [],
#     "here": [] 
# }
#Brand  = {Prada,DandG,Harrods,Gucci,Tiffanys}
# img_dict = { chosen choice
#     "img1": "Qlshdblabdl",
#     "img2": "sjdhbljda"

#     for i in img_dict.keys():
#     url + img_dict[i]
# uri = url + img_dict['img1']
# {data1, "shoes",
# data2, "pther"}
# }

 ##Image_Dicts for each Brand which is [choice]

# selection = []

# for m in img_dict.keys():
#     url + img_dict[m]
# #uri = url + img_dict.values()
# st.image(m)
# if st.button(label = f"{m} buy now"):
#         selection == image(m)

# for i in Prada :
#     uri = url + Prada.values(i)    


# st.form("select item", options = items[choice])
# submitted = st.form_submit_button("Submit")
# if submitted:
#         st.session_state.items = items
#         item_list = [items]
#         st.image(item_list, width=400)
#         st.write("end")





# artwork_uri = st.text_input("Select item Owner", options=accounts)
# if st.button("Register your digital asset"):
#     tx_hash = contract.functions.registerArtwork(choice, artwork_uri).transact({'from': choice, 'gas': 1000000})
#     receipt = w3.eth.waitForTransactionReceipt(tx_hash)
#     st.write("Transaction receipt mined:")
#     st.write(dict(receipt))
# st.markdown("---")

# # Using "with" notation
# with st.sidebar:
#     st.image('../Resources/Images/LOGOHEADER.PNG')

# # Image database saved harddrive

# # --------






# if st.form('Check out this!'):
#     user_choice = st.button
#     st.image(user_choice)
# if "visibility" not in st.session_state:
#     st.session_state.visibility = "visible"
#     st.session_state.disabled = False

# st.write('Access catalogue')
# with st.form("option choice", clear_on_submit=False):
#     catalogue_choice = st.selectbox(label='here options', 
#     options= image)
#     # Every form must have a submit button.
#     submitted = st.form_submit_button("Submit")
#     if submitted:
#         st.session_state.catalogue_choice = catalogue_choice
#         item_list = [catalogue_choice]
#         st.image(item_list, width=400)
#         st.write("end")