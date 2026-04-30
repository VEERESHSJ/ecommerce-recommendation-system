import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

st.title("🛒 E-Commerce Recommendation System")

# Load dataset
df = pd.read_csv("sample_ratings.csv")

st.write("Dataset:")
st.write(df)

# Create user-item matrix
matrix = df.pivot_table(index='user_id', columns='product_id', values='rating').fillna(0)

# Similarity
similarity = cosine_similarity(matrix)

# Recommend function
def recommend(user_index):
    scores = list(enumerate(similarity[user_index]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:4]
    users = matrix.index
    return [users[i] for i, _ in scores]

# UI
user_input = st.number_input("Enter User Index (0,1,2)", min_value=0, max_value=2, step=1)

if st.button("Recommend"):
    recs = recommend(user_input)
    st.subheader("Recommended Similar Users:")
    for r in recs:
        st.write(f"User {r}")
