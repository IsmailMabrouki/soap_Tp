import streamlit as st
from zeep import Client

# SOAP WSDL URL
wsdl = "http://localhost:8000/?wsdl"

# Create the SOAP client
client = Client(wsdl=wsdl)

# Streamlit App
st.title("SOAP Calculator Service")

# User inputs
st.subheader("Perform Calculations")

operation = st.selectbox("Select Operation", ["Add", "Multiply"])
num1 = st.number_input("Enter the first number", value=0, step=1)
num2 = st.number_input("Enter the second number", value=0, step=1)

# Perform calculation
if st.button("Calculate"):
    if operation == "Add":
        result = client.service.add(num1, num2)
        st.success(f"Addition Result: {result}")
    elif operation == "Multiply":
        result = client.service.multiply(num1, num2)
        st.success(f"Multiplication Result: {result}")
