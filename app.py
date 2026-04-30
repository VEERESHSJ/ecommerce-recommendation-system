import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

st.title("🛒 E-Commerce Recommendation System")

# Load dataset (small sample only!)
@st.cache_data
def load_data():
    df = pd.read_json("ratings_Electronics.json", lines=True)
    df = df[['reviewerID', 'asin', 'overall']]
    df = df.head(5000)   # limit data
    return df

df = load_data()

st.write("Data Loaded ✅")
st.write(df.head())

# Create user-item matrix
user_item_matrix = df.pivot_table(index='reviewerID', columns='asin', values='overall').fillna(0)

# Compute similarity
similarity = cosine_similarity(user_item_matrix)

# Recommend function
def recommend_products(user_index, n=5):
    sim_scores = list(enumerate(similarity[user_index]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:n+1]
    user_ids = user_item_matrix.index
    return [user_ids[i] for i, _ in sim_scores]

# UI
user_number = st.number_input("Enter User Index (0-100)", min_value=0, max_value=100, step=1)

if st.button("Recommend"):
    recs = recommend_products(user_number)
    st.subheader("🎯 Recommended Users:")
    for r in recs:
        st.write(r)
