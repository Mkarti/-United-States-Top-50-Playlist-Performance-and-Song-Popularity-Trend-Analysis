"""
==========================================================
PDF Export

Generates a professional Executive PDF Report from the
🎵 Song Analytics Dashboard.

Version : 1.0
==========================================================
"""

from io import BytesIO

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)

from src.report_generator import generate_report


def export_pdf(df):
    """
    Generate Executive PDF Report.
    """

    report = generate_report(df)
    metrics = report["metrics"]

    buffer = BytesIO()

    document = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    title_style = styles["Heading1"]
    title_style.alignment = TA_CENTER

    heading = styles["Heading2"]

    body = styles["BodyText"]

    story = []

    # ======================================================
    # Cover
    # ======================================================

    story.append(
        Paragraph(
            "United States Top 50 Playlist Performance<br/>"
            "& Song Popularity Trend Analysis",
            title_style,
        )
    )

    story.append(Spacer(1, 20))

    story.append(
        Paragraph(
            "<b>Executive Historical Analytics Report</b>",
            styles["Heading2"],
        )
    )

    story.append(
        Paragraph(
            f"Generated On: {report['generated_on']}",
            body,
        )
    )

    story.append(
        Paragraph(
            f"Dashboard Version: {report['dashboard_version']}",
            body,
        )
    )

    story.append(
        Paragraph(
            f"Analysis Type: {report['analysis_type']}",
            body,
        )
    )

    story.append(Spacer(1, 20))

    # ======================================================
    # Executive Summary
    # ======================================================

    story.append(
        Paragraph(
            "1. Executive Summary",
            heading,
        )
    )

    story.append(
        Paragraph(
            report["summary"],
            body,
        )
    )

    story.append(Spacer(1, 18))

    # ======================================================
    # Dataset Metrics
    # ======================================================

    story.append(
        Paragraph(
            "2. Dataset Overview",
            heading,
        )
    )

    table_data = [

        ["Metric", "Value"],

        ["Playlist Records", f"{metrics['total_records']:,}"],

        ["Unique Songs", f"{metrics['unique_songs']:,}"],

        ["Unique Artists", f"{metrics['unique_artists']:,}"],

        ["Average Popularity", f"{metrics['avg_popularity']:.1f}"],

        ["Explicit Songs", f"{metrics['explicit_pct']:.1f}%"],

        ["Best Playlist Rank", f"#{metrics['best_rank']}"],

        ["Top Artist", metrics["top_artist"]],

        ["Artist Share", f"{metrics['top_artist_share']:.1f}%"]

    ]

    table = Table(table_data, colWidths=[220, 180])

    table.setStyle(

        TableStyle(

            [

                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1DB954")),

                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),

                ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),

                ("BACKGROUND", (0, 1), (-1, -1), colors.whitesmoke),

                ("BOTTOMPADDING", (0, 0), (-1, 0), 10),

                ("ALIGN", (0, 0), (-1, -1), "CENTER"),

                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),

            ]

        )

    )

    story.append(table)

    story.append(Spacer(1, 18))

    # ======================================================
    # Business Insights
    # ======================================================

    story.append(
        Paragraph(
            "3. Key Business Insights",
            heading,
        )
    )

    for insight in report["insights"]:

        story.append(
            Paragraph(
                f"• {insight}",
                body,
            )
        )

    story.append(Spacer(1, 18))

    # ======================================================
    # Executive Conclusion
    # ======================================================

    story.append(
        Paragraph(
            "4. Executive Conclusion",
            heading,
        )
    )

    story.append(
        Paragraph(
            report["conclusion"],
            body,
        )
    )

    story.append(Spacer(1, 18))

    # ======================================================
    # Methodology
    # ======================================================

    story.append(
        Paragraph(
            "5. Methodology",
            heading,
        )
    )

    story.append(
        Paragraph(
            "This report is based exclusively on descriptive "
            "historical analytics of the selected playlist records. "
            "The analysis includes playlist rankings, artist "
            "representation, popularity metrics and content "
            "characteristics. No predictive modelling or "
            "recommendation algorithms have been applied.",
            body,
        )
    )

    story.append(Spacer(1, 18))

    # ======================================================
    # Disclaimer
    # ======================================================

    story.append(
        Paragraph(
            "6. Disclaimer",
            heading,
        )
    )

    story.append(
        Paragraph(
            "This report is automatically generated from the "
            "currently filtered dataset and is intended for "
            "historical reporting purposes only.",
            body,
        )
    )

    story.append(Spacer(1, 30))

    # ======================================================
    # Footer
    # ======================================================

    footer = Paragraph(
        "<para align='center'><font size='9'>"
        "Generated by Spotify Historical Analytics Dashboard<br/>"
        "© 2026 Kartikeya Mishra"
        "</font></para>",
        styles["Normal"],
    )

    story.append(footer)

    document.build(story)

    buffer.seek(0)

    return buffer