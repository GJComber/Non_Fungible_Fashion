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
label1="Handbags",
label2="NFT ownership"
)
st.write('Bag_Azure [link](https://gateway.pinata.cloud/ipfs/QmUdBhaMekmpg9oQ3bb8zryuDdEAGsu3Q9WVSMibqnkHff)')
# https://gateway.pinata.cloud/ipfs/QmQeNbJGVNjR8Yx9fJnCHszdRwyYNH6Vxtdr7YMMBjVxv6 (Bag_Pink.png)
# https://gateway.pinata.cloud/ipfs/QmRAoXPfAftGdc9734ZCAYmk9n9VA972SXGuBaRCC2smio (Bag_Maroon.png)
# https://gateway.pinata.cloud/ipfs/QmWnU6xGBhjYnm2nQB154vyjqMRyFe6Tgtgrg5cdKxDxLz (Bag_Leather.png)
# https://gateway.pinata.cloud/ipfs/QmeDQySaM3qhHdwJFd7crdLQ3o1jG4urUcSNMigiY1E9g1 (Bag_Grey.png)
# https://gateway.pinata.cloud/ipfs/QmUhgfWwwp1Ztzt3pG5vMT4Zu4g1yEyTf25eotwVydkXPc (Bag_Blue.png)
# https://gateway.pinata.cloud/ipfs/QmU4kG4QNsqWf7YWTaVUt2fqw1TsYU7Duiyy5qM2DU9Hcv (Bag_Beige.png)
# https://gateway.pinata.cloud/ipfs/QmbnakQtcyJfDdfMG89KQTVZkkbAY8KSRN5PB8Bdut5ZjL (Bag_White.png)