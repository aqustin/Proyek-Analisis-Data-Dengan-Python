import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Judul aplikasi
st.title("Analisis Produk dengan Jumlah Review Tertinggi")

# Upload file data
products_file = st.file_uploader("Upload file products_dataset.csv", type="csv")
order_items_file = st.file_uploader("Upload file order_items_dataset.csv", type="csv")

if products_file is not None and order_items_file is not None:
    # Membaca data
    products_dataset_df = pd.read_csv(products_file)
    order_items_dataset_df = pd.read_csv(order_items_file)

    # Gabungkan data products_dataset dan order_items_dataset berdasarkan product_id
    merged_df = pd.merge(products_dataset_df, order_items_dataset_df, on='product_id', how='inner')

    # Hitung jumlah review untuk setiap produk
    product_reviews_count = merged_df.groupby('product_category_name')['order_item_id'].count().sort_values(ascending=False)

    # Tampilkan 10 produk dengan jumlah review paling tinggi
    top_10_products_reviews = product_reviews_count.head(10)

    # Tampilkan hasil di Streamlit
    st.write("10 Produk dengan Jumlah Review Paling Tinggi:")
    st.write(top_10_products_reviews)

    # Visualisasikan hasil dengan bar chart
    plt.figure(figsize=(12, 6))
    sns.barplot(x=top_10_products_reviews.index, y=top_10_products_reviews.values)
    plt.xlabel("Kategori Produk")
    plt.ylabel("Jumlah Review")
    plt.title("10 Produk dengan Jumlah Review Paling Tinggi")
    plt.xticks(rotation=45, ha="right")

    # Tampilkan plot di Streamlit
    st.pyplot(plt)
