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
label1="Jackets",
label2="NFT ownership"
)

st.write('Jacket_Biker [link](https://gateway.pinata.cloud/ipfs/QmR43LPfW4aweLSGk5yjJh3Wsk7dUq18TNeNyxX1tySeVF)')
# https://gateway.pinata.cloud/ipfs/QmQceZmv7vwfRntB8r2b8cp7o5jaPUH94f1ZEFMqWgGvbS (Jacket_Blazer.png)
# https://gateway.pinata.cloud/ipfs/QmcYvSX2AMkMUGYLBNqpWyE13QN8KxqXGw4n2NoMU1rSow (Jacket_Bomber.png)
# https://gateway.pinata.cloud/ipfs/QmTFVcRVKWn6jGZkJ7zZmn3FYFvfZAcJSiCn5foDtq5rxt (Jacket_Field.png)
# https://gateway.pinata.cloud/ipfs/QmQ4WvDMvb7SLcbw6WRmFZcB2SMZ93Lac4DQPyPA7XvwVd (Jacket_Cafe_Racer.png)