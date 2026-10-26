"""Streamlit entry point for the E-CV static website."""
import streamlit as st

st.set_page_config(
    page_title="E-CV Digital — Abdurrazzaq & Afif",
    page_icon="👥",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Hide Streamlit chrome so the embedded portfolio feels like a standalone site.
st.markdown(
    """
    <style>
      #MainMenu, footer, header {visibility: hidden;}
      .block-container {padding: 0 !important; max-width: 100% !important;}
      iframe {border: 0 !important;}
      [data-testid="stAppViewContainer"] > .main {padding: 0 !important;}
      [data-testid="stVerticalBlock"] {gap: 0 !important;}
    </style>
    """,
    unsafe_allow_html=True,
)

# Static files are served by Streamlit when .streamlit/config.toml enables it.
# Keep the site in an iframe to preserve the original HTML/CSS/JS and local asset links.
st.components.v1.iframe("/app/static/index.html", height=5000, scrolling=True)
