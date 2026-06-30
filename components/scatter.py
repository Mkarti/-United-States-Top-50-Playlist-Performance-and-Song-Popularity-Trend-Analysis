import streamlit as st
import plotly.express as px


def render_scatter(df):
    selected_artist = st.selectbox(
        "Focus on Artist",
        ["All"] + sorted(df["artist"].unique().tolist())
    )
    
    scatter_df = df.copy()

    if selected_artist != "All":
        scatter_df = scatter_df[
        scatter_df["artist"] == selected_artist
        ]

    st.subheader("🎯 Popularity vs Playlist Rank")

    fig = px.scatter(
        scatter_df,
        x="popularity",
        y="position",
        color="artist",
        hover_name="song",
        size_max=12,
        opacity=0.75,
        trendline="ols",
        title="Popularity vs Playlist Rank"
    )

    fig.update_layout(
        height=600,
        hovermode="closest"
    )

    # Rank 1 should appear at the top
    fig.update_yaxes(autorange="reversed")

    st.plotly_chart(
        fig,
        use_container_width=True
    )