import streamlit as st


def render_sidebar(df):

    st.sidebar.header("🎛 Dashboard Filters")

    # -------------------------
    # Date Range
    # -------------------------
    min_date = df["date"].min().date()
    max_date = df["date"].max().date()

    selected_dates = st.sidebar.date_input(
        "Select Date Range",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date,
    )

    if len(selected_dates) == 2:
        start_date, end_date = selected_dates
    else:
        start_date, end_date = min_date, max_date

    # -------------------------
    # Artist Filter
    # -------------------------
    artists = sorted(df["artist"].dropna().unique())

    selected_artists = st.sidebar.multiselect(
        "Artist",
        artists,
        default=[]
    )

    # -------------------------
    # Album Type
    # -------------------------
    album_types = sorted(df["album_type"].dropna().unique())

    selected_album_types = st.sidebar.multiselect(
        "Album Type",
        album_types,
        default=album_types
    )

    # -------------------------
    # Rank Slider
    # -------------------------
    rank_range = st.sidebar.slider(
        "Playlist Rank",
        min_value=int(df["position"].min()),
        max_value=int(df["position"].max()),
        value=(
            int(df["position"].min()),
            int(df["position"].max())
        )
    )

    # -------------------------
    # Explicit Filter
    # -------------------------
    explicit_options = ["All", "Explicit", "Clean"]

    explicit_choice = st.sidebar.radio(
        "Explicit Content",
        explicit_options
    )

    # -------------------------
    # Apply Filters
    # -------------------------
    filtered_df = df.copy()

    filtered_df = filtered_df[
        (filtered_df["date"].dt.date >= start_date)
        &
        (filtered_df["date"].dt.date <= end_date)
    ]

    filtered_df = filtered_df[
        (filtered_df["position"] >= rank_range[0])
        &
        (filtered_df["position"] <= rank_range[1])
    ]

    filtered_df = filtered_df[
        filtered_df["album_type"].isin(selected_album_types)
    ]

    if selected_artists:
        filtered_df = filtered_df[
            filtered_df["artist"].isin(selected_artists)
        ]

    if explicit_choice == "Explicit":
        filtered_df = filtered_df[
            filtered_df["explicit"] == True
        ]

    elif explicit_choice == "Clean":
        filtered_df = filtered_df[
            filtered_df["explicit"] == False
        ]

    st.sidebar.markdown("---")

    st.sidebar.success(f"{len(filtered_df):,} records")

    return filtered_df

    st.sidebar.divider()

    st.sidebar.caption(
    """
    🎵 Song Analytics Dashboard

    Version 1.0
    """
    )