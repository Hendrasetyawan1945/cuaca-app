import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from datetime import datetime

st.set_page_config(layout="wide")

# Memuat data cuaca
data_cuaca = pd.read_csv("seattle-weather.csv")

# Konversi kolom 'date' menjadi objek datetime
data_cuaca['date'] = pd.to_datetime(data_cuaca['date'])

# Change speaker
st.header('Awan Dashboard :sparkles:')
st.image("https://cdn.icon-icons.com/icons2/8/PNG/96/cloudyweather_cloud_inpart_day_wind_thunder_sunny_rain_darkness_nublad_1459.png")
# Penjelasan aplikasi
st.write("Selamat datang di Awan Dashboard! Aplikasi ini memberikan akses ke data cuaca Seattle yang terperinci, "
        "dengan berbagai visualisasi yang informatif. Anda dapat menjelajahi tren cuaca dan kondisi sepanjang waktu.")

st.write("Mari kita mulai mengeksplorasi data cuaca yang menarik!")

# Tombol mulai
if st.button("Mulai Eksplorasi"):
    st.write("Saya siap!")
st.write('\n')
st.write('\n')
# Sidebar untuk filter
st.sidebar.header("Filter Data")
st.sidebar.image("https://storage.googleapis.com/kaggle-datasets-images/480074/897420/77403d4853d89a343d90d4ed63eff720/dataset-thumbnail.jpg?t=2020-01-17-22-06-51")

# Filter berdasarkan tanggal
start_date = st.sidebar.date_input("Pilih Tanggal Awal", data_cuaca['date'].min())
end_date = st.sidebar.date_input("Pilih Tanggal Akhir", data_cuaca['date'].max())

# Filter berdasarkan kondisi cuaca
weather_conditions = st.sidebar.selectbox("Pilih Kondisi Cuaca", ["Semua"] + list(data_cuaca['weather'].unique()))

# Konversi start_date dan end_date menjadi objek datetime
start_date = datetime(start_date.year, start_date.month, start_date.day)
end_date = datetime(end_date.year, end_date.month, end_date.day)

# Menerapkan filter
filtered_data = data_cuaca[(data_cuaca['date'] >= start_date) & (data_cuaca['date'] <= end_date)]
if weather_conditions != "Semua":
    filtered_data = filtered_data[filtered_data['weather'] == weather_conditions]


col1, col2 = st.columns(2)
with col1 :
    # Visualisasi data
    st.subheader("Grafik Suhu Maksimum")
    fig, ax = plt.subplots()
    sns.lineplot(data=filtered_data, x='date', y='temp_max', ax=ax)
    st.pyplot(fig)


with col2 :
    st.subheader("Grafik Jumlah Presipitasi")
    fig, ax = plt.subplots()
    sns.barplot(data=filtered_data, x='date', y='precipitation', ax=ax)
    ax.tick_params(axis='x', labelrotation=45)
    st.pyplot(fig)

st.subheader("Tabel Data Cuaca")
st.write(filtered_data)
st.write('---')

col1, col2 = st.columns(2)
with col1 :
    # Visualisasi data
    st.subheader("Grafik Suhu Maksimum")
    fig, ax = plt.subplots()
    sns.lineplot(data=filtered_data, x='date', y='temp_max', ax=ax)
    st.pyplot(fig)
with col2 :
    st.subheader("Grafik Jumlah Presipitasi")
    fig, ax = plt.subplots()
    sns.barplot(data=filtered_data, x='date', y='precipitation', ax=ax)
    ax.tick_params(axis='x', labelrotation=45)
    st.pyplot(fig)
st.write('---')

col1, col2 ,col3= st.columns(3)
with col1 :
    # Tambah visualisasi data tambahan
    st.subheader("Grafik Suhu Minimum")
    fig, ax = plt.subplots()
    sns.lineplot(data=filtered_data, x='date', y='temp_min', ax=ax)
    st.pyplot(fig)

with col2 :
    st.subheader("Grafik Kecepatan Angin")
    fig, ax = plt.subplots()
    sns.lineplot(data=filtered_data, x='date', y='wind', ax=ax)
    st.pyplot(fig)

with col3 :
    st.subheader("Grafik Jumlah Presipitasi (Total)")
    fig, ax = plt.subplots()
    sns.barplot(data=filtered_data, x='date', y='precipitation', estimator=sum, ax=ax)
    ax.tick_params(axis='x', labelrotation=45)
    st.pyplot(fig)



st.markdown('---')
st.subheader("Keterangan Aplikasi")
st.write("Aplikasi ini memungkinkan Anda untuk mengeksplorasi data cuaca di Seattle. Anda dapat menggunakan filter di sidebar untuk memilih rentang tanggal dan kondisi cuaca yang Anda minati.")
st.write("Visualisasi data meliputi grafik suhu maksimum, grafik suhu minimum, grafik kecepatan angin, dan grafik jumlah presipitasi.")
st.write("Selamat Belajar!")

# Keterangan
st.caption('Copyright © Hendra Saja 2023')
