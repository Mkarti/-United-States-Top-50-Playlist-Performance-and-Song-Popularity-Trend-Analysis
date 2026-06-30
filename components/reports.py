"""
==========================================================
Reports Center

Provides downloadable executive reports generated from
the currently filtered historical playlist dataset.

Supported Exports
-----------------
• Microsoft Word (.docx)
• Portable Document Format (.pdf)
• Filtered Dataset (.csv)

Version : 1.0
==========================================================
"""

import streamlit as st

from src.docx_export import export_docx
from src.pdf_export import export_pdf
from src.csv_export import export_csv
from src.metrics import calculate_metrics


def render_reports(df):
    """
    Render the Reports Center.
    """

    metrics = calculate_metrics(df)

    # ======================================================
    # Page Header
    # ======================================================

    st.title("📄 Executive Reports")

    st.markdown(
        """
Generate professional reports based on the **currently selected
historical playlist dataset**.

The exported reports automatically reflect all filters applied
within the dashboard.
"""
    )

    st.divider()

    # ======================================================
    # Empty Dataset
    # ======================================================

    if metrics["total_records"] == 0:

        st.warning(
            "No records are available for the selected filters."
        )

        return

    # ======================================================
    # Report Summary
    # ======================================================

    st.subheader("Current Report Summary")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Playlist Records",
            f"{metrics['total_records']:,}"
        )

    with col2:
        st.metric(
            "Unique Songs",
            f"{metrics['unique_songs']:,}"
        )

    with col3:
        st.metric(
            "Unique Artists",
            f"{metrics['unique_artists']:,}"
        )

    st.divider()

    # ======================================================
    # Word Report
    # ======================================================

    st.subheader("📘 Microsoft Word Report")

    st.caption(
        "Download a professionally formatted executive report "
        "for documentation and stakeholder communication."
    )

    st.download_button(
        label="⬇ Download DOCX Report",
        data=export_docx(df),
        file_name="Executive_Historical_Report.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        use_container_width=True,
    )

    st.divider()

    # ======================================================
    # PDF Report
    # ======================================================

    st.subheader("📕 PDF Report")

    st.caption(
        "Generate a presentation-ready PDF report suitable "
        "for sharing and printing."
    )

    st.download_button(
        label="⬇ Download PDF Report",
        data=export_pdf(df),
        file_name="Executive_Historical_Report.pdf",
        mime="application/pdf",
        use_container_width=True,
    )

    st.divider()

    # ======================================================
    # CSV Export
    # ======================================================

    st.subheader("📊 Filtered Dataset")

    st.caption(
        "Export the currently filtered historical dataset "
        "for additional analysis or archival purposes."
    )

    st.download_button(
        label="⬇ Download CSV Dataset",
        data=export_csv(df),
        file_name="Filtered_Playlist_Dataset.csv",
        mime="text/csv",
        use_container_width=True,
    )

    st.divider()

    # ======================================================
    # Report Information
    # ======================================================

    with st.expander("ℹ About These Reports", expanded=False):

        st.markdown(
            """
### Included in every report

- Executive Summary
- Dataset Overview
- Historical Playlist Metrics
- Key Business Insights
- Executive Conclusion
- Dashboard Metadata
- Methodology Summary
- Disclaimer

All reports are generated dynamically from the currently
selected dashboard filters and reflect the historical data
visible within the application.

The dashboard provides **descriptive historical analytics**
only. No predictive modelling, recommendation systems,
or causal inference techniques have been applied.
"""
        )

    # ======================================================
    # Footer
    # ======================================================

    st.success(
        "All reports have been generated from the current "
        "dashboard filters and are ready for download."
    )