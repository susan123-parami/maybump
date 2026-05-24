"""
The Four Mes - Streamlit wrapper for the deck.gl/MapLibre/D3 dashboard.

This file is intentionally tiny. The real dashboard is `bump_3d.html`, a
self-contained file that we just embed via Streamlit's HTML component.
Streamlit's role here is hosting and giving us a public URL via Streamlit
Cloud, not data processing.
"""

from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

# ---------- page config ----------
st.set_page_config(
    page_title="The Four Mes - Bump 3D",
    page_icon="🗺️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------- hide Streamlit's default chrome ----------
st.markdown(
    """
    <style>
      #MainMenu, footer, header { visibility: hidden; height: 0; }
      .block-container {
        padding: 0 !important;
        max-width: 100% !important;
      }
      .stApp { background: #0a0a0d; }
      iframe { border: 0; display: block; }
      [data-testid="stToolbar"] { display: none; }
      [data-testid="stDecoration"] { display: none; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- backup download button (top-right, tiny) ----------
# Streamlit components.html() uses a sandboxed iframe, so the in-HTML
# "Download report" link may not work for everyone. Give them a guaranteed
# fallback as a Streamlit-native download button.
pdf_path = Path("report.pdf")
if pdf_path.exists():
    cols = st.columns([10, 1])
    with cols[1]:
        st.download_button(
            label="📄 Report",
            data=pdf_path.read_bytes(),
            file_name="May-Bump-Report.pdf",
            mime="application/pdf",
            help="Download the project report (PDF, 4 pages)",
        )

# ---------- embed the dashboard ----------
html = Path("bump_3d.html").read_text(encoding="utf-8")
components.html(html, height=920, scrolling=False)
