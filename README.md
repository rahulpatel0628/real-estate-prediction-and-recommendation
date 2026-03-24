# 🏠 Real Estate Gurugram Property Intelligence System

🚀 A complete **Machine Learning + Data Analysis + Recommendation System** for real estate, built using real-world Gurugram property data.

This project helps users:

* 📊 Analyze property trends
* 💰 Predict house prices
* 🎯 Get personalized property recommendations

---

## 📌 Project Modules

### 🏠 1. Home Page

* Overview of the project
* Navigation guide
* User-friendly interface

### 📊 2. Analysis Module

* Exploratory Data Analysis (EDA)
* Price trends and distributions
* Feature relationships

### 💰 3. Price Prediction Module

* Predict property prices using ML models
* Input features:

  * Sector / Location
  * Area (sqft)
  * Bedrooms, Bathrooms, Balcony
  * Furnishing type
  * Luxury category

### 🎯 4. Recommendation System

* Suggests similar properties
* Based on:

  * Cosine similarity
  * Location distance
  * Feature similarity

---

## 🛠️ Tech Stack

* **Frontend:** Streamlit
* **Backend:** Python
* **Machine Learning:** Scikit-learn, XGBoost
* **Data Processing:** Pandas, NumPy
* **Visualization:** Plotly, Matplotlib, Seaborn
* **Model Serialization:** Pickle
* **Deployment:** AWS ☁️

---

## 📂 Project Structure

```bash
project/
│
├── data/
│   ├── apartments.csv
│   ├── flats_cleaned.csv
│   ├── gurgaon_properties.csv
│   ├── gurgaon_properties_cleaned_v1.csv
│   ├── house_cleaned.csv
│   └── ...
│
├── notebooks/
│   ├── data-preprocessing-flats.ipynb
│   ├── data-preprocessing-house.ipynb
│   ├── feature-engineering.ipynb
│   ├── feature-selection.ipynb
│   ├── model-selection.ipynb
│   ├── recommender-system.ipynb
│   └── ...
│
├── pages/
│   ├── 1_Analysis App.py
│   ├── 2_Price Predictor.py
│   └── 3_Recommend Appartments.py
│
├── Recommended/
│   ├── cosine_sim1.pkl
│   ├── cosine_sim2.pkl
│   ├── cosine_sim3.pkl
│   ├── location_distance.pkl
│── df.pkl
├── feature_text.pkl
 ── model.pkl
│
├── home.py
├── requirements.txt
└── README.md
```

---

## ⚙️ How to Run Locally

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/rahulpatel0628/real-estate-prediction-and-recommendation.git
cd real-estate-prediction-and-recommendation
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run Streamlit App

```bash
streamlit run home.py
```

---

## 🤖 Machine Learning Pipeline

* Data Cleaning & Preprocessing
* Missing Value Handling
* Outlier Detection & Treatment
* Feature Engineering
* Feature Selection
* Model Training & Evaluation

### Models Used:

* Linear Regression
* Ridge & Lasso
* Decision Tree
* Random Forest
* Extra Trees
* Gradient Boosting
* XGBoost

---

## 🎯 Recommendation System Logic

Hybrid recommendation using weighted similarity:

```python
cosine_sim_matrix = 30 * cosine_sim1 + 20 * cosine_sim2 + 8 * cosine_sim3
```

* Combines multiple similarity matrices
* Improves recommendation accuracy
* Uses location distance + feature similarity

---

## ☁️ Deployment (AWS)

This project is deployed on **AWS Cloud**.

### Steps:

1. Launch EC2 instance
2. Install Python & dependencies
3. Clone repository
4. Install requirements
5. Run Streamlit app

```bash
streamlit run home.py --server.port 8501 --server.address 0.0.0.0
```

### Access App:

```
http://<your-ec2-public-ip>:8501
```

---

## 📈 Future Enhancements

* 🌍 Expand to All India dataset
* 🗺️ Map-based visualization (lat-long)
* 📉 Price trend forecasting
* 🔄 Real-time data scraping
* ⚙️ MLOps pipeline integration

---

## 👨‍💻 Author

**Rahul Patel**
🎯 Aspiring Data Scientist | ML Engineer

* 🔗 GitHub: https://github.com/rahulpatel0628
