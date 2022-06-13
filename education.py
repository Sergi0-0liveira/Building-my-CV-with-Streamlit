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
st.set_page_config(page_title = 'Sérgio Oliveira education', page_icon =':mortar_board:', layout='wide')

# load assets

def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

edu_pic = load_lottie('https://assets3.lottiefiles.com/packages/lf20_4je7jquf.json')

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style/style.css")

# body

with st.container():
    text_col, lottie_col = st.columns(2)
    with text_col:
        st.subheader("Education :mortar_board:")
        st.write("""
                - [2021 - 2022] - Python 4 everybody Program - University of Michigan (Coursera)
                - [2021 - 2022] - Google Data Analytics Professional Certificate - Google (Coursera)
                - [2021 - 2022] - PostgreSQL 4 Everybody Program - University of Michigan (Coursera)
                - [2022] - Webscrapping with R - DataCamp
                - [2021] - Python for Data Science - Sololearn
                - [2021] - Python for beginners - Sololearn
                - [2019] - Inovating with Data - Dot Native
                - [2019] - Storytelling with Data - Dot Native
                - [2019] - Shane Snow on Storytelling - LinkedIn Learning
                - [2009 - 2012] - Human Resources - University Degree - IPP
                - [2003 - 2006] - Accounting and HR Specilization - High School Specialization - IEFP
                """)
    with lottie_col:
        st_lottie(edu_pic, height=450, key='edu_lottie')
        
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