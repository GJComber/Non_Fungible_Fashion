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
label1="Shoes",
label2="NFT ownership"
)

st.write('Shoe_Shiny_Choo [link] (https://gateway.pinata.cloud/ipfs/QmYSTuZUmGhBiKk1iZjnTrD6y6YJ9HC8Gy79djUaQEmLtQ)')
# https://gateway.pinata.cloud/ipfs/QmWt7XRzoyByexqdRuUi8PwjQz7fMSWBrhRNcFZVVHhhrJ (Shoe_Chelsea.png)
# https://gateway.pinata.cloud/ipfs/QmX8dLLwBkBfzuWxC62aHrdWzTvVRLgeFAUcDeHa49UJ3Z (Shoe_CL_Red.png)
# https://gateway.pinata.cloud/ipfs/QmfKiWeQgSu2qGgiQaUhaXYMUhfJVGkDydXWn9cE8k1Rps (Shoe_Gucci_Sneaker.png)
# https://gateway.pinata.cloud/ipfs/QmWGMTcMMSF8bebcz6ZC2oAHYB175g8w6turjEh9EBUe2a (Shoe_Hightop.png)
# https://gateway.pinata.cloud/ipfs/QmVimMJRoQoP2jFgUQkuHEkdieNKSuGmvASvijjLJdXhtS (Shoe_Rad_Black.png)
# https://gateway.pinata.cloud/ipfs/QmVx2BT6k3Ko8wwpQ8ipXMqX1WN6eiDoSG7YtB1B5izVoQ (Shoe_Sneakers.png)