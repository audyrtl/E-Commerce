import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import calendar
sns.set(style='dark')

# Fungsi untuk mengambil data
def load_data():
    # Gantilah 'path_to_hour_df' dengan lokasi file hour_df.csv
    merged_df = pd.read_csv('https://raw.githubusercontent.com/audyrtl/E-Commerce/main/dashboard/main_data.csv')
    return merged_df

# Memuat data
merged_df=load_data()

# Sidebar
with st.sidebar:
    st.markdown(
        """
        <div style='display: flex; align-items: center; justify-content: center;'>
            <img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQLJSvewL0Q9fta2XVO4JXqeEt_NpeSbh7hpA&usqp=CAU' alt='Logo' style='width: 80px; height: 100px;'>
            <div style='margin-left: 10px; font-size: 30px; font-weight: bold; color: #817dad;'>Audy's</div>
            <div style='margin-left: 10px; font-size: 24px; color: #817dad;'>E-Commerce Projects</div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown("<hr style='margin: 15px 0; border-color: #817dad;'>", unsafe_allow_html=True)

    st.markdown("<div style='margin-left: 10px; font-size: 17px; color: #817dad;'>E-Commerce Public Dataset</div>", unsafe_allow_html=True)
    st.markdown("[Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)")

    st.markdown("<hr style='margin: 15px 0; border-color: #817dad;'>", unsafe_allow_html=True)

    st.markdown("<div style='margin-left: 10px; font-size: 17px; color: #817dad;'>Silahkan hubungi saya untuk informasi lebih lanjut.</div>",
        unsafe_allow_html=True)
    st.markdown(
        """
        - Email: [shabinaaudy@gmail.com.com](mailto:shabinaaudy@gmail.com)
        - Linkedin: [Shabina Retalia Audy](https://www.linkedin.com/in/shabina-audy-81b890237/)
        """,
        unsafe_allow_html=True
    )
    st.markdown("<hr style='margin: 15px 0; border-color: #817dad;'>", unsafe_allow_html=True)
    
    st.caption('Copyright (C) Shabina R Audy. 2024')

# Membuat judul
st.markdown(
    "<h1>Proyek Analisis Data E-Commerce</h1>",
    unsafe_allow_html=True
)
st.write("")

# Menampilkan hasil pertanyaan 1
st.markdown(
    "<h3 style='color: #faaff5;'>Pertanyaan 1</h3>",
    unsafe_allow_html=True
)
st.markdown(
    "<h3 style='color: #faaff5;'>Berapakah rata-rata waktu pengiriman barang ke pelanggan untuk setiap negara bagian, mulai dari tanggal pembelian hingga tanggal penerimaan oleh pelanggan?</h3>",
    unsafe_allow_html=True
)
st.markdown(
    "<h4 style='text-align: center; color: #925ccc;'>Rata-Rata Lama Pengiriman per Negara Bagian</h4>",
    unsafe_allow_html=True
)


# Menampilkan bar chart
mean_delivered_orders = merged_df[merged_df['order_status'] == 'delivered'].groupby('customer_state')['delivery_time'].mean().reset_index()
st.bar_chart(mean_delivered_orders.set_index('customer_state'))

# Menampilkan kesimpulan
st.write("""<div style="text-align: justify; color: #c1abd9;">
Dari data yang disajikan, dapat disimpulkan bahwa rata-rata waktu pengiriman barang ke pelanggan bervariasi di setiap negara bagian. Negara bagian dengan rata-rata waktu pengiriman terpendek adalah São Paulo (SP) dengan 8.74 hari, sementara negara bagian dengan rata-rata waktu pengiriman terpanjang adalah Roraima (RR) dengan 29.34 hari. Banyak faktor-faktor yang dapat menyebabkan perbedaan waktu pengiriman antar negara bagian tersebut, seperti lokasi geografis, infrastruktur logistik, dan kebijakan pengiriman yang berbeda.
</div>""",
unsafe_allow_html=True
)
st.write("")
st.markdown("<hr style='margin: 15px 0; border-color: #817dad;'>", unsafe_allow_html=True)

# Menampilkan hasil pertanyaan 2
st.markdown(
    "<h3 style='color: #faaff5;'>Pertanyaan 2</h3>",
    unsafe_allow_html=True
)
st.markdown(
    "<h3 style='color: #faaff5;'>Negara bagian manakah yang memiliki volume pesanan barang tertinggi dibandingkan dengan negara bagian lainnya?</h3>",
    unsafe_allow_html=True
)
st.markdown(
    "<h4 style='text-align: center; color: #925ccc;'>Jumlah Pesanan per Negara Bagian</h4>",
    unsafe_allow_html=True
)

# Menghitung jumlah pesanan (order_id) per customer_state
state_fixed_orders = merged_df[~merged_df['order_status'].isin(['unavailable', 'canceled'])].groupby('customer_state')['order_id'].count().reset_index()
state_fixed_orders.columns = ['customer_state', 'order_count']

# Menampilkan bar chart
st.bar_chart(state_fixed_orders.set_index('customer_state'))

# Menampilkan kesimpulan
st.write("""<div style="text-align: justify; color: #c1abd9;">
Dari data yang disajikan, dapat disimpulkan bahwa negara bagian dengan volume pesanan barang tertinggi adalah São Paulo (SP) dengan 41,127 pesanan. Diikuti oleh Rio de Janeiro (RJ) dengan 12,698 pesanan dan Paraná (PR) dengan 4,983 pesanan. Negara bagian dengan volume pesanan terendah adalah Roraima (RR) dengan 45 pesanan. Analisis ini dapat memberikan informasi yang berharga bagi perusahaan untuk mengarahkan strategi pemasaran dan distribusi mereka ke negara bagian dengan volume pesanan tertinggi untuk meningkatkan penjualan dan keuntungan. Selain itu, perusahaan bisa juga memasang strategi untuk mendongkrak pesanan pada negara bagian yang memiliki volume pesanan sedikit.
</div>""",
unsafe_allow_html=True
)
st.write("")
st.markdown("<hr style='margin: 15px 0; border-color: #817dad;'>", unsafe_allow_html=True)


# Menampilkan hasil pertanyaan 3
st.markdown(
    "<h3 style='color: #faaff5;'>Pertanyaan 3</h3>",
    unsafe_allow_html=True
)
st.markdown(
    "<h3 style='color: #faaff5;'>Berdasarkan data penjualan 2017, pada bulan apa permintaan paling banyak terjadi, diukur dari jumlah pesanannya?</h3>",
    unsafe_allow_html=True
)
st.markdown(
    "<h4 style='text-align: center; color: #925ccc;'>Jumlah Pesanan per Bulan Tahun 2017</h4>",
    unsafe_allow_html=True
)

# Konversi kolom 'order_purchase_timestamp' ke format datetime
merged_df['order_purchase_timestamp'] = pd.to_datetime(merged_df['order_purchase_timestamp'])

# Filter data untuk tahun 2017
merged_df_2017 = merged_df[merged_df['order_purchase_timestamp'].dt.year == 2017]

# Menghitung jumlah pesanan (order_id) per bulan
order_counts_per_month_2017 = merged_df_2017.groupby(merged_df_2017['order_purchase_timestamp'].dt.month)['order_id'].count().reset_index()
order_counts_per_month_2017.columns = ['month', 'order_count']

# Mengubah angka bulan menjadi nama bulan
order_counts_per_month_2017['month'] = order_counts_per_month_2017['month'].apply(lambda x: calendar.month_name[x])

# Mengatur urutan bulan sesuai urutan Januari hingga Desember
month_order = [calendar.month_name[i] for i in range(1, 13)]
order_counts_per_month_2017['month'] = pd.Categorical(order_counts_per_month_2017['month'], categories=month_order, ordered=True)

# Mengurutkan DataFrame berdasarkan urutan bulan
order_counts_per_month_2017.sort_values(by='month', inplace=True)

# Menampilkan line chart
st.line_chart(order_counts_per_month_2017.set_index('month'))

# Menampilkan kesimpulan
st.write("""<div style="text-align: justify; color: #c1abd9;">
Berdasarkan data penjualan tahun 2017, permintaan paling tinggi terjadi pada bulan November, dengan jumlah pesanan mencapai 7,544. Bulan-bulan lain yang juga memiliki permintaan tinggi adalah bulan Oktober (4,631 pesanan) dan Desember (5,673 pesanan). Sedangkan permintaan paling sedikit jatuh pada bulan Januari (800 pesanan). Hal ini menunjukkan bahwa pada kuartal terakhir tahun 2017, terjadi peningkatan signifikan dalam permintaan barang, mungkin terkait dengan musim liburan dan akhir tahun di mana konsumen cenderung melakukan lebih banyak pembelian. Analisis ini dapat membantu perusahaan untuk mempersiapkan stok dan strategi pemasaran yang tepat untuk menghadapi lonjakan permintaan pada bulan-bulan tersebut di tahun-tahun berikutnya.
</div>""",
unsafe_allow_html=True
)
st.write("")

