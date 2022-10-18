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
label1="Glasses",
label2="NFT ownership"
)



st.write('Glasses_Black_Gold [link](https://gateway.pinata.cloud/ipfs/QmfWTNA1B2y85rUTGLrUgNRpeBWmUDHHXke7hA2oiwL11U)')
# https://gateway.pinata.cloud/ipfs/QmRoVwMejmuq1M4mk62meVNotYdjtiWGZVCVftmySZj5GT (Glasses_Black_Ray.png)
# https://gateway.pinata.cloud/ipfs/QmQjL3b2PBFmo3xqgnQWm59vEBVz2GQruH1oYxkHZwaFz2 (Glasses_Dark_Rad.png)
# https://gateway.pinata.cloud/ipfs/QmXiji3BDzPs27D7v2GTr3hhnk7ZYbpoBKR3fLownZyFVi (Glasses_DG_Chain.png)
# https://gateway.pinata.cloud/ipfs/QmZZLq93Emf3WPPKukAJVNPUgwUbjDxNAAHF2J813iBxZ9 (Glasses_Pearl_Chain.png)
# https://gateway.pinata.cloud/ipfs/Qmd9TMYggGcgBrDDSWmthWCJWT38pxmYUoeUfLEphewnvP (Glasses_Pink.png)
# https://gateway.pinata.cloud/ipfs/QmdT38NtaXTPAHa4jtdoHLnFNLdxDx1q6nXwLXMmSYj8kM (Glasses_Rose_Chain.png)