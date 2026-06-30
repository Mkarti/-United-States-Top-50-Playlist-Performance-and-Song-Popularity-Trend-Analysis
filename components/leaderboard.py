import streamlit as st
import pandas as pd
import plotly.express as px


def render_leaderboard(df):

    st.subheader("🎤 Artist Leaderboard")

    artist_stats = (
        df.groupby("artist")
        .agg(
            Appearances=("artist", "count"),
            Avg_Popularity=("popularity", "mean"),
            Best_Rank=("position", "min")
        )
        .reset_index()
    )

    artist_stats = artist_stats.sort_values(
        "Appearances",
        ascending=False
    )

    top_n = st.slider(
        "Select Top Artists",
        5,
        25,
        10
    )
    
    top_artists = artist_stats.head(top_n)

    fig = px.bar(
        top_artists,
        x="Appearances",
        y="artist",
        orientation="h",
        color="Avg_Popularity",
        title="Top 10 Artists by Playlist Appearances"
    )

    fig.update_layout(
        height=500,
        yaxis=dict(categoryorder="total ascending")
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.dataframe(
        top_artists,
        use_container_width=True
    )