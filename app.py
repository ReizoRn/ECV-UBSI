from pathlib import Path
import re
import base64
import mimetypes
import streamlit as st

st.set_page_config(
    page_title="E-CV Digital — Abdurrazzaq & Afif",
    page_icon="👥",
    layout="wide",
    initial_sidebar_state="collapsed",
)

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

base = Path(__file__).parent
static_dir = base / "static"
html = (static_dir / "index.html").read_text(encoding="utf-8")
css = (static_dir / "style.css").read_text(encoding="utf-8")
js = (static_dir / "script.js").read_text(encoding="utf-8")
html = html.replace('<link rel="stylesheet" href="style.css">', '<style>\n' + css + '\n</style>')
html = html.replace('<script src="script.js" defer></script>', '<script>\n' + js + '\n</script>')

# Embed profile photos directly in the HTML so they load reliably inside the iframe.
def embed_image(match):
    filename = match.group(2)
    path = static_dir / filename
    if not path.is_file():
        return match.group(0)
    mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f'{match.group(1)}="data:{mime};base64,{encoded}"'

html = re.sub(r'(src)=["\'](foto/[^"\']+)["\']', embed_image, html)

# Keep certificate links available through Streamlit static serving.
html = re.sub(
    r'(?P<attr>href)=["\'](sertifikat/[^"\']+)["\']',
    lambda m: f'{m.group("attr")}="/app/static/{m.group(2)}"',
    html,
)

st.iframe(html, height=5000)
