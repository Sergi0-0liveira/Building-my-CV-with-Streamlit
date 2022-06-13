# -*- coding: utf-8 -*-
"""
Created on Mon May 30 17:14:11 2022

@author: SergioOliveira
"""
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


#emojis ->https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title = 'Sérgio Oliveira Online CV', page_icon =':briefcase:', layout='wide')


## defining a request to get the json file (lottie_pic)

def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

## -- load assesst

lottie_pic = load_lottie('https://assets9.lottiefiles.com/packages/lf20_chcyxcbj.json')
education_pic = Image.open('Images/learning.png')
experience_pic = Image.open('Images/experience.png')
projects_pic = Image.open('Images/projects.png')

# -- Use local CSS file

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style/style.css")
    

## --- Header Section---
with st.container():
    presentation_col, socialmedia_col = st.columns([2,1])
    
    with presentation_col:
        st.subheader('Hi! :wave: I am Sérgio!')
        st.title(" People Science and Analytics Professional")
        st.write("""I am from Portugal and I've always wanted to be 'ahead of the game' and by that I mean I've always wanted to anticipate and predict future problems. 
                 So in the early stages of my career I started to pay more attention to data to understand problems and maybe pick up trends and I LOVED IT. 
                 From there to learning pyhton was a small step.'
                 Today I am very passionate about using Python, SQL and my People skills into making data driven decision.
                 And above all I love learning and be challenged""")
        
    
    with socialmedia_col:
        st.subheader("Checkout my Social Media!")
        st.write(':point_right: [Linked In Profile](linkedin.com/in/sérgio-oliveira-01132418)')
        st.write(':point_right: [Git Hub Profile](https://github.com/Sergi0-0liveira)')
###--- What I do -----

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader('# What I do?')
        st.write('##')
        st.write("""
                
                 As a HR professional What I do is ensure that my stakeholders make the best decisions possible having in
                 the priorities for the year. I am responsible for:
                    - Understanding people challenges.
                    - Bringing people expertise and developing solutions to help the business area to deliver its strategy
                    - Influencing and building relationships with people around the business
                    - Acting as a POC of people expertise for specialist teams that are implementing new people approaches
                    - Questioning and challenging others to get to the root of people and business issues
                    - Coaching and providing feedback to key stakeholders to help improve business efficiency.
                    - Ensure Data consistency throughout my business units
                    - Develop Python Scripts to ensure proper and relevant data collection to address people challenges
                    - Develop people dashboard to track people Kpi's
            
                 """)
    with right_column:
        st_lottie(lottie_pic, height=450, key='coding')
        
###--- Select what you want to see---

with st. container():
    st.write("---")
    choice = st.selectbox('What do you Want to see?', ['Select one option', 'Education', 'Experience', 'Data Projects', 'Summary of all'], key='0')
    if "Select one option" in choice:
            st.empty()
    elif "Education" in choice:
            st.subheader("Education :mortar_board:")
            st.image(education_pic, width = 300)
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
    elif "Experience" in choice:
            st.subheader("Experience :office:")
            st.image(experience_pic, width = 300)
            st.write("""
                 - [2021 - NOW] - bolttech - Senior People Business Partner
                 - [2018 - 2020] - blip.pt - People Business Partner
                 - [2017 - 2018] - Eberspaecher - HR Business Partner
                 - [2016 - 2017] - NewCoffee - HR Manager
                 - [2013 - 2016] - DF Elastomer Solutions - HR Generalist
                 - [2009 - 2012] - University Internships & Working throughout studying in University                 
                 """)
    elif "Data Projects" in choice:
            st.subheader('Data Projects :bar_chart:')
            st.image(projects_pic, width = 300)
            st.write("""
                 - Supermarket Sales Analysis
                 - WebScrapping Job Information
                 - Credit Default - PowerBI Dashboard
                 
                 """)
    elif "Summary of all" in choice:
            with st.container():
                st.write("---")
                education_col, experience_col, data_projects_col = st.columns(3)
                with education_col:
                    st.subheader("Education :mortar_board:")
                    st.image(education_pic, width = 300)
                    st.write("""
                             - [2021 - 2022] - Python 4 everybody Program - Coursera
                             - [2021 - 2022] - Google Data Analytics Professional Certificate - Google/Coursera
                             - [2021 - 2022] - PostgreSQL 4 Everybody Program - Coursera
                             - [2022] - Webscrapping with R - DataCamp
                             - [2021] - Python for Data Science - Sololearn
                             - [2021] - Python for beginners - Sololearn
                             - [2019] - Inovating with Data - Dot Native
                             - [2019] - Storytelling with Data - Dot Native
                             - [2019] - Shane Snow on Storytelling - LinkedIn Learning
                             - [2009 - 2012] - Human Resources - University Degree - IPP
                             - [2003 - 2006] - Accounting and HR Specilization - High School Specialization - IEFP
                             """)
                with experience_col:
                    st.subheader("Experience :office:")
                    st.image(experience_pic, width = 300)
                    st.write("""
                             - [2021 - NOW] - bolttech - Senior People Business Partner
                             - [2018 - 2020] - blip.pt - People Business Partner
                             - [2017 - 2018] - Eberspaecher - HR Business Partner
                             - [2016 - 2017] - NewCoffee - HR Manager
                             - [2013 - 2016] - DF Elastomer Solutions - HR Generalist
                             - [2009 - 2012] - University Internships & Working throughout studying in University                 
                             """)
                    
                with data_projects_col:
                    st.subheader('Data Projects :bar_chart:')
                    st.image(projects_pic, width = 300)
                    st.write("""
                             - Supermarket Sales Analysis
                             - WebScrapping Job Information
                             - Credit Default - PowerBI Dashboard
                             - StreamLit Project
                             """)
    else:
        st.empty()
                            
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
















