import streamlit as st
import pandas as pd
from data import show_data


#judul dashboard
def judul ():
    st.title("📊 Dashboard  Covid-19")
    st.write("Selamat datang di dashboard Covid-19 disini anda dapat melihat data pribadi anda")


st.sidebar.title("Navigasi")
menu = st.sidebar.radio("Pilih Halaman", ["Home", "Halaman data"])
if menu == "Home":
    judul()
elif menu == "Halaman data":
    judul()
    show_data()







    