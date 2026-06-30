import streamlit as st
import pandas as pd
import plotly.express as px


def render_timeline(df):

    st.subheader("📈 Popularity Trend Over Time")

    # --------------------------
    # Daily Average Popularity
    # --------------------------
    daily_popularity = (
        df.groupby("date")["popularity"]
        .mean()
        .reset_index()
    )

    # --------------------------
    # Rolling Average
    # --------------------------
    daily_popularity["rolling_avg"] = (
        daily_popularity["popularity"]
        .rolling(7)
        .mean()
    )

    # --------------------------
    # Plotly Figure
    # --------------------------
    fig = px.line(
        daily_popularity,
        x="date",
        y="popularity",
        markers=True,
        title="Daily Average Popularity"
    )

    fig.add_scatter(
        x=daily_popularity["date"],
        y=daily_popularity["rolling_avg"],
        mode="lines",
        name="7-Day Rolling Average"
    )

    fig.update_layout(
        height=500,
        hovermode="x unified",
        xaxis_title="Date",
        yaxis_title="Popularity Score"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )