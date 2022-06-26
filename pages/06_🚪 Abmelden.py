import streamlit as st
import psycopg2
import psycopg2.extras
from sqlalchemy import create_engine
import pandas
from PIL import Image
import streamlit as st
import streamlit_multipage
from streamlit_multipage.multipage import MultiPage
import streamlit as st
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
def load_lottieurl2(url: str):
  f = requests.get(url)
  if f.status_code != 200:
     return None
  return f.json()
  lottie_url_hello2 = "https://assets9.lottiefiles.com/packages/lf20_z4zn0d1v.json"
 #"https://assets3.lottiefiles.com/packages/lf20_E3exCx.json"
  
  
    
def app():
    st.write("Möchten Sie sich wirklich ausloggen?")
    with st.form("button"):
        ja=st.form_submit_button(label="Ja")
        nein=st.form_submit_button(label="Nein")
        
    if ja:
        del name2
        st.success("Sie haben sich erfolgreich ausgeloggt")
        
    if nein:
        st.info("Nicht abgemeldet")
    lottie_url_hello2 = "https://assets9.lottiefiles.com/packages/lf20_z4zn0d1v.json"
    lottie_hello2 = load_lottieurl2(lottie_url_hello2)
    st_lottie(lottie_hello2, key="hello") 
app()


load_lottieurl2("https://assets9.lottiefiles.com/packages/lf20_z4zn0d1v.json")
 
#def load_lottieurl2(url: str):
 #   f = requests.get(url)
  #  if f.status_code != 200:
   #     return None
    #return f.json()
   #lottie_url_hello2 = "https://assets4.lottiefiles.com/packages/lf20_7mibdcvp.json"
 #"https://assets3.lottiefiles.com/packages/lf20_E3exCx.json"
    #lottie_hello2 = load_lottieurl2(lottie_url_hello2)
    #st_lottie(lottie_hello2, key="hello") 
#load_lottieurl2("https://assets4.lottiefiles.com/packages/lf20_7mibdcvp.json")  
