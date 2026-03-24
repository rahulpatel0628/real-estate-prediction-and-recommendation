import streamlit as st

# Page Config
st.set_page_config(
    page_title="Real Estate Gurugram",
    page_icon="🏠",
    layout="wide"
)

# Title Section
st.title("🏠 Real Estate Gurugram Property Intelligence System")
st.markdown("### Your Smart Assistant for Buying the Perfect Property")

# Banner Image
st.image("https://images.unsplash.com/photo-1560518883-ce09059eeffa")

# Introduction
st.markdown("""
## 📌 About This Project

This project is a **Machine Learning-based Real Estate System** that helps users:
- Predict house prices 💰
- Analyze market trends 📊
- Get personalized property recommendations 🎯

It is built using:
- Python 🐍
- Machine Learning 🤖
- Streamlit 🌐
""")

# Features Section
st.markdown("## 🚀 Key Features")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("📊 **Analysis Module**\n\nExplore property trends, price distribution, and insights.")

with col2:
    st.success("💰 **Price Prediction**\n\nPredict house prices using advanced ML models.")

with col3:
    st.warning("🎯 **Recommendation System**\n\nGet similar properties based on your preferences.")

# How to Use Section
st.markdown("## 🧭 How to Use This App")

st.markdown("""
1. 🏠 Go to **Analysis Module** to explore data insights  
2. 💰 Use **Price Prediction** to estimate property value  
3. 🎯 Use **Recommendation System** to find similar houses  
""")

# Navigation Guide
st.markdown("## 🔗 Navigation")

st.markdown("""
Use the **sidebar** to switch between modules:
- 📊 Analysis
- 💰 Price Prediction
- 🎯 Recommendations
""")

# Sidebar
st.sidebar.title("🏠 Navigation")
st.sidebar.markdown("""
- Home  
- Analysis  
- Price Prediction  
- Recommendations  
""")

# Footer
st.markdown("---")
st.markdown("### 👨‍💻 Developed By Rahul Patel")
st.markdown("🔗 Aspiring Data Scientist | ML Enthusiast")
