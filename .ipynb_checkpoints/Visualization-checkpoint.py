import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from PIL import Image

geoloc_df = pd.read_csv("geolocation_dataset.csv")
order_payments_df = pd.read_csv("order_payments_dataset.csv")
order_item_df = pd.read_csv("order_items_dataset.csv")
orders_df = pd.read_csv("orders_dataset.csv")
product_df = pd.read_csv("products_dataset.csv")
product_category_df = pd.read_csv("product_category_name_translation.csv")
customer_df = pd.read_csv("customers_dataset.csv")

product_df.dropna(axis=0, inplace=True)
orders_df['order_approved_at'].fillna(method='ffill', inplace=True)
orders_df['order_delivered_carrier_date'].fillna(method='ffill', inplace=True)
orders_df['order_delivered_customer_date'].fillna(method='ffill', inplace=True)
geoloc_df.drop_duplicates(inplace=True)

# Merge 'customers' with 'orders' on 'customer_id'
merged_data = pd.merge(customer_df, orders_df, how='inner', on='customer_id')

# Merge the result with 'order_items' on 'order_id'
merged_data = pd.merge(merged_data, order_item_df, how='inner', on='order_id')

# Merge the result with 'order_payments' on 'order_id'
merged_data = pd.merge(merged_data, order_payments_df, how='inner', on='order_id')

# Merge the result with 'product' on 'product_id'
merged_data = pd.merge(merged_data, product_df, how='inner', on='product_id')

# Merge the 'merged_data' dataframe with the translation dataframe
merged_data = pd.merge(merged_data, product_category_df,
                                          how='left',
                                          on='product_category_name')

merged_data = pd.merge(merged_data, geoloc_df,
                                   left_on='customer_zip_code_prefix',
                                   right_on='geolocation_zip_code_prefix',
                                   how='left')

# Calculate transaction frequencies per city
transaction_counts_per_city = merged_data['customer_city'].value_counts()

# You can also calculate the average transaction value per city for additional insights
average_transaction_values_per_city = merged_data.groupby('customer_city')['payment_value'].mean()


st.title("Project Akhir Analisis Data")

# Top 20 cities by transaction counts
st.subheader("Top 20 cities by transaction counts")
plt.figure(figsize=(30, 20))  # Adjust the figure size
top_cities_transaction = transaction_counts_per_city.sort_values(ascending=False).head(20)

# Plotting average transaction values for the top 20 cities
ax = top_cities_transaction.plot(kind='bar', color='lightcoral')
plt.title('Top 20 Cities by Transaction Counts')
plt.xlabel('City')
plt.ylabel('Total Transaction Counts')
plt.ylim(0, 1200000)  # Adjust the y-axis range based on your data
plt.xticks(rotation=45, ha='right')  # Rotate city labels for better visibility

# Annotate each bar with its value
for i, v in enumerate(top_cities_transaction):
    ax.text(i, v + 50, f'{v:.2f}', ha='center', va='bottom', fontsize=8, color='black')

# Display the plot using Streamlit
st.pyplot(plt)

# Top 20 cities by transaction values
st.subheader("Top 20 cities by transaction values")
plt.figure(figsize=(30, 20))  # Adjust the figure size
top_cities_avg_transaction = average_transaction_values_per_city.sort_values(ascending=False).head(20)

# Plotting average transaction values for the top 20 cities
ax = top_cities_avg_transaction.plot(kind='bar', color='lightcoral')
plt.title('Top 20 Cities by Average Transaction Values')
plt.xlabel('City')
plt.ylabel('Average Transaction Value')
plt.ylim(0, 3000)  # Adjust the y-axis range based on your data
plt.xticks(rotation=45, ha='right')  # Rotate city labels for better visibility

# Annotate each bar with its value
for i, v in enumerate(top_cities_avg_transaction):
    ax.text(i, v + 50, f'{v:.2f}', ha='center', va='bottom', fontsize=8, color='black')

# Display the plot using Streamlit
st.pyplot(plt)


st.subheader("Clustering customer's behavior based on price and payment value")
image_path = "Clustering-1.jpeg"
image_file = Image.open(image_path)
st.image(image_file, caption='Clustering graph', use_column_width=True)

