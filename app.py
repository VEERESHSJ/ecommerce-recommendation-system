import streamlit as st
import pandas as pd

st.title("E-Commerce Recommendation System")

# simple working data
data = {
    "User": [1, 1, 2, 2],
    "Product": ["Mobile", "Laptop", "Laptop", "Headphones"],
    "Rating": [5, 4, 5, 3]
}

df = pd.DataFrame(data)

st.write("App is working ✅")
st.write(df)
