import streamlit as st
import pandas as pd
import plotly.express as px

def load_data():
    df = pd.read_csv("dataset/covid_19_indonesia_time_series_all.csv")
    return df

def filter_data(df,  year=None):
    if year:
        df = df[df['Date'].astype(str).str.contains(str(year))]
    return df

def select_year():
    return st.sidebar.selectbox(
        "Pilih Tahun 📅",
        options=[None, 2020, 2021, 2022],
        format_func=lambda x: "Semua Tahun" if x is None else str(x)
    )


def show_data(df):
    selected_columns = ['Location'] + list(df.loc[:, 'New Cases':'Total Recovered'].columns)
    df_selected = df[selected_columns]
    st.subheader("Data Covid-19 Indonesia 🔴⚪")
    st.dataframe(df_selected.head(10))

def total_case(df):
    total_kasus = df['Total Cases'].sum()
    return total_kasus

def total_death(df):
    total_kematian = df['Total Deaths'].sum()
    return total_kematian

def total_recovery(df):
    total_sembuh = df['Total Recovered'].sum()
    return total_sembuh

def kolom(df):
    kasus = total_case(df)    
    kematian = total_death(df)
    sembuh = total_recovery(df)

    coll, col2, col3 = st.columns(3)
    coll.metric(label="Total Kasus 📈", value=f"{kasus/1000:.1f}k", border=True)
    col2.metric(label="Total Kematian 🧟", value=f"{kematian/1000:.1f}k",border=True)
    col3.metric(label="Total Sembuh 🏋️‍♀️", value=f"{sembuh/1000:.1f}k",border=True)

def pie_chart1(df):
    total_mati = total_death(df)
    total_sembuh = total_recovery(df)

    data = {
        'Status': ['Meninggal', 'Sembuh'],
        'Jumlah': [total_mati, total_sembuh]
    }

    fig = px.pie(
        data,
        names='Status',
        values='Jumlah',
        title='Perbandingan Total Kematian VS Total Kesembuhan',
        hole=0.5,
        color_discrete_sequence=['#4de89f', '#ff6459']  # also fix typo here
    )

    st.plotly_chart(fig, use_container_width=True)







