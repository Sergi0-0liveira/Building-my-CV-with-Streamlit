# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 12:13:17 2022

@author: SergioOliveira
"""

import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

#binder title
st.set_page_config(page_title = 'Sérgio Oliveira Projects', page_icon =':bar_chart:', layout='wide')


def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

data_pic = load_lottie('https://assets9.lottiefiles.com/packages/lf20_4syqy0rw.json')

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style/style.css")


# body

with st.container():
    data_col, lottie_col = st.columns(2)
    with data_col:
        st.subheader("Data Projects :office:")
        st.write("""
                - Supermarket Sales Analysis
                - WebScrapping Job Information
                - Credit Default - PowerBI Dashboard
                - StreamLit Project                
                 """)
    with lottie_col:
        st_lottie(data_pic, height=450, key='exp_lottie')
        
### -- contact me

with st.container():
    st.write("---")
    st.subheader("Contact Me!")
    
# using the code from formsubmit.co

    contactform ="""
    <form action="https://formsubmit.co/sergio.miguel.oliveira.87@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    
    contactcol, blankcol = st.columns(2)
    with contactcol:
        st.markdown(contactform, unsafe_allow_html = True)
    with blankcol:
        st.empty()