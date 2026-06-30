"""
==========================================================
Metrics Engine

Centralized business metrics used throughout the
🎵 Song Analytics Dashboard.

This module acts as the single source of truth for
all historical playlist calculations.
==========================================================
"""

from datetime import datetime


def calculate_metrics(df):
    """
    Calculate all business metrics required by the dashboard.

    Parameters
    ----------
    df : pandas.DataFrame
        Filtered playlist dataset.

    Returns
    -------
    dict
        Dictionary containing business metrics and metadata.
    """

    # ======================================================
    # Metadata
    # ======================================================

    metadata = {
        "analysis_type": "Historical Descriptive Analytics",
        "dashboard_version": "1.0",
        "generated_by": "🎵 Song Analytics Dashboard",
        "generated_on": datetime.now().strftime("%d %B %Y, %H:%M"),
    }

    # ======================================================
    # Empty Dataset Handling
    # ======================================================

    if df.empty:

        return {

            # Dataset
            "total_records": 0,
            "unique_songs": 0,
            "unique_artists": 0,

            # Playlist Performance
            "avg_popularity": 0.0,
            "best_rank": None,

            # Content
            "explicit_pct": 0.0,

            # Artist Representation
            "top_artist": "N/A",
            "top_artist_count": 0,
            "top_artist_share": 0.0,
            "songs_per_artist": 0.0,

            # Metadata
            **metadata
        }

    # ======================================================
    # Dataset Metrics
    # ======================================================

    total_records = len(df)

    unique_songs = df["song"].nunique()

    unique_artists = df["artist"].nunique()

    # ======================================================
    # Playlist Performance
    # ======================================================

    avg_popularity = round(
        df["popularity"].mean(),
        1
    )

    best_rank = int(
        df["position"].min()
    )

    # ======================================================
    # Explicit Content
    # ======================================================

    explicit_pct = round(
        df["is_explicit"].mean() * 100,
        1
    )

    # ======================================================
    # Artist Representation
    # ======================================================

    artist_counts = df["artist"].value_counts()

    top_artist = artist_counts.index[0]

    top_artist_count = int(
        artist_counts.iloc[0]
    )

    top_artist_share = round(
        (
            top_artist_count /
            total_records
        ) * 100,
        1
    )

    songs_per_artist = round(
        unique_songs /
        unique_artists,
        2
    )

    # ======================================================
    # Metrics Dictionary
    # ======================================================

    metrics = {

        # -------------------------------
        # Dataset
        # -------------------------------

        "total_records": total_records,

        "unique_songs": unique_songs,

        "unique_artists": unique_artists,

        # -------------------------------
        # Playlist Performance
        # -------------------------------

        "avg_popularity": avg_popularity,

        "best_rank": best_rank,

        # -------------------------------
        # Content
        # -------------------------------

        "explicit_pct": explicit_pct,

        # -------------------------------
        # Artist Representation
        # -------------------------------

        "top_artist": top_artist,

        "top_artist_count": top_artist_count,

        "top_artist_share": top_artist_share,

        "songs_per_artist": songs_per_artist,

        # -------------------------------
        # Metadata
        # -------------------------------

        **metadata
    }

    return metrics