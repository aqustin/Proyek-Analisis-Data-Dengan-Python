import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Judul aplikasi
st.title("Analisis Produk dengan Minat Jual Tertinggi")

# Upload file data
order_items_file = st.file_uploader("Upload file order_items_dataset.csv", type="csv")
products_file = st.file_uploader("Upload file products_dataset.csv", type="csv")

if order_items_file is not None and products_file is not None:
    # Membaca data
    order_items_dataset_df = pd.read_csv(order_items_file)
    products_dataset_df = pd.read_csv(products_file)

    # Group by product ID and count the number of orders for each product
    product_order_counts = order_items_dataset_df.groupby('product_id')['order_id'].count()

    # Sort the product order counts in descending order and get the top 10
    top_10_products = product_order_counts.sort_values(ascending=False).head(10)

    # Tampilkan hasil di Streamlit
    st.write("Top 10 Products with the Highest Number of Orders:")
    st.write(top_10_products)

    # Visualisasikan hasil dengan bar chart
    plt.figure(figsize=(10, 6))
    top_10_products.plot(kind='bar')
    plt.title('Top 10 Products with Highest Number of Orders')
    plt.xlabel('Product ID')
    plt.ylabel('Number of Orders')

    # Tampilkan plot di Streamlit
    st.pyplot(plt)
    
    # Clear the figure after plotting
    plt.clf()
