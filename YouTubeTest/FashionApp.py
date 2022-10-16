import os
import json
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st

from pinata import pin_file_to_ipfs, pin_json_to_ipfs, convert_data_to_json

load_dotenv()

# Define and connect a new Web3 provider
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))

################################################################################
# Load_Contract Function
################################################################################


@st.cache(allow_output_mutation=True)
def load_contract():

    # Load the contract ABI  eg:'./contracts/compiled/fashion_abi.json'
    with open(Path(./py_file/contracts/compiled/fashion_abi.json)) as f: 
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

################################################################################
# Helper functions to pin files and json to Pinata
################################################################################


def pin_purchase(product_name, artwork_file):
    # Pin the file to IPFS with Pinata
    ipfs_file_hash = pin_file_to_ipfs(artwork_file.getvalue())

    # Build a token metadata file for the purchase token_json could be NFT_minted_json
    token_json = {
        "name": product_name,
        "image": ipfs_file_hash
    }
    json_data = convert_data_to_json(token_json)

    # Pin the json to IPFS with Pinata
    json_ipfs_hash = pin_json_to_ipfs(json_data)

    return json_ipfs_hash, token_json


# def pin_appraisal_report(report_content):
#     json_report = convert_data_to_json(report_content)
#     report_ipfs_hash = pin_json_to_ipfs(json_report)
#     return report_ipfs_hash


st.title("Designer Products")
st.write("Login and Select account to get started")
st.selectbox("Login")
st.selectbox("Password")
accounts = w3.eth.accounts
address = st.selectbox("Select Account", options=accounts)
st.markdown("---")

################################################################################
# Purchase item and register NFT
################################################################################
st.markdown("## Purchase item and collect NFT")
data = product_list  # choices of handbag, watch etc
product_type = st.text_input ("select Product type", options = data)
product_name = st.text_input("select Item", options = images)
#artist_name = st.text_input("Enter the artist name")
#initial_appraisal_value = st.text_input("Enter the initial appraisal amount")

# Use the Streamlit `file_uploader` function create the list of digital image file types(jpg, jpeg, or png) that will be uploaded to Pinata.
file = st.file_uploader("Upload Artwork", type=["jpg", "jpeg", "png"])   #??do we need this?? Can we have the pinned images as a list instead

if st.button("Confirm Purchase"):
    # Use the `pin_purchase` helper function to pin the file to IPFS
    artwork_ipfs_hash, token_json = pin_purchase(product_name, file)

    artwork_uri = f"ipfs://{artwork_ipfs_hash}"

    tx_hash = contract.functions.registerArtwork(
        address,
        product_name,
        # artist_name,  #not used but could be brand name
        # int(initial_appraisal_value), # not req
        artwork_uri,
        token_json['image']
    ).transact({'from': address, 'gas': 1000000})
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    st.write("Transaction receipt NFT minted:")
    st.write(dict(receipt))
    st.write("You can view the Receipt detail here.") 
    st.markdown(f"[Receipt Link](https://ipfs.io/ipfs/{artwork_ipfs_hash})")
    st.markdown(f"[NFT Image Link](https://ipfs.io/ipfs/{token_json['image']})")

st.markdown("---")


################################################################################
# Appraise Art  Can change & use part of this
################################################################################
# st.markdown("## Appraise Artwork")
# tokens = contract.functions.totalSupply().call()
# token_id = st.selectbox("Choose an Art Token ID", list(range(tokens)))
# new_appraisal_value = st.text_input("Enter the new appraisal amount")
# appraisal_report_content = st.text_area("Enter details for the Appraisal Report")

# if st.button("Appraise Artwork"):

#     # Make a call to the contract to get the image uri
#     image_uri = str(contract.functions.imageUri(token_id).call())
    
#     # Use Pinata to pin an appraisal report for the report content
#     appraisal_report_ipfs_hash =  pin_appraisal_report(appraisal_report_content+image_uri)

#     # Copy and save the URI to this report for later use as the smart contract’s `reportURI` parameter.
#     report_uri = f"ipfs://{appraisal_report_ipfs_hash}"

#     tx_hash = contract.functions.newAppraisal(
#         token_id,
#         int(new_appraisal_value),
#         report_uri,
#         image_uri

#     ).transact({"from": w3.eth.accounts[0]})
#     receipt = w3.eth.waitForTransactionReceipt(tx_hash)
#     st.write(receipt)
# st.markdown("---")

################################################################################
# Get Appraisals
################################################################################

# st.markdown("## Get the appraisal report history")
# art_token_id = st.number_input("Artwork ID", value=0, step=1)
# if st.button("Get Appraisal Reports"):
#     appraisal_filter = contract.events.Appraisal.createFilter(
#         fromBlock=0, argument_filters={"tokenId": art_token_id}
#     )
#     reports = appraisal_filter.get_all_entries()
#     if reports:
#         for report in reports:
#             report_dictionary = dict(report)
#             st.markdown("### Appraisal Report Event Log")
#             st.write(report_dictionary)
#             st.markdown("### Pinata IPFS Report URI")
#             report_uri = report_dictionary["args"]["reportURI"]
#             report_ipfs_hash = report_uri[7:]
#             image_uri = report_dictionary["args"]["artJson"]
#             st.markdown(
#                 f"The report is located at the following URI: "
#                 f"{report_uri}"
#             )
#             st.write("You can also view the report URI with the following ipfs gateway link")
#             st.markdown(f"[IPFS Gateway Link](https://ipfs.io/ipfs/{report_ipfs_hash})")
#             st.markdown("### Appraisal Event Details")
#             st.write(report_dictionary["args"])
#             st.image(f'https://ipfs.io/ipfs/{image_uri}')
#     else:
#         st.write("This artwork has no new appraisals")

        
       
