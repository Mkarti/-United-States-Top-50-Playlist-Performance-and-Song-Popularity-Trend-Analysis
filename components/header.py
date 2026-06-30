import streamlit as st


def render_header(df):

    st.title(
    "🎵 United States Top 50 Playlist Analysis\n"
    )

    st.markdown("""
    Analyze playlist trends, artist performance, popularity patterns,
    and streaming insights from the United States Top 50 dataset.
    """)
    
    st.caption(
    """
    🎵 Song Analytics Dashboard

    Dataset: Atlantic_United_States.csv

    Version 1.0
    """
    )

    st.divider()