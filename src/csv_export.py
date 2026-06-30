"""
==========================================================
CSV Export

Exports the currently filtered historical playlist dataset
as a CSV file.

This module provides a reusable CSV export function for
the Reports Center.

Version : 1.0
==========================================================
"""

from io import BytesIO
from datetime import datetime

import pandas as pd


def export_csv(df: pd.DataFrame) -> BytesIO:
    """
    Export the filtered dataset as a CSV file.

    Parameters
    ----------
    df : pandas.DataFrame
        Filtered historical playlist dataset.

    Returns
    -------
    BytesIO
        CSV file stored in memory.
    """

    # ======================================================
    # Handle Empty Dataset
    # ======================================================

    if df.empty:

        export_df = pd.DataFrame(
            {
                "Message": [
                    "No records available for the selected filters."
                ]
            }
        )

    else:

        export_df = df.copy()

        # ==================================================
        # Export Metadata
        # ==================================================

        export_df["Analysis Type"] = (
            "Historical Descriptive Analytics"
        )

        export_df["Dashboard Version"] = "1.0"

        export_df["Export Timestamp"] = (
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )

    # ======================================================
    # Convert to CSV
    # ======================================================

    output = BytesIO()

    export_df.to_csv(
        output,
        index=False,
        encoding="utf-8"
    )

    output.seek(0)

    return output