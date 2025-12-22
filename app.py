import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity
from collections import Counter

# =============================
# PAGE CONFIG
# =============================
st.set_page_config(page_title="User Similarity Recommendation", layout="wide")
st.title("🧠 User-Based Product Category Recommendation System")
st.write("Prediction based on user similarity (Correct for one-user-one-category data)")

# =============================
# LOAD DATA
# =============================
@st.cache_data
def load_data():
    df = pd.read_csv(
        r"C:\Users\Geethanjali\OneDrive\New folder\Product_Recommendation\data\user_personalized_features.csv"
    )
    df.columns = df.columns.str.lower().str.strip()
    return df

df = load_data()

# =============================
# DATA PREVIEW
# =============================
st.subheader("📄 Dataset Preview")
st.dataframe(df.head())

# =============================
# FEATURE SELECTION
# =============================
feature_cols = [
    "age",
    "income",
    "purchase_frequency",
    "average_order_value",
    "total_spending",
    "time_spent_on_site_minutes",
    "pages_viewed",
    "last_login_days_ago"
]

X = df[feature_cols].fillna(df[feature_cols].mean())

# =============================
# NORMALIZATION
# =============================
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# =============================
# USER SIMILARITY
# =============================
similarity_matrix = cosine_similarity(X_scaled)
similarity_df = pd.DataFrame(
    similarity_matrix,
    index=df.index,
    columns=df.index
)

# =============================
# RECOMMENDATION FUNCTION
# =============================
def predict_categories(user_index, top_n=3):
    # Get similar users (excluding self)
    similar_users = similarity_df[user_index].sort_values(ascending=False)[1:6]

    categories = df.loc[similar_users.index, "product_category_preference"]

    # Count category frequency
    predicted = Counter(categories).most_common(top_n)
    return predicted, similar_users

# =============================
# SIDEBAR
# =============================
st.sidebar.header("🔍 Recommendation Panel")
user_index = st.sidebar.selectbox("Select User Index", df.index)
num_recs = st.sidebar.slider("Number of Predicted Categories", 1, 5, 3)
predict_btn = st.sidebar.button("Predict Preferences")

# =============================
# OUTPUT
# =============================
if predict_btn:
    st.subheader("👤 Selected User Profile")
    st.json(df.loc[user_index].to_dict())

    predicted_categories, similar_users = predict_categories(user_index, num_recs)

    st.subheader("👥 Similar Users (Similarity Score)")
    for uid, score in similar_users.items():
        st.write(f"User {uid} → Similarity: {round(score, 3)}")

    st.subheader("🛒 Predicted Product Categories")
    for cat, freq in predicted_categories:
        st.markdown(f"- **{cat}** (chosen by {freq} similar users)")

# =============================
# FOOTER
# =============================
st.markdown("---")
st.caption("User-Based Recommendation | Cosine Similarity | Behavioral Features")
