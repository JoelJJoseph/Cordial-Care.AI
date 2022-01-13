import streamlit as st
from multiapp import MultiApp


import base64
from PIL import Image
import gloww, alz, chest, lung, skin

from PIL import Image, ImageOps
import numpy as np
app = MultiApp()

new_title = '<p style="font-family:sans-serif; color:Black; font-size: 52px;"><b>Cordial Care.AI</b></p>'
st.markdown(new_title, unsafe_allow_html=True)


# Add all your application here
app.add_app("Refug Assist.AI", gloww.app)
app.add_app("Alzhemiers ", alz.app)
app.add_app("Chest cancer", chest.app)
app.add_app("Lung cancer", lung.app)
app.add_app("Skin cancer", skin.app)
# The main app
app.run()
