"""
==========================================================
Executive Summary

Displays executive KPI cards together with
automatically generated historical observations.

This component is responsible only for presentation.
==========================================================
"""

import streamlit as st

from src.metrics import calculate_metrics
from src.analytics_engine import generate_executive_insights
from src.utils import executive_card


def render_executive_summary(df):
    """
    Render the Executive Summary section.
    """

    # ======================================================
    # Metrics
    # ======================================================

    metrics = calculate_metrics(df)

    insights = generate_executive_insights(metrics)

    # ======================================================
    # Executive Interpretation
    # ======================================================

    st.success("""
### Strategic Interpretation

The current dashboard summarizes historical playlist performance using descriptive analytics.

The presented metrics and observations support transparent reporting of artist representation,
playlist rankings, song popularity, and content composition.

The analysis is intended for historical evaluation only and does not include predictive modelling,
recommendation systems, or causal inference.
""")
    
    st.divider()