# 🕵️‍♂️ Fake Social Media Account Detection

A Machine Learning based web application that detects whether a social media account is **Fake or Real** using behavioral and profile-based features.

---

## 📌 Project Overview

This project focuses on identifying fake social media accounts by analyzing various user attributes such as engagement patterns, username characteristics, and account activity. The system uses machine learning models to classify accounts and provides real-time predictions through an interactive web interface.

---

## 🚀 Features

* Detects fake vs real social media accounts
* Uses behavioral and profile-based features
* Interactive UI built with Streamlit
* Real-time prediction with probability scores
* Clean and user-friendly interface

---

## 🧠 Machine Learning Models Used

* Logistic Regression
* Support Vector Machine (SVM)
* Random Forest (Final Model Used)

---

## 📊 Input Features

* Username length, digits, special characters
* Username randomness
* Followers and following count
* Follower/Following ratio
* Engagement rate
* Posts and posts per day
* Spam and generic comment rate
* Account age
* Profile picture presence
* Verified status
* Suspicious links in bio
* Platform (Facebook, Instagram, X)

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Joblib

---

## ⚙️ Project Structure

```
├── app.py
├── model_rf_FSD.pkl
├── scaler.pkl
├── columns.pkl
├── Fake_SocialMedia_Account_detection.ipynb
└── README.md
```

---

## ▶️ How to Run the Project

### 1. Clone the repository

```
git clone https://github.com/SATYA012904/ml-fake-social-media-detection.git
cd ml-fake-social-media-detection
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Run the application

```
streamlit run app.py
```

---

## 📈 Model Performance

* Accuracy: ~90%
* Evaluated using:

  * Precision
  * Recall
  * F1-score
  * Confusion Matrix

---

## 💡 Key Highlights

* Strong feature engineering based on real-world fake account patterns
* Comparison of multiple machine learning models
* Interactive deployment using Streamlit
* Useful for cybersecurity and social media analysis

---

## 📌 Future Improvements

* Add deep learning models
* Integrate real-time API for live data
* Add feature importance visualization
* Deploy on cloud platforms

---

## 👨‍💻 Author

Satyabrata Sahu
B.Tech Computer Science Student

---

## 📜 License

This project is for educational purposes.


