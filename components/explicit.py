import streamlit as st
import pandas as pd
import plotly.express as px


def render_explicit_analysis(df):

    st.subheader("🧩 Explicit Content Analysis")

    col1, col2 = st.columns(2)

    # ------------------------
    # Distribution
    # ------------------------
    explicit_counts = (
        df["is_explicit"]
        .value_counts()
        .reset_index()
    )

    explicit_counts.columns = [
        "Explicit",
        "Count"
    ]

    explicit_counts["Explicit"] = explicit_counts[
        "Explicit"
    ].map({
        True: "Explicit",
        False: "Clean"
    })

    fig1 = px.pie(
        explicit_counts,
        names="Explicit",
        values="Count",
        title="Song Distribution"
    )

    with col1:
        st.plotly_chart(
            fig1,
            use_container_width=True
        )

    # ------------------------
    # Popularity Comparison
    # ------------------------
    popularity_compare = (
        df.groupby("is_explicit")["popularity"]
        .mean()
        .reset_index()
    )

    popularity_compare["is_explicit"] = (
        popularity_compare["is_explicit"]
        .map({
            True: "Explicit",
            False: "Clean"
        })
    )

    fig2 = px.bar(
        popularity_compare,
        x="is_explicit",
        y="popularity",
        title="Average Popularity"
    )

    with col2:
        st.plotly_chart(
            fig2,
            use_container_width=True
        )

    # ------------------------
    # Rank Comparison
    # ------------------------
    rank_compare = (
        df.groupby("is_explicit")["position"]
        .mean()
        .reset_index()
    )

    rank_compare["is_explicit"] = (
        rank_compare["is_explicit"]
        .map({
            True: "Explicit",
            False: "Clean"
        })
    )

    fig3 = px.bar(
        rank_compare,
        x="is_explicit",
        y="position",
        title="Average Playlist Rank"
    )

    fig3.update_yaxes(
        autorange="reversed"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )