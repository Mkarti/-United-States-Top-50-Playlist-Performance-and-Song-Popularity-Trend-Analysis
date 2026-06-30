import streamlit as st
from pathlib import Path


def load_css():
    css_path = Path(__file__).parent.parent / "assets" / "style.css"

    with open(css_path, "r", encoding="utf-8") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )


def create_kpi_card(title, value, color):

    card = f"""
    <div class="kpi-card" style="background:{color};">
        <div class="kpi-title">{title}</div>
        <div class="kpi-value">{value}</div>
    </div>
    """

    st.markdown(card, unsafe_allow_html=True)
    
def executive_card(title, value, icon):

    st.markdown(
        f"""
        <div style="
        border-left:6px solid #1DB954;
        padding:18px;
        border-radius:10px;
        background:#F8F9FA;
        margin-bottom:15px;
        box-shadow:0px 2px 8px rgba(0,0,0,0.08);
        ">

        <h5 style="margin:0;">
        {icon} {title}
        </h5>

        <h2 style="
        margin-top:10px;
        color:#1DB954;
        ">
        {value}
        </h2>

        </div>
        """,
        unsafe_allow_html=True
    )    