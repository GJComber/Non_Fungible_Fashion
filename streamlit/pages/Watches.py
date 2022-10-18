import streamlit as st
from PIL import Image
from pathlib import Path
from streamlit_image_comparison import image_comparison
import streamlit.components.v1 as components


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
img1="../Resources/Images/DesignerPages.png",     # image changed
img2="../Resources/Images/NFT_Page.jpg",  # image changed
label1="Watches",
label2="NFT ownership"
)

st.write('Watches_Rolex[link](https://gateway.pinata.cloud/ipfs/QmfKbjghewk34YU6yNTArchX6Lm25iz5WQ9qJRxrSodyzD)')
# https://gateway.pinata.cloud/ipfs/QmaMdqhJ73CaQ6EGr9jBhVGvhq6NnnLkTVGCth9gCmenA8 (Watches_Omega.png)
# https://gateway.pinata.cloud/ipfs/QmRJhf6kFvMSzEA5TcgUM4GjLBig4ddEWKxeNt2pSG8F6E (Watches_Patek_Philippe.png)
# https://gateway.pinata.cloud/ipfs/QmWxFetLjU3vAT43U9RwxkN7utr3PUmTzMhCQUNQcmx22H (Watches_Tagheuer.png)
# https://gateway.pinata.cloud/ipfs/QmbqgGWo1CVVGD7k87CuHc54V1WWP6UyaTKSWWdz7hjr2T (Wathes_Vacheron_Constantin.png)