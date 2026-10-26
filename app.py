from pathlib import Path
import re
import streamlit as st

st.set_page_config(
    page_title="E-CV Digital — Abdurrazzaq & Afif",
    page_icon="👥",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Rapikan tampilan Streamlit agar website tampil seperti situs mandiri.
st.markdown(
    """<style>
    #MainMenu, footer, header {visibility: hidden;}
    .block-container {padding: 0 !important; max-width: 100% !important;}
    [data-testid="stAppViewContainer"] > .main {padding: 0 !important;}
    [data-testid="stVerticalBlock"] {gap: 0 !important;}
    iframe {border: 0 !important; width: 100% !important;}
    </style>""",
    unsafe_allow_html=True,
)

# Muat HTML, CSS, dan JavaScript ke dalam satu iframe. Ini menghindari
# masalah MIME type ketika index.html diminta langsung dari folder static.
base = Path(__file__).parent
html_path = base / "static" / "index.html"
css_path = base / "static" / "style.css"
js_path = base / "static" / "script.js"

html = html_path.read_text(encoding="utf-8")
css = css_path.read_text(encoding="utf-8")
js = js_path.read_text(encoding="utf-8")
html = html.replace('<link rel="stylesheet" href="style.css">', '<style>\n' + css + '\n</style>')
html = html.replace('<script src="script.js" defer></script>', '<script>\n' + js + '\n</script>')
html = re.sub(
    r'(?P<attr>src|href)=["\'](foto/[^"\']+|sertifikat/[^"\']+)["\']',
    lambda m: f'{m.group("attr")}="/app/static/{m.group(2)}"',
    html,
)

st.iframe(html, height=5000)
