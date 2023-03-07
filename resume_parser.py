import streamlit as st
from PyPDF2 import PdfReader
from streamlit_tags import st_tags
import pandas as pd
import base64
import spacy

#nlp=spacy.load('en_core_web_sm')
import en_core_web_sm
nlp = en_core_web_sm.load()
from spacy.matcher import Matcher
matcher = Matcher(nlp.vocab)
import pandas as pd
import re

from functions import pdf_to_text,extract_name,extract_email,extract_phone,extract_skills,extract_github,extract_linkedin,extract_country

hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}

       .st-b7 {
    color: white;
    font-size=10px;
}

       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)






st.title('Resume Parser APP V1')

uploaded_file = st.file_uploader("Upload your ' PDF ' RESUME", type="pdf")

with st.expander("WHAT IS THIS ?"):
    st.write('This is an intelligent Resume Parser (1st version) made by HELMI MASSOUSSI')


with st.expander("HOW IT IS WORK ?"):
    st.write('Just drag & drop the resume and wait for the extracted informations')

if uploaded_file:
    st.header('EXTRACTED INFORMATIONS: ')
    file = uploaded_file.name
    txt=pdf_to_text(file)
    name=extract_name(nlp(txt))
    email=extract_email(txt)
    phone=extract_phone(txt)
    skills=extract_skills(txt)
    github=extract_github(txt)
    linkedin=extract_linkedin(txt)
    country=extract_country(txt)
    st.success(f'NAME : {name}')
    st.success(f'EMAIL : {email}')
    st.success(f'PHONE : {phone}')
    st.success(f'GITHUB : {github}')
    st.success(f'LINKEDIN : {linkedin}')
    st.success(f'NATIONALITY : {country}')

    keywords = st_tags(
    label='# SKILLS:',
    value=skills,
    
    maxtags = -1,
    key='1')

    data=[(name,email,phone,github,linkedin,country)]
    df=pd.DataFrame(data,columns =['Name', 'Email', 'Phone','Github','Linkedin','country'])
        
    st.dataframe(df)
    download=df.to_csv().encode('utf-8')
    st.download_button(
    label=f'Download  {name} data as CSV',
    data=download,
    file_name=f'{name}.csv',
    mime='text/csv')

    

