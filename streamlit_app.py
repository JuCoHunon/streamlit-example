
import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="RainsBerry - Météo",
    page_icon="👋",
    layout="wide", 
)

from PIL import Image
image = Image.open('images/RainsBerry.jpg')

st.image(image, caption='RainsBerry')


st.markdown(
    """
    ### Promotion : DataScientist – Octobre 2021
    - Lionel Bottan
    - Julien Coquard
    - Samuel Guérin
    
    Streamlit is an open-source app framework built specifically for
    Machine Learning and Data Science projects.
    **👈 Select a demo from the sidebar** to see some examples
    of what Streamlit can do!
    ### Want to learn more?
    - Check out [streamlit.io](https://streamlit.io)
    - Jump into our [documentation](https://docs.streamlit.io)
    - Ask a question in our [community
        forums](https://discuss.streamlit.io)
    ### See more complex demos
    - Use a neural net to [analyze the Udacity Self-driving Car Image
        Dataset](https://github.com/streamlit/demo-self-driving)
    - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
    """
)




