"""
==========================================================
Analytics Engine

Generates executive insights from the calculated
dashboard metrics.

This module contains only business interpretation.
No metric calculations should occur here.
==========================================================
"""

from src.constants import (
    HIGH_ARTIST_CONCENTRATION,
    MEDIUM_ARTIST_CONCENTRATION,
    HIGH_POPULARITY,
    LARGE_DATASET,
)


def generate_executive_insights(metrics):
    """
    Generate executive business insights.

    Parameters
    ----------
    metrics : dict
        Output from calculate_metrics().

    Returns
    """

    insights = []

    # ======================================================
    # Empty Dataset
    # ======================================================

    if metrics["total_records"] == 0:

        insights.append(
            "No historical playlist records match the selected filters."
        )

        return insights

    # ======================================================
    # Artist Representation
    # ======================================================

    share = metrics["top_artist_share"]

    if share >= HIGH_ARTIST_CONCENTRATION:

        insights.append(
            f"🎤 Artist representation is highly concentrated. "
            f"**{metrics['top_artist']}** accounts for "
            f"**{share:.1f}%** of playlist appearances."
        )

    elif share >= MEDIUM_ARTIST_CONCENTRATION:

        insights.append(
            "🎤 Artist representation shows moderate concentration, "
            "with several artists appearing consistently throughout "
            "the historical records."
        )

    else:

        insights.append(
            "🎤 Artist representation is well distributed across "
            "multiple artists, indicating a diverse playlist."
        )

    # ======================================================
    # Popularity
    # ======================================================

    popularity = metrics["avg_popularity"]

    if popularity >= HIGH_POPULARITY:

        insights.append(
            f"📈 Average popularity is **{popularity}**, "
            "indicating consistently strong audience engagement."
        )

    else:

        insights.append(
            f"📈 Average popularity is **{popularity}**, "
            "suggesting greater variation across the selected records."
        )

    # ======================================================
    # Explicit Content
    # ======================================================

    explicit = metrics["explicit_pct"]

    if explicit >= 50:

        insights.append(
            f"🧩 Explicit tracks represent **{explicit:.1f}%** "
            "of the playlist."
        )

    else:

        insights.append(
            f"🧩 Explicit content accounts for "
            f"**{explicit:.1f}%** of playlist entries, "
            "remaining below half of the observed records."
        )

    # ======================================================
    # Market Leader
    # ======================================================

    insights.append(
        f"🏆 **{metrics['top_artist']}** appears "
        f"**{metrics['top_artist_count']}** times, "
        "making them the most represented artist "
        "within the filtered dataset."
    )

    # ======================================================
    # Playlist Performance
    # ======================================================

    if metrics["best_rank"] == 1:

        insights.append(
            "🥇 The filtered dataset includes tracks that "
            "reached the #1 playlist position."
        )

    else:

        insights.append(
            f"🥇 The highest playlist position observed "
            f"is **#{metrics['best_rank']}**."
        )

    # ======================================================
    # Artist Productivity
    # ======================================================

    insights.append(
        f"🎵 On average, each artist contributes "
        f"**{metrics['songs_per_artist']}** unique songs "
        "to the filtered historical dataset."
    )

    # ======================================================
    # Dataset Coverage
    # ======================================================

    if metrics["total_records"] >= LARGE_DATASET:

        insights.append(
            "📊 The current selection represents a large historical "
            "sample, supporting long-term trend evaluation."
        )

    else:

        insights.append(
            "📊 The applied filters narrow the historical dataset "
            "to a focused subset for detailed analysis."
        )

    return insights