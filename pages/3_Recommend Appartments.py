import streamlit as st
import pickle
import pandas as pd

st.set_page_config(page_title="Property Recommendation", layout="wide")

#load data
@st.cache_data
def load_data():
    location_distance = pickle.load(open("Recommended/location_distance.pkl", "rb"))
    cosine_sim1 = pickle.load(open("Recommended/cosine_sim1.pkl", "rb"))
    cosine_sim2 = pickle.load(open("Recommended/cosine_sim2.pkl", "rb"))
    cosine_sim3 = pickle.load(open("Recommended/cosine_sim3.pkl", "rb"))
    return location_distance, cosine_sim1, cosine_sim2, cosine_sim3

location_distance, cosine_sim1, cosine_sim2, cosine_sim3 = load_data()

#function for recommendation
def recommend_properties(property_name, top_n=10):
    cosine_sim_matrix = 30 * cosine_sim1 + 20 * cosine_sim2 + 8 * cosine_sim3

    idx = location_distance.index.get_loc(property_name)
    sim_scores = list(enumerate(cosine_sim_matrix[idx]))

    sorted_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    top_indices = [i[0] for i in sorted_scores[1:top_n + 1]]
    top_scores = [i[1] for i in sorted_scores[1:top_n + 1]]

    recommendations = pd.DataFrame({
        'Property': location_distance.index[top_indices],
        'Similarity Score': [round(score, 3) for score in top_scores]
    })

    return recommendations

#title
st.markdown("<h1 style='text-align:center; color:#2E86C1;'>🏠 Property Recommendation System</h1>", unsafe_allow_html=True)
st.markdown("---")

#location and distance wise properties
st.subheader("📍 Find Nearby Properties")

col1, col2 = st.columns(2)

location = col1.selectbox("Select Location", sorted(location_distance.columns))
distance = col2.slider("Select Radius (KM)", 1, 20, 5)

if st.button("🔍 Search Nearby Properties"):

    nearby = location_distance[location_distance[location] < distance * 1000][location]
    nearby = nearby.sort_values()

    if nearby.empty:
        st.warning("⚠️ No properties found in this range")
    else:
        st.success(f"✅ Found {len(nearby)} properties")

        result_df = pd.DataFrame({
            "Property": nearby.index,
            "Distance (KM)": (nearby.values / 1000).round(2)
        })

        st.dataframe(result_df, use_container_width=True)

#Similarity Based Property
st.markdown("---")
st.subheader("🤖 Similar Property Recommendations")

selected_property = st.selectbox("Select Property", sorted(location_distance.index))
top_n = st.slider("Number of Recommendations", 5, 20, 10)

if st.button("✨ Recommend Properties"):

    recommendations = recommend_properties(selected_property, top_n)

    st.success("✅ Recommendations Generated")

    st.dataframe(recommendations, use_container_width=True)

#footer
st.markdown("---")
st.markdown("<center>🚀 Recommendation Engine | Real Estate ML Project</center>", unsafe_allow_html=True)