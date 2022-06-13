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
st.set_page_config(page_title = 'Sérgio Oliveira experience', page_icon =':office:', layout='wide')

# load assets

def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

exp_pic = load_lottie('https://assets2.lottiefiles.com/packages/lf20_zzasoagh.json')

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style/style.css")

# body

with st.container():
    exp_col, lottie_col = st.columns(2)
    with exp_col:
        st.subheader("Experience :office:")
        st.write("""
                 - [2021 - NOW] - bolttech - Senior People Business Partner
                 - [2018 - 2020] - blip.pt - People Business Partner
                 - [2017 - 2018] - Eberspaecher - HR Business Partner
                 - [2016 - 2017] - NewCoffee - HR Manager
                 - [2013 - 2016] - DF Elastomer Solutions - HR Generalist
                 - [2009 - 2012] - University Internships & Working throughout studying in University                 
                 """)
    with lottie_col:
        st_lottie(exp_pic, height=450, key='exp_lottie')
        
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