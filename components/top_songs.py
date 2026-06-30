import streamlit as st
import pandas as pd
import plotly.express as px


def render_top_songs(df):

    selected_song = st.selectbox(
        "Explore Song",
        sorted(df["song"].unique())
    )

    song_df = df[df["song"] == selected_song]

    st.subheader("🎵 Song Performance Analysis")

    # Global ranking table (ok to keep global)
    song_stats = (
        df.groupby(["song", "artist"])
        .agg(
            Best_Rank=("position", "min"),
            Avg_Popularity=("popularity", "mean"),
            Appearances=("song", "count")
        )
        .reset_index()
        .sort_values("Avg_Popularity", ascending=False)
    )

    top_n = st.slider("Top Songs", 5, 25, 10)

    top_songs = song_stats.head(top_n)

    fig = px.bar(
        top_songs,
        x="Avg_Popularity",
        y="song",
        color="artist",
        orientation="h",
        title="Top Songs by Average Popularity"
    )

    fig.update_layout(height=600)

    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(top_songs, use_container_width=True)

    # Safe metrics
    st.metric(
        "Best Chart Position",
        int(song_df["position"].min()) if not song_df.empty else "N/A"
    )

    st.metric(
        "Average Popularity",
        round(song_df["popularity"].mean(), 1) if not song_df.empty else 0
    )

    st.metric(
        "Days on Playlist",
        len(song_df)
    )