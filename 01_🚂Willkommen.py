import streamlit as st
import streamlit as st
import psycopg2
import psycopg2.extras
from sqlalchemy import create_engine, true
import pandas
import streamlit as st
import streamlit_multipage 
import requests
import streamlit as st
from bs4 import BeautifulSoup
import time
import pandas as pd
from time import sleep
import streamlit as st
import psycopg2
import psycopg2.extras
from sqlalchemy import create_engine
from bs4 import BeautifulSoup
import requests
import time 
from time import sleep
from matplotlib import dates as mpl_dates
from cProfile import label
from streamlit.cli import main  
from streamlit.proto.RootContainer_pb2 import RootContainer
import pandas 
import plotly.figure_factory as ff
import numpy as np
from streamlit_option_menu import option_menu 
import yagmail
from dbTable import *
from http.client import CONFLICT
from re import X
from telnetlib import DO
from typing import Collection
import smtplib, ssl
from http.client import CONFLICT
from pickle import TRUE
from re import X
from telnetlib import DO
from typing import Collection
from attr import s
import streamlit as st
import psycopg2
import psycopg2.extras
from sqlalchemy import create_engine
from bs4 import BeautifulSoup
import requests
import time 
from time import sleep
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import plotly.express as px 
import plotly
from matplotlib import dates as mpl_dates
from cProfile import label
from distutils.cmd import Command
import datetime 
from streamlit.cli import main  
from streamlit.proto.RootContainer_pb2 import RootContainer
import pandas 
import plotly.figure_factory as ff
import numpy as np
from streamlit_option_menu import option_menu 
import yagmail
from dbTable import *
from http.client import CONFLICT
from re import X
from telnetlib import DO
from typing import Collection
import smtplib, ssl
from http.client import CONFLICT
from re import X
from telnetlib import DO
from typing import Collection
import streamlit as st
import psycopg2
import psycopg2.extras
from sqlalchemy import create_engine
import pandas
from bs4 import BeautifulSoup
import requests
import time 
from time import sleep
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import plotly.express as px 
import plotly
from matplotlib import dates as mpl_dates
from cProfile import label
from distutils.cmd import Command
import datetime 
from streamlit.cli import main  
from streamlit.proto.RootContainer_pb2 import RootContainer
import pandas as pd 
import plotly.figure_factory as ff
import numpy as np
from streamlit_option_menu import option_menu 
import yagmail
from dbTable import *
from http.client import CONFLICT
from re import X
from telnetlib import DO
from typing import Collection
import smtplib, ssl


conn = psycopg2.connect(host ="dpg-cajo73sgqg428kba9ikg-a.frankfurt-postgres.render.com",
                        database="dbticket", 
                        user="dbticket_user", 
                        password="Nhaema5GzFDyW3j0sGHVYjfhRBu0fTvy")

engine = create_engine('postgresql://dbticket_user:Nhaema5GzFDyW3j0sGHVYjfhRBu0fTvy@dpg-cajo73sgqg428kba9ikg-a.frankfurt-postgres.render.com/dbticket')
global cursor 
cur = conn.cursor()

def app():
    st.set_page_config("DB-Price-App",page_icon="🚂",layout="wide")
    st.title("DB Price App")
    #st.info("Um diese App vollständig zu benutzen, müssen Sie sich auf der Willkommen-Seite eingeloggt haben.")
    #st.warning("Ansonsten werden Sie einige Funktionen nicht durchführen können.")
    #st.header("Anleitung")
    #image=Image.open("website.png")
    
    optionliste = ["",'Darmstadt Hbf',
      "Wiesbaden Hbf",
      "Hanau Hbf",
      "Frankenthal Hbf",
      "Kaiserslautern Hbf",
      "Pirmasens Hbf",
      "Speyer Hbf",
      "Zweibrücken Hbf",
      "Kassel Hbf",
      "Boppard Hbf",
      "Berlin Hbf",             
      "Koblenz Hbf",
      "Wittlich Hbf",
      "Mainz Hbf",
      "Worms Hbf",
      "Saarbrücken Hbf",
      "Saarlouis Hbf",
      "Trier Hbf",
      "Braunschweig Hbf",
      "Hildesheim Hbf",
      "Wolfsburg Hbf",
      "Bremen Hbf",
      "Bremerhaven Hbf",
      "Emden Hbf",
      "Osnabrück Hbf",
      "Hamburg Hbf",
      "Hannover Hbf",
      "Kiel Hbf",
      "Lübeck Hbf",
      "Cottbus Hbf",
      "Brandenburg Hbf",
      "Eberswalde Hbf",
      "Potsdam Hbf",
      "Neustrelitz Hbf",
      "Rostock Hbf",
      "Stralsund Hbf",
      "Schwerin Hbf",
      "Augsburg Hbf",
      "Lindau Hbf",
      "Bayreuth Hbf",
      "Hof Hbf",
      "München Hbf",
      "Nürnberg Hbf",
      "Deggendorf Hbf",
      "Passau Hbf",
      "Regensburg Hbf",
      "Berchtesgaden Hbf",
      "Ingolstadt Hbf",
      "Aschaffenburg Hbf",
      "Schweinfurt Hbf",
      "Würzburg Hbf",
      "Chemnitz Hbf",
      "Gera Hbf",
      "Dresden Hbf",
      "Arnstadt Hbf",
      "Erfurt Hbf",
      "Merseburg Hbf",
      "Döbeln Hbf",
      "Leipzig Hbf",
      "Bernburg Hbf",
      "Dessau Hbf",
      "Magdeburg Hbf",
      "Stendal Hbf",
      "Thale Hbf",
      "Wernigerode Hbf",
      "Lörrach Hbf",
      "Reutlingen Hbf",
      "Tübingen Hbf",
      "Freudenstadt Hbf",
      "Karlsruhe Hbf",
      "Pforzheim Hbf",
      "Bad Friedrichshall Hbf",
      "Heidelberg Hbf",
      "Heilbronn Hbf",
      "Mannheim Hbf",
      "Öhringen Hbf",
      "Stuttgart Hbf",
      "Aalen Hbf",
      "Ulm Hbf",
      "Bielefeld Hbf",
      "Gütersloh Hbf",
      "Paderborn Hbf",
      "Dortmund Hbf",
      "Lünen Hbf",
      "Bottrop Hbf",
      "Duisburg Hbf",
      "Krefeld Hbf",
      "Oberhausen Hbf",
      "Aachen Hbf",
      "Düsseldorf Hbf",
      "Eschweiler Hbf",
      "Gevelsberg Hbf",
      "Mönchengladbach Hbf",
      "Neuss Hbf",
      "Remscheid Hbf",
      "Rheydt Hbf",
      "Solingen Hbf",
      "Wuppertal Hbf",
      "Bochum Hbf",
      "Castrop-Rauxel Hbf",
      "Essen Hbf",
      "Gelsenkirchen Hbf",
      "Wanne-Eickel Hbf",
      "Witten Hbf",
      "Hagen Hbf",
      "Siegen Hbf",
      "Bonn Hbf",
      "Köln Hbf",
      "Recklinghausen Hbf"
      ]
      
    st.header("Anfragen")
    col1,col2,col3=st.columns(3)

    bahnkarteliste=["Nicht ausgewählt","25 in der 1.Klasse","25 in der 2.Klasse","50 in der 1.Klasse","50 in der 2.Klasse","Nein"]

    klassenliste=["Nicht ausgewählt","1","2"]
    optionliste.sort()

    with col1: 
            st.subheader("Bahnhof")
            option = st.selectbox('Startbahnhof auswählen', optionliste)
            st.write('Dein Startbahnhof:', option)
            zielbahn=st.selectbox("Zielbahnhof auswählen", optionliste)
            st.write("Dein Zielbahnhof:", zielbahn)
            
    with col2:
            st.subheader("Abfahrt")
            losdatum=st.date_input('Datum', value= pd.to_datetime("today"))
            st.write("Datum:", losdatum.strftime("%d.%m.%Y"))          
            uhrzeit_stunde1=st.number_input("Stunde: ", min_value=1,value=12,max_value=24,step=1)
            st.write("Stunde: ", uhrzeit_stunde1)
            uhrzeit_minuten1=st.number_input("Minute: ",min_value=00,max_value=59,step=1) 
            st.write("Minute: ", uhrzeit_minuten1)
    with col3:
            st.subheader("Alter & Bahnkarte")
            alter_1=st.number_input("Alter: ",min_value=1,value=18,max_value=110,step=1) 
            st.write("Alter: ", alter_1)
            bahnkarteneu=st.selectbox("Bahnkarte:", bahnkarteliste)
            st.write("Bahnkarte:", bahnkarteneu)
            klasse=st.selectbox("In welcher Klasse willst Du fahren:",klassenliste)
            st.write("Deine ausgewählte Klasse: ",klasse)

    submit_buttonhome = st.checkbox(label='Bestätigen')     
    if submit_buttonhome:
      if 'sub' not in st.session_state:
        st.session_state.sub= True
      start=option
      ziel=zielbahn
      datum=losdatum.strftime("%d.%m.%Y") 
      uhrzeit_stunde=str(uhrzeit_stunde1)
      uhrzeit_minuten=str(uhrzeit_minuten1)
      uhrzeit_minuten=str(uhrzeit_minuten1)
      if alter_1 in range(15,5,-1):
          alter="f"
      else: 
          if alter_1 in range(26,13,-1): 
              alter="y"
          else:
              if alter_1 in range(64,26,-1):
                  alter="e"
              else: 
                  alter="s" 
                  
      if bahnkarteneu=="25 in der 1.Klasse":
         bahnkarte="1"
      else: 
         if bahnkarteneu=="25 in der 2.Klasse":
            bahnkarte="2"
         else: 
            if bahnkarteneu=="50 in der 1.Klasse":
               bahnkarte="3"
            else :
              if bahnkarteneu=="50 in der 2.Klasse":
                 bahnkarte="4"
              else:
                bahnkarte="0"
            
      url='https://reiseauskunft.bahn.de/bin/query.exe/dn?revia=yes&existOptimizePrice-deactivated=1&country=DEU&dbkanal_007=L01_S01_D001_qf-bahn-svb-kl2_lz03&start=1&protocol=https%3A&REQ0JourneyStopsS0A=1&S='+start+'&REQ0JourneyStopsSID=A%3D1%40O%3DM%C3%BCnchen+Hbf%40X%3D11558339%40Y%3D48140229%40U%3D80%40L%3D008000261%40B%3D1%40p%3D1652295202%40&REQ0JourneyStopsZ0A=1&Z='+ziel+'&REQ0JourneyStopsZID=A%3D1%40O%3DAachen+Hbf%40X%3D6091495%40Y%3D50767803%40U%3D80%40L%3D008000001%40B%3D1%40p%3D1652295202%40&date=Fr%2C+'+datum+'&time='+uhrzeit_stunde+'%3A'+uhrzeit_minuten+'&timesel=depart&returnDate=&returnTime=&returnTimesel=depart&optimize=0&auskunft_travelers_number=1&tariffTravellerType.1='+alter+'&tariffTravellerReductionClass.1='+bahnkarte+'&tariffClass='+klasse+'&rtMode=DB-HYBRID&externRequest=yes&HWAI=JS%21js%3Dyes%21ajax%3Dyes%21&externRequest=yes&HWAI=JS%21js%3Dyes%21ajax%3Dyes%21#hfsseq1|gl.0263982.1652621988'
      source=requests.get(url)
      soup = BeautifulSoup(source.text,"html.parser")

      zugverbindungen=soup.find("div", class_= "overviewConnection")
      zugverbindungen1=zugverbindungen.find("div", class_="connectionRoute")
      station1=zugverbindungen1.find("div", class_="station first").get_text(strip=True)
      station2=zugverbindungen1.find("div", class_="station stationDest").get_text(strip=True)
      uhrzeit_zv1=zugverbindungen.find("div", class_= "connectionTimeSoll")
      zeiten_zv1=uhrzeit_zv1.find("div", class_= "time").get_text(strip=True)
      art_zug_zv1=soup.find("div", class_= "connectionData")
      art_zug_zv2=art_zug_zv1.find("div", class_= "connectionBar").get_text(strip=True)
      preis_zv1=zugverbindungen.find("div",class_="connectionAction").get_text(strip=True)
      sparpreis_zv2=preis_zv1.replace("€","")
      sparpreis_zv1=sparpreis_zv2.replace("Rückfahrt hinzufügen","")
      sparpreis_zv3=sparpreis_zv1.replace("\xa0","")
      sparpreis_zv=sparpreis_zv3.replace("ab","€")

      if "Verbindung liegt in der Vergangenheit" in sparpreis_zv1: 
          st.info("Diese Verbindung liegt in der Vergangenheit. Bitte wählen eine andere Verbindung.")

      else: 
          if "THA" in art_zug_zv2:

              st.write("Diese Zugverbindung wird nicht von uns unterstüzt. Bitte wähle eine Zugverbindung von der DB.")

          else: 
              if "VRS-Tarif" in sparpreis_zv1:

                  st.write("Hier ist kein Vergleich notwendig, da diese Verbindung zu VRS-Tarifen angeboten wird.")

              else: 
                  st.header("Wir haben folgende Verbindung gefunden:")
                  st.write("Abfahrt: ",station1)
                  st.write("Reiseziel: ",station2)
                  st.write("Fahrzeit: ",zeiten_zv1)
                  st.write("Preis: ",sparpreis_zv)
                  
                  with st.container():
                    st.info("Wenn Du Deine Anfrage speichern möchten, musst Du Dich bitte zuerst anmelden bzw. registrieren.")
                    with st.form("log1"):
                      option = st.selectbox(
                      'Wähle eine der folgenden Optionen:',
                      ("bitte auswählen",'Anmelden', 'Registrieren'))
                      sbest=st.form_submit_button("Auswählen")
                  coll1,coll2,coll3=st.columns(3)
                  if option=="Anmelden":
                    with coll1:
       
                      with st.form("log"):
                          loginn=st.text_input("Benutzername: ")
                          loginp=st.text_input("Passwort: ",type="password")
                          inhalt=st.text_input("Gib Deiner Anfrage einen Namen:")
                          wunsch=inhalt.lower()
                          st.write("Deine Anfrage wurde wie folgt gespeichert: " + wunsch)
                
                          tabe=''.join(wunsch)
                          best=st.form_submit_button("Anfrage speichern")
                      def Login(loginn,loginp): 
                          cur.execute("SELECT login.username FROM login WHERE username=%s", [loginn])
                          if not cur.fetchone():  # An empty result evaluates to False.
                               st.info("Kein Benutzer mit diesem Benutzernamen")
                          else:
                              cur.execute("""SELECT login.passwort FROM login WHERE passwort=%s""", [loginp])
                              if not cur.fetchone():  # An empty result evaluates to False.
                                  st.warning("Falsches Passwort")
                              else:
                                  st.success("Du hast Dich erfolgreich angemeldet")
                                  result=pandas.DataFrame(columns=["username","tabelle"])
                                  result.loc[len(result)]=[loginn,wunsch]
                                  result.to_sql(name="anfragen", con=engine, if_exists="append")
                                  result=result[0:0]
                                  def mehrereanfragen(loginn,wunsch):
                                    
                                    tababfrage=cur.execute("Select anfragen.tabelle From anfragen where username=%s and tabelle=%s",[loginn,wunsch])
                                    st.info(tababfrage)
                                    if cur.fetchone():
                                      while true:
                                        url='https://reiseauskunft.bahn.de/bin/query.exe/dn?revia=yes&existOptimizePrice-deactivated=1&country=DEU&dbkanal_007=L01_S01_D001_qf-bahn-svb-kl2_lz03&start=1&protocol=https%3A&REQ0JourneyStopsS0A=1&S='+start+'&REQ0JourneyStopsSID=A%3D1%40O%3DM%C3%BCnchen+Hbf%40X%3D11558339%40Y%3D48140229%40U%3D80%40L%3D008000261%40B%3D1%40p%3D1652295202%40&REQ0JourneyStopsZ0A=1&Z='+ziel+'&REQ0JourneyStopsZID=A%3D1%40O%3DAachen+Hbf%40X%3D6091495%40Y%3D50767803%40U%3D80%40L%3D008000001%40B%3D1%40p%3D1652295202%40&date=Fr%2C+'+datum+'&time='+uhrzeit_stunde+'%3A'+uhrzeit_minuten+'&timesel=depart&returnDate=&returnTime=&returnTimesel=depart&optimize=0&auskunft_travelers_number=1&tariffTravellerType.1='+alter+'&tariffTravellerReductionClass.1='+bahnkarte+'&tariffClass='+klasse+'&rtMode=DB-HYBRID&externRequest=yes&HWAI=JS%21js%3Dyes%21ajax%3Dyes%21&externRequest=yes&HWAI=JS%21js%3Dyes%21ajax%3Dyes%21#hfsseq1|gl.0263982.1652621988'
                                        source=requests.get(url)
                                        soup = BeautifulSoup(source.text,"html.parser")
                                        zugverbindungen=soup.find("div", class_= "overviewConnection")
                                        zugverbindungen1=zugverbindungen.find("div", class_="connectionRoute")
                                        station1=zugverbindungen1.find("div", class_="station first").get_text(strip=True)
                                        station2=zugverbindungen1.find("div", class_="station stationDest").get_text(strip=True)
                                        uhrzeit_zv1=zugverbindungen.find("div", class_= "connectionTimeSoll")
                                        zeiten_zv1=uhrzeit_zv1.find("div", class_= "time").get_text(strip=True)
                                        art_zug_zv1=soup.find("div", class_= "connectionData")
                                        art_zug_zv2=art_zug_zv1.find("div", class_= "connectionBar").get_text(strip=True)
                                        preis_zv1=zugverbindungen.find("div",class_="connectionAction").get_text(strip=True)
                                        sparpreis_zv2=preis_zv1.replace("ab","")
                                        sparpreis_zv1=sparpreis_zv2.replace("Rückfahrt hinzufügen","")
                                        sparpreis_zv=sparpreis_zv1.replace("€","")
                                        sparpreis_ohne_punkt=sparpreis_zv.replace(",",".")
                                        preis_float=float(sparpreis_ohne_punkt)
                                        if "Verbindung liegt in der Vergangenheit" in sparpreis_zv1: 
                                            st.info("Diese Verbindung liegt in der Vergangenheit. Wählen Sie eine andere Verbindung")
                                            break

                                        else: 
                                            if "THA" in art_zug_zv2:
                      
                                              st.info("Diese Zugverbindung wird nicht von uns unterstüzt. Bitte wählen Sie eine Verbindung der Züge von der DB.")
                                              break

                                            else: 
                                               if "VRS-Tarif" in sparpreis_zv1:
                            
                                                 st.info("Hier ist kein Vergleich notwendig, da diese Verbindung zu VRS-Tarifen angeboten wird.")
                                                 break 
                          
                                               else:
                                
                                                   anfrage_tage=time.strftime("%d.%m")
                                                   anfrage_zeit=time.strftime("%H:%M")
                                                   anfrage_komplett=time.strftime("%d.%m. %H:%M")
                                                   wunschpreis1="0"
                                                   result=pandas.DataFrame(columns=["anfrage_tag","anfrage_uhrzeit","anfrage_komplett","startbahnhof", "zielbahnhof","fahrzeit","preis","wunschpreis"])
                                                   result.loc[len(result)]=[anfrage_tage,anfrage_zeit, anfrage_komplett,station1,station2,zeiten_zv1,preis_float,wunschpreis1]
                                                   result.to_sql(name=tabe, con=engine, if_exists="append" )
                                                   result=result[0:0]
                                                   st.success("Du hast diese Anfrage erfolgreich gestellt")
                                                   port = 587  # For starttls
                                                   smtp_server = "smtp.gmail.com"
                                                   yag = yagmail.SMTP("dbpriceapp123@gmail.com","jxdovcbbxcdkmgxl")
                                                   contents = [
                                                            "Hallo :)"
                                                            "\n" 
                                                            "Good News!! Der Preis Deiner favoritisierten Verbindung ist auf Deinen Wunschpreis gefallen!"
                                                            "\n"
                                                            "Kaufe Dir also am besten direkt ein Ticket auf der Seite der DeutschenBahn."
                                                            "Hier gehts zur Webseite: https://www.bahn.de "
                                                            "\n"
                                                            "\n"
                                                            "Freundliche Grüße und eine gute Fahrt!"
                                                            "\n"
                                                            "Dein Team von"
                                                            "DB-Price-App"]

                                                   preisauswahl=cur.execute(f"SELECT preis FROM {wunsch} where preis <= {wunschpreis1}",conn)
                                                   if cur.fetchall():
                                                    yag.send(to=loginn,
                                                    subject='Wunschpreis',
                                                    contents=contents)
           
                                               sleep(18)
                                      else:
                                        st.warning("Der Name dieser Anfrage existiert bereits. Bitte wähle einen Anderen.")
                                  mehrereanfragen(loginn,wunsch)

                              if 'name' not in st.session_state:
                                    st.session_state.name =loginn
                              if 'passw' not in st.session_state:
                                    st.session_state.passw=loginp

                    if best:
                      Login(loginn,loginp)
                      if 'willen' not in st.session_state:
                        st.session_state.willen= True
                          
                  if option=="Registrieren":
                      with st.form(key='form201'):
                       eingabe=st.text_input("Benutzername:")
                       passw1=st.text_input("Passwort:",type="password")
                       register = st.form_submit_button(label="Registrieren")
                      def add_userdata(eingabe,passw1):
                              anf=cur.execute("Select login.username From login where username=%s",[eingabe])
                              if not cur.fetchone():
                                  result=pandas.DataFrame(columns=["username","passwort"])
                                  result.loc[len(result)]=[eingabe,passw1]
                                  result.to_sql(name="login", con=engine, if_exists="append")
                                  result=result[0:0]
                                  st.info("Du hast Dich erfolgreich registriert")
                                  st.success("Du kannst dich nun anmelden, wähl dazu oben die Option Anmelden aus")
                              else:
                                  st.warning("Der Benutzername existiert bereits. Melde Dich bitte an.")
                      if register:   
                          add_userdata(eingabe,passw1)
                    
       

    
app()
