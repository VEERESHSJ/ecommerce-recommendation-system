import streamlit as st
import pandas as pd

st.title("E-Commerce Recommendation System")

data = {
    "User": [1, 2, 3],
    "Product": ["Mobile", "Laptop", "Headphones"],
    "Rating": [5, 4, 3]
}

df = pd.DataFrame(data)

st.write("App is working ✅")
st.write(df)
