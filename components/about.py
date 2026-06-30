"""
==========================================================
About Component

Displays project information.

Version : 1.0
==========================================================
"""

import streamlit as st


def render_about():
    """
    Render About page.
    """

    st.title("ℹ About this Dashboard")

    st.markdown("""
### Project Objective

This dashboard provides historical descriptive analytics of the United States Top 50 Playlist dataset 
to examine playlist performance, artist representation, popularity trends, and content characteristics.

---

### Technology Stack

- Python
- Streamlit
- Pandas
- NumPy
- Plotly
- ReportLab
- python-docx

---

### Dashboard Features

- Executive Overview
- Historical Trends
- Artist Analysis
- Executive Reports
- Methodology

---

### Analysis Type

Historical Descriptive Analytics

---

### Dashboard Version

**Version 1.0**

---

### Developed By

**Kartikeya Mishra**
""")