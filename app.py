import streamlit as st
import pandas as pd
from data import show_data, kolom, select_year, load_data, filter_data, pie_chart1, select_location


#judul dashboard
def judul ():
    st.title("📊 Dashboard  Covid-19")
    st.write("Selamat datang di dashboard Covid-19 disini anda dapat melihat data pribadi anda")


st.sidebar.title("Navigasi")
menu = st.sidebar.radio("Pilih Halaman", ["Home", "Halaman data"])

if menu == "Home":
    judul()
    df = load_data()
    year = select_year()
    location = select_location(df)
    df_filtered = filter_data(df, year, location)
    kolom(df_filtered)
    pie_chart1(df_filtered)
    
elif menu == "Halaman data":
    judul()
    year = select_year()
    df = load_data()
    df_filtered = filter_data(df, year)
    show_data(df_filtered)
   
# Selesai: Dashboard Covid-19 berhasil diimplementasikan dengan navigasi interaktif.






    