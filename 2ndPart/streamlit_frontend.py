import streamlit as st
from zeep import Client

client = Client("http://127.0.0.1:8000/?wsdl")

st.title("Product Catalog Management")

# Add Product
st.header("Add Product")
with st.form("add_form"):
    product_id = st.number_input("Product ID", step=1, min_value=1)
    name = st.text_input("Name")
    description = st.text_input("Description")
    price = st.number_input("Price", step=0.01, min_value=0.0)
    add_btn = st.form_submit_button("Add Product")
    if add_btn:
        response = client.service.add_product(product_id, name, description, price)
        st.success(response)

# Delete Product
st.header("Delete Product")
delete_id = st.number_input("Product ID to Delete", step=1, min_value=1)
if st.button("Delete Product"):
    response = client.service.delete_product(delete_id)
    st.success(response)

# Update Product
st.header("Update Product")
with st.form("update_form"):
    update_id = st.number_input("Product ID to Update", step=1, min_value=1)
    new_name = st.text_input("New Name")
    new_description = st.text_input("New Description")
    new_price = st.number_input("New Price", step=0.01, min_value=0.0)
    update_btn = st.form_submit_button("Update Product")
    if update_btn:
        response = client.service.update_product(update_id, new_name, new_description, new_price)
        st.success(response)

# Get All Products
st.header("All Products")
if st.button("Retrieve Products"):
    products = client.service.get_all_products()
    for product in products:
        st.write(product)
