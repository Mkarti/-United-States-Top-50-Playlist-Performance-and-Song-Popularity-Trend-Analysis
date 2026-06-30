"""
==========================================================
Executive Scorecard

Provides a high-level executive overview of the filtered
historical playlist dataset.

Version : 1.0
==========================================================
"""

import streamlit as st

from src.metrics import calculate_metrics
from src.constants import (
    STATUS_EXCELLENT,
    STATUS_GOOD,
    STATUS_MODERATE,
)


def render_scorecard(df):
    """
    Render the Executive Scorecard.
    """

    metrics = calculate_metrics(df)

    st.subheader("📊 Executive Scorecard")

    # ======================================================
    # Empty Dataset
    # ======================================================

    if metrics["total_records"] == 0:

        st.warning("No data available for the selected filters.")

        return

    # ======================================================
    # Dataset Status
    # ======================================================

    if metrics["total_records"] >= 20000:

        status = STATUS_EXCELLENT
        status_icon = "🟢"

    elif metrics["total_records"] >= 10000:

        status = STATUS_GOOD
        status_icon = "🟡"

    else:

        status = STATUS_MODERATE
        status_icon = "🟠"

    # ======================================================
    # Scorecard
    # ======================================================

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "📂 Playlist Records",
            f"{metrics['total_records']:,}"
        )

        st.metric(
            "🎵 Unique Songs",
            f"{metrics['unique_songs']:,}"
        )

    with col2:

        st.metric(
            "🎤 Unique Artists",
            f"{metrics['unique_artists']:,}"
        )

        st.metric(
            "⭐ Avg Popularity",
            f"{metrics['avg_popularity']:.1f}"
        )

    with col3:

        st.metric(
            "🏆 Best Rank",
            f"#{metrics['best_rank']}"
        )

        st.metric(
            "🧩 Explicit Content",
            f"{metrics['explicit_pct']:.1f}%"
        )

    st.success(
        f"{status_icon} Overall Dataset Status: **{status} Historical Coverage**"
    )
    
    st.divider()