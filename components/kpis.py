import streamlit as st
from src.utils import create_kpi_card


def render_kpis(df):

    # -----------------------------
    # Calculate KPIs
    # -----------------------------
    total_records = len(df)

    total_tracks = df["song"].nunique()

    total_artists = df["artist"].nunique()

    avg_popularity = (
        round(df["popularity"].mean(), 1)
        if not df.empty
        else 0
    )

    best_rank = (
        int(df["position"].min())
        if not df.empty
        else 0
    )

    explicit_pct = (
        round((df["is_explicit"].sum() / len(df)) * 100, 1)
        if len(df) > 0
        else 0
    )

    # -----------------------------
    # Dashboard Title
    # -----------------------------
    st.subheader("📊 Dashboard KPIs")

    c1, c2, c3 = st.columns(3)

    with c1:
        create_kpi_card(
            "Total Songs",
            total_tracks,
            "#1DB954"
        )

    with c2:
        create_kpi_card(
            "Artists",
            total_artists,
            "#191414"
        )

    with c3:
        create_kpi_card(
            "Average Popularity",
            avg_popularity,
            "#2D2D2D"
        )

    st.write("")

    c4, c5, c6 = st.columns(3)

    with c4:
        create_kpi_card(
            "Best Rank",
            f"#{best_rank}",
            "#0E7490"
        )

    with c5:
        create_kpi_card(
            "Explicit Songs",
            f"{explicit_pct}%",
            "#8B5CF6"
        )

    with c6:
        create_kpi_card(
            "Total Records",
            f"{total_records:,}",
            "#EF4444"
        )
    
    st.divider()    