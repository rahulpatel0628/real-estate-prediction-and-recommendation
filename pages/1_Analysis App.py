import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from wordcloud import WordCloud
import pickle
import seaborn as sns

st.set_page_config(page_title="Real Estate Analytics", layout="wide")

#load data
@st.cache_data
def load_data():
    df = pd.read_csv("data/new_df2.csv")
    df1 = pd.read_csv("data/gurgaon_properties_missing_value_imputation.csv")
    with open('feature_text.pkl', 'rb') as file:
        text = pickle.load(file)
    return df, df1, text

df, df1, text = load_data()


st.markdown("<h1 style='text-align: center; color: #2E86C1;'>🏠 Real Estate Analytics Dashboard</h1>", unsafe_allow_html=True)
st.markdown("---")


st.sidebar.header("🔍 Filters")

selected_sector = st.sidebar.multiselect(
    "Select Sector",
    options=sorted(df['sector'].unique()),
    default=sorted(df['sector'].unique())
)

# Apply filter
filtered_df = df[df['sector'].isin(selected_sector)]

#KPIs
col1, col2, col3 = st.columns(3)

col1.metric("🏘️ Total Sectors", filtered_df.shape[0])
col2.metric("💰 Avg Price/Sqft", f"{filtered_df['price_per_sqft'].mean():,.0f}")
col3.metric("📐 Avg Area", f"{filtered_df['built_up_area'].mean():,.0f} sqft")

st.markdown("---")

#Map
st.subheader("📍 Geographical Price Distribution")

fig = px.scatter_mapbox(
    filtered_df,
    lat='latitude',
    lon='longitude',
    color='price_per_sqft',
    size='built_up_area',
    color_continuous_scale=px.colors.cyclical.IceFire,
    zoom=10,
    mapbox_style='open-street-map',
    text='sector',
    hover_name='sector'
)

st.plotly_chart(fig, use_container_width=True)

#WordCloud
st.markdown("---")
st.subheader("🧠 Feature Insights (Word Cloud)")

wordcloud = WordCloud(
    width=800,
    height=500,
    background_color='white',
    colormap='viridis'
).generate(text)

fig_wc, ax = plt.subplots(figsize=(10, 6))
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis('off')

st.pyplot(fig_wc)

#Area vs Price
st.markdown("---")
st.subheader("📊 Area vs Price Analysis")

col1, col2 = st.columns(2)

property_type = col1.selectbox("Select Property Type", ['flat', 'house'])
sector_area = col2.selectbox("Select Sector", sorted(df1['sector'].unique()))

filtered_df1 = df1[
    (df1['property_type'] == property_type) &
    (df1['sector'] == sector_area)
]

fig1 = px.scatter(
    filtered_df1,
    x='built_up_area',
    y='price',
    color='bedRoom',
    title='Area vs Price'
)

st.plotly_chart(fig1, use_container_width=True)

#BHK Pie Chart
st.markdown("---")
st.subheader("🏠 BHK Distribution")

sector_pie = st.selectbox("Select Sector for BHK Distribution", sorted(df1['sector'].unique()))

fig2 = px.pie(
    df1[df1['sector'] == sector_pie],
    names='bedRoom',
    title="BHK Distribution"
)

st.plotly_chart(fig2, use_container_width=True)

# BHK vs Price
st.markdown("---")
st.subheader("📦 BHK vs Price")

temp_df = df1[df1['bedRoom'] <= 4]

fig3 = px.box(
    temp_df,
    x='bedRoom',
    y='price',
    title='BHK vs Price'
)

st.plotly_chart(fig3, use_container_width=True)

# KDEPlot
st.markdown("---")
st.subheader("📈 Price Distribution (Flat vs House)")

sector_density = st.selectbox("Select Sector for Density Plot", sorted(df1['sector'].unique()))

house = df1[(df1['property_type'] == 'house') & (df1['sector'] == sector_density)]
flat = df1[(df1['property_type'] == 'flat') & (df1['sector'] == sector_density)]

fig4, ax = plt.subplots(figsize=(10, 6))

sns.kdeplot(house['price'], label='House', fill=True)
sns.kdeplot(flat['price'], label='Flat', fill=True)

ax.legend()
ax.set_title("Price Density")

st.pyplot(fig4)

#Insigths
st.markdown("---")
st.subheader("📊 Key Insights")

st.markdown(f"""
- 💡 **Most expensive sector:** {filtered_df.sort_values(by='price_per_sqft', ascending=False)['sector'].iloc[0]}
- 📉 **Most affordable sector:** {filtered_df.sort_values(by='price_per_sqft').iloc[0]['sector']}
- 📈 Price depends on **location, BHK, and area**
- 🏗️ Premium sectors show higher price clusters
""")

# ------------------ FOOTER ------------------
st.markdown("---")
st.markdown("<center>🚀 Built By Rahul Patel| ML Real Estate Project</center>", unsafe_allow_html=True)