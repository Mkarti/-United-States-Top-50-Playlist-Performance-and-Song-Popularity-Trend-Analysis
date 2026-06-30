"""
==========================================================
Executive Conclusion

Provides a concise executive conclusion based on the
currently filtered historical playlist dataset.

Version : 1.0
==========================================================
"""

import streamlit as st

from src.metrics import calculate_metrics
from src.constants import (
    HIGH_ARTIST_CONCENTRATION,
    MEDIUM_ARTIST_CONCENTRATION,
    HIGH_POPULARITY,
)


def render_conclusion(df):
    """
    Render the Executive Conclusion section.
    """

    metrics = calculate_metrics(df)

    # ======================================================
    # Empty Dataset
    # ======================================================

    if metrics["total_records"] == 0:
        st.warning("No data available for the selected filters.")
        return

    # ======================================================
    # Dynamic Executive Statements
    # ======================================================

    if metrics["top_artist_share"] >= HIGH_ARTIST_CONCENTRATION:
        artist_summary = (
            "Playlist representation is highly concentrated among a relatively small "
            "group of artists, indicating recurring artist dominance."
        )

    elif metrics["top_artist_share"] >= MEDIUM_ARTIST_CONCENTRATION:
        artist_summary = (
            "Artist representation shows moderate concentration across the selected period."
        )

    else:
        artist_summary = (
            "Artist representation remains well diversified across the selected records."
        )

    if metrics["avg_popularity"] >= HIGH_POPULARITY:
        popularity_summary = (
            "Average popularity remains consistently high, indicating sustained listener engagement."
        )

    else:
        popularity_summary = (
            "Popularity scores display greater variation across the historical observation period."
        )

    if metrics["explicit_pct"] >= 50:
        explicit_summary = (
            "Explicit content represents the majority of playlist entries."
        )

    else:
        explicit_summary = (
            "Explicit and non-explicit tracks remain relatively balanced."
        )

    # ======================================================
    # Executive Conclusion
    # ======================================================

    st.subheader("📌 Executive Conclusion")

    st.success(
        "The following conclusion is automatically generated from the currently "
        "selected historical playlist records."
    )

    st.markdown(
        f"""
### Executive Assessment

The filtered dataset contains **{metrics['total_records']:,}** historical playlist records,
covering **{metrics['unique_songs']:,}** unique songs performed by
**{metrics['unique_artists']:,}** artists.

The most represented artist is **{metrics['top_artist']}**, appearing
**{metrics['top_artist_count']}** times within the selected dataset.

---

### Key Findings

- 🎤 {artist_summary}

- 📈 {popularity_summary}

- 🧩 {explicit_summary}

- 🏆 The highest playlist position observed is **#{metrics['best_rank']}**.

- ⭐ The average popularity score across the filtered dataset is
  **{metrics['avg_popularity']:.1f}**.

---

### Business Interpretation

The historical playlist demonstrates meaningful patterns in artist representation, song popularity, and playlist
composition. These observations provide evidence-based insights into historical streaming performance and support 
strategic evaluation of music market dynamics.

This dashboard is intended exclusively for **historical descriptive analytics**.
No predictive modelling, recommendation systems, forecasting, or causal inference
techniques have been applied.
"""
    )

    st.caption(
        f"""
Dashboard Version: **{metrics['dashboard_version']}** •
Analysis Type: **{metrics['analysis_type']}** •
Generated: **{metrics['generated_on']}**
"""
    )
    