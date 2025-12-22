🧠 Product Recommendation System (User-Based Collaborative Filtering)

A User-Based Product Recommendation System that predicts product category preferences for users by identifying similar users using cosine similarity on behavioral and demographic features.
The application is built using Python, Scikit-learn, and Streamlit with an interactive web interface.

📌 Project Overview

This project recommends product categories to a selected user by analyzing the preferences of most similar users.
It uses collaborative filtering and works best for one-user–one-category datasets, making it suitable for academic mini projects and demonstrations.

🚀 Features

👤 User-based collaborative filtering

📊 Behavioral and demographic feature analysis

🧮 Cosine similarity for user similarity measurement

⚖️ Feature normalization using StandardScaler

🖥️ Interactive Streamlit web application

🔍 Displays similar users with similarity scores

🛒 Predicts top N product categories

🧠 Recommendation Technique

Approach: User-Based Collaborative Filtering

Workflow:

Load user behavioral dataset

Select numerical features

Normalize features using StandardScaler

Compute cosine similarity between users

Identify top similar users

Recommend product categories using majority voting

📂 Project Structure
Product_Recommendation/
│
├── data/
│   └── user_personalized_features.csv
│
├── app.py
├── test.py
├── requirements.txt
└── README.md

📊 Dataset Description

Each row in the dataset represents a single user profile containing demographic and behavioral information.

Features Used:

Age

Income

Purchase Frequency

Average Order Value

Total Spending

Time Spent on Site (minutes)

Pages Viewed

Last Login Days Ago

Product Category Preference (Target)

🛠️ Technologies Used

Python

Pandas

NumPy

Scikit-learn

Streamlit

Cosine Similarity

StandardScaler

▶️ How to Run the Project
1️⃣ Clone the Repository
git clone https://github.com/your-username/Product_Recommendation.git
cd Product_Recommendation

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run the Streamlit App
streamlit run app.py

🖥️ Application Output

Select a User Index

Choose number of predicted categories

Click Predict Preferences

View:

Selected user profile

Similar users with similarity scores

Recommended product categories

📈 Sample Output

Similar Users

User 809 → Similarity: 0.948

User 274 → Similarity: 0.879

Predicted Product Categories

Apparel (chosen by 3 similar users)

Books (chosen by 2 similar users)

⚠️ Limitations

Cold-start problem for new users

Does not consider item-level similarity

Best suited for one-category-per-user datasets

🔮 Future Enhancements

Item-based collaborative filtering

Hybrid recommendation system

Real-time interaction tracking

Database integration

Model evaluation metrics (Precision, Recall)

🎓 Academic Use

This project is suitable for:

Machine Learning Mini Projects

Data Science Laboratory Work

Recommendation System Demonstrations

Pre-final and Final Year Engineering Projects

👩‍💻 Author

Geethanjali M
B.E. Student | Machine Learning Enthusiast
