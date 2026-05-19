import streamlit as st
import streamlit.components.v1 as components

# Page config
st.set_page_config(
    page_title="ML with Scikit-Learn — Interactive Learning Lab",
    layout="wide",
    page_icon="📈"
)

# Title (optional)
st.title("⚡ AI & ML Visual Learning Platform (CBSE XII)")

# Read your HTML file
with open("ml_sklearn_hub.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Render HTML inside Streamlit
components.html(html_content, height=900, scrolling=True)


