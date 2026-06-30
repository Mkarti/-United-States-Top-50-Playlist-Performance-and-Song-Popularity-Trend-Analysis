import streamlit as st

from src.metrics import calculate_metrics
from src.analytics_engine import generate_executive_insights


def render_dashboard_insights(df):

    metrics = calculate_metrics(df)

    insights = generate_executive_insights(metrics)

    st.subheader("💡 Key Business Insights")

    for i, insight in enumerate(insights, start=1):
        st.info(f"Insight {i}\n\n{insight}")
        
    st.divider()    