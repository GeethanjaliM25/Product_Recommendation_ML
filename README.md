User-Based Product Recommendation System

A production-style collaborative filtering recommendation system that predicts relevant product categories for users by analyzing behavioral similarity using cosine similarity.
Built with Python, Scikit-learn, and Streamlit for interactive, real-time recommendations...

✨ Why This Project?

Personalized recommendations are core to modern e-commerce platforms.
This project demonstrates how user similarity can be leveraged to infer preferences without explicit product ratings, using only behavioral and demographic signals.

🧠 How It Works

User behavioral data is preprocessed and normalized

Cosine similarity is computed between users

The top-K most similar users are identified

Product categories are recommended via majority voting

Technique: User-Based Collaborative Filtering

🚀 Key Highlights

Clean end-to-end recommendation pipeline

Feature scaling with StandardScaler

Similarity computation using cosine_similarity

Interactive UI built with Streamlit

Designed for one-user–one-category datasets

🗂 Repository Structure
Product_Recommendation/
├── data/
│   └── user_personalized_features.csv
├── app.py
├── test.py
├── requirements.txt
└── README.md

🛠 Tech Stack
Layer	Technology
Language	Python
Data Processing	Pandas, NumPy
Machine Learning	Scikit-learn
Similarity Metric	Cosine Similarity
Interface	Streamlit
▶️ Run Locally
pip install -r requirements.txt
streamlit run app.py

📌 Current Limitations

Cold-start issue for new users

No item-level similarity modeling

Assumes one category per user

🔮 Future Scope

Hybrid recommendation (user + item based)

Real-time behavior tracking

Model evaluation metrics

Database and cloud deployment

👩‍💻 Author

Geethanjali M
B.E. Student | Machine Learning & Data Science
