import streamlit as st
import streamlit.components.v1 as components

# 1. Configure the Streamlit page to utilize the absolute maximum available screen real estate
st.set_page_config(
    page_title="ML with Scikit-Learn — Interactive Learning Lab",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Inject CSS to hide all default Streamlit structural UI elements (header, footer, padding)
st.markdown("""
<style>
    /* Completely eliminate all margins, padding, and borders from Streamlit's container framework */
    [data-testid="stHeader"] { display: none !important; }
    footer { display: none !important; }
    [data-testid="stSidebarCollapseButton"] { display: none !important; }
    
    .main .block-container {
        padding: 0px !important;
        margin: 0px !important;
        max-width: 100% !important;
        height: 100vh !important;
    }
    
    /* Force the element hosting the iframe to occupy 100% viewport dimensions */
    element-container, stHtml {
        width: 100% !important;
        height: 100vh !important;
        margin: 0 !important;
        padding: 0 !important;
    }
    
    iframe {
        width: 100vw !important;
        height: 100vh !important;
        border: none !important;
        display: block !important;
    }
    
    /* Disable double scrollbars on the main application layer */
    html, body, [data-testid="stAppViewContainer"] {
        overflow: hidden !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. Safely read and deliver the raw HTML asset
try:
    with open("ml_sklearn_hub.html", "r", encoding="utf-8") as f:
        html_content = f.read()
except FileNotFoundError:
    st.error("Error: 'ml_sklearn_hub.html' file not found in the current directory.")
    st.stop()

# 4. Render the HTML using the maximum possible height bound to the viewport layout
components.html(
    html_content, 
    height=2500,  # Arbitrarily large fallback height to allow internal HTML scroll bars to take full command
    scrolling=True
)
'''
import streamlit as st

# Set full-width layout and configure tab properties
st.set_page_config(
    page_title="ML with Scikit-Learn — Interactive Learning Lab",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Read the HTML file contents
try:
    with open("ml_sklearn_hub.html", "r", encoding="utf-8") as f:
        html_content = f.read()
except FileNotFoundError:
    st.error("Could not find 'ml_sklearn_hub.html'. Please ensure it is placed in the same directory as this app.py file.")
    st.stop()

# Inject and render the HTML inside a full-width responsive view wrapper
# adjusting scrolling and heights automatically.
st.components.v1.html(
    html_content, 
    height=2000,          # Adjust the layout height (in pixels) depending on content scroll lines
    scrolling=True        # Enables side/vertical scrolling inside the container if it exceeds constraints
)

# Optional styling adjustment to eliminate padding around your native app dashboard canvas layout
st.markdown("""
<style>
    div[data-testid="stSidebarCollapseButton"] { display: none; }
    .main .block-container { padding: 0rem; max-width: 100%; }
    iframe { width: 100% !important; border: none !important; }
</style>
""", unsafe_allow_html=True)
'''
