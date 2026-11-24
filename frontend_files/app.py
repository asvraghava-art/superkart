
import streamlit as st
import pandas as pd
import requests

st.title("SuperKart Sales Forecasting")

st.write("Enter Product and Store Details")

product_weight = st.number_input("Product Weight", value=10.0)
product_allocated_area = st.number_input("Product Allocated Area", value=0.05)
product_mrp = st.number_input("Product MRP", value=100.0)
store_age_years = st.number_input("Store Age Years", value=10)

product_sugar_content = st.selectbox(
    "Product Sugar Content",
    ["Low Sugar", "Regular", "No Sugar"]
)

store_size = st.selectbox(
    "Store Size",
    ["Small", "Medium", "High"]
)

store_location = st.selectbox(
    "Store Location City Type",
    ["Tier 1", "Tier 2", "Tier 3"]
)

store_type = st.selectbox(
    "Store Type",
    ["Departmental Store",
     "Supermarket Type1",
     "Supermarket Type2",
     "Food Mart"]
)

product_id_char = st.selectbox(
    "Product Id Character",
    ["FD", "DR", "NC"]
)

product_type_category = st.selectbox(
    "Product Type Category",
    ["Perishables", "Non Perishables"]
)

if st.button("Predict Sales"):

    payload = {
        "Product_Weight": product_weight,
        "Product_Sugar_Content": product_sugar_content,
        "Product_Allocated_Area": product_allocated_area,
        "Product_MRP": product_mrp,
        "Store_Size": store_size,
        "Store_Location_City_Type": store_location,
        "Store_Type": store_type,
        "Product_Id_char": product_id_char,
        "Store_Age_Years": store_age_years,
        "Product_Type_Category": product_type_category
    }

    response = requests.post(
        "http://backend:5000/v1/predict",
        json=payload
    )

    if response.status_code == 200:
        prediction = response.json()

        st.success(
            f"Predicted Sales: {prediction['Predicted_Product_Store_Sales_Total']:.2f}"
        )
    else:
        st.error("Prediction failed")
