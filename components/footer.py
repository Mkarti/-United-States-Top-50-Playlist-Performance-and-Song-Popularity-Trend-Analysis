"""
==========================================================
Footer Component

Reusable dashboard footer.

Author : Kartikeya Mishra
Version : 1.0
==========================================================
"""

import streamlit as st


def render_footer():

    st.divider()

    st.markdown(
        """
<div style="text-align:center;color:gray;font-size:14px;">

<b>United States Top 50 Playlist Performance & Song Popularity Trend Analysis</b>

🎵 Song Analytics Dashboard

Version <b>1.0</b>

Developed by <b>Kartikeya Mishra</b>

</div>
""",
        unsafe_allow_html=True,
    )