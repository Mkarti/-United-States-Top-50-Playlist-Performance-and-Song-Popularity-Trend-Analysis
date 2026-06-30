"""
==========================================================
Data Quality & Coverage

Displays dataset quality indicators for the
Atlantic_United_States dataset.

Version : 1.0
==========================================================
"""

import streamlit as st

from src.metrics import calculate_metrics
from src.constants import (
    ANALYSIS_TYPE,
    STATUS_EXCELLENT,
    STATUS_GOOD,
    STATUS_MODERATE,
)


def render_data_quality(df):
    """
    Render the Data Quality & Coverage panel.
    """

    metrics = calculate_metrics(df)

    st.subheader("🛡️ Data Quality & Coverage")

    # ======================================================
    # Empty Dataset
    # ======================================================

    if metrics["total_records"] == 0:

        st.warning("No data available for the selected filters.")

        return

    # ======================================================
    # Quality Metrics
    # ======================================================

    missing_values = int(df.isna().sum().sum())

    duplicate_rows = int(df.duplicated().sum())

    completeness = round(
        ((df.size - missing_values) / df.size) * 100,
        1
    )

    if "date" in df.columns:

        start_date = df["date"].min().strftime("%d %b %Y")

        end_date = df["date"].max().strftime("%d %b %Y")

        coverage = f"{start_date} → {end_date}"

    else:

        coverage = "Unavailable"

    # ======================================================
    # Validation Status
    # ======================================================

    if completeness == 100 and duplicate_rows == 0:

        status = STATUS_EXCELLENT
        icon = "🟢"

    elif completeness >= 95:

        status = STATUS_GOOD
        icon = "🟡"

    else:

        status = STATUS_MODERATE
        icon = "🟠"

    # ======================================================
    # Quality Cards
    # ======================================================

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Dataset Completeness",
            f"{completeness}%"
        )

        st.metric(
            "Missing Values",
            f"{missing_values:,}"
        )

    with col2:

        st.metric(
            "Duplicate Rows",
            f"{duplicate_rows:,}"
        )

        st.metric(
            "Analysis Type",
            ANALYSIS_TYPE
        )

    with col3:

        st.metric(
            "Date Coverage",
            coverage
        )

        st.metric(
            "Validation Status",
            status
        )

    st.success(
        f"{icon} Dataset Validation: **{status}**"
    )

    st.caption(
        "These indicators describe the quality of the filtered "
        "Atlantic_United_States dataset used for the current analysis."
    )
    
    st.divider()