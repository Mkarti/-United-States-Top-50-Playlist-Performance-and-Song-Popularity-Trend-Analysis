import streamlit as st

# ==========================================================
# Components
# ==========================================================

from components.header import render_header
from components.scorecard import render_scorecard
from components.sidebar import render_sidebar
from components.kpis import render_kpis
from components.executive_summary import render_executive_summary
from components.dashboard_insights import render_dashboard_insights
from components.data_quality import render_data_quality
from components.conclusion import render_conclusion

from components.timeline import render_timeline
from components.scatter import render_scatter

from components.leaderboard import render_leaderboard
from components.top_songs import render_top_songs
from components.explicit import render_explicit_analysis

from components.methodology import render_methodology

from components.reports import render_reports

from components.about import render_about

from components.footer import render_footer

# ==========================================================
# Utilities
# ==========================================================

from src.loader import load_data
from src.utils import load_css

# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(
    page_title="Song Analytics Dashboard",
    page_icon="🎵",
    layout="wide"
)

# ==========================================================
# Load Custom CSS
# ==========================================================

load_css()

# ==========================================================
# Load Dataset
# ==========================================================

df = load_data()

# ==========================================================
# Sidebar Filters
# ==========================================================

filtered_df = render_sidebar(df)

# ==========================================================
# Dashboard Tabs
# ==========================================================

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(

[
    "📊 Executive Overview",

    "📈 Historical Trends",

    "🎤 Artist Analysis",

    "📝 Methodology",

    "📄 Reports",

    "ℹ About"

])

# ==========================================================
# TAB 1
# Executive Overview
# ==========================================================

with tab1:

    render_header(filtered_df)

    render_scorecard(filtered_df)

    render_kpis(filtered_df)

    render_executive_summary(filtered_df)

    render_dashboard_insights(filtered_df)
    
    render_data_quality(filtered_df)
    
    render_conclusion(filtered_df)

# ==========================================================
# TAB 2
# Historical Trend Analysis
# ==========================================================

with tab2:

    st.header("📈 Historical Trend Analysis")

    st.markdown("""
This section presents historical playlist behavior over time,
highlighting changes in song popularity, playlist rankings,
and long-term performance patterns.
""")

    st.divider()

    render_timeline(filtered_df)

    st.divider()

    render_scatter(filtered_df)

# ==========================================================
# TAB 3
# Artist & Content
# ==========================================================

with tab3:

    st.header("🎤 Artist & Content")

    st.markdown("""
This section examines artist representation,
track performance, and playlist composition
to identify historical market dominance
and content characteristics.
""")

    st.divider()

    render_leaderboard(filtered_df)

    st.divider()

    render_top_songs(filtered_df)

    st.divider()

    render_explicit_analysis(filtered_df)

# ==========================================================
# TAB 4
# Methodology
# ==========================================================

with tab4:

    render_methodology()

# ==========================================================
# TAB 5
# Reports
# ==========================================================

with tab5:

    render_reports(filtered_df)
    
# ==========================================================
# TAB 6
# About
# ========================================================== 

with tab6:

    render_about()    
    

render_footer()   