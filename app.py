# app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Buat data sample secara manual
data = pd.DataFrame({
    'Bulan': ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun'],
    'Penjualan': [100, 150, 200, 180, 250, 220]
})

# Fungsi untuk menampilkan grafik menggunakan Matplotlib
def plot_data(data, gender, selected_months):
    st.title('Visualisasi Data Penjualan Bulanan')
    st.write(data)

    st.subheader('Grafik Penjualan Bulanan')
    fig, ax = plt.subplots()
    data.plot(x='Bulan', y='Penjualan', ax=ax)
    plt.xlabel('Bulan')
    plt.ylabel('Penjualan')
    st.pyplot(fig)

    st.subheader('Hasil Pilihan Anda')
    st.write(f'Gender: {gender}')
    st.write(f'Bulan Terpilih: {", ".join(selected_months)}')

def main():
    st.header('Aplikasi Visualisasi Data dengan Streamlit')

    gender = st.radio('Pilih jenis kelamin', ['Pria', 'Wanita'])
    selected_months = st.multiselect('Pilih bulan', data['Bulan'])

    plot_data(data, gender, selected_months)

if __name__ == '__main__':

    
    main()
