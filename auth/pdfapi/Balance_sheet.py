from reportlab.lib import colors, styles
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

# data = {
#     "date": "2023-07-05",
#     "cash_in_bank": 50000,
#     "total_current_assets": 50000,
#     "total_assets": 100000,
#     "net_income": 20000,
#     "opening_balance_equity": 10000,
#     "owner_loan": 5000,
#     "retained_earning": 1000,
#     "total_shareholder_equity": 31000,
#     "total_liabilities_equity": 100000,
#     "today_date_time": "2023-07-05 12:00:00"
# }


def bal_sheet_pdf(buffer, data):
    doc = SimpleDocTemplate(buffer, pagesize=A4, rightMargin=72, leftMargin=72, topMargin=60, bottomMargin=60)
    styles = getSampleStyleSheet()
    title_style = styles['Heading2']
    heading_style = styles['Heading3']
    paragraph_style = styles['Normal']
    paragraph_style.alignment = 1
    title_style.alignment = 1
    heading_style.alignment = 1  # Center alignment

    # Title
    title = Paragraph("PBCIX", title_style)
    heading = Paragraph("Profit and Loss", heading_style)
    dates = Paragraph(f"As of {data['date']}", heading_style)

    elements = []
    elements.append(title)
    elements.append(heading)
    elements.append(dates)
    elements.append(Spacer(1, 10))
    t1 = [
        ['', 'TOTAL'],
    ]
    t2 = [
        ["Assets", ""],
    ]
    t3 = [
        ["Current Assets", ""],
        ["- Cash in Bank", f"{data['cash_in_bank']} ILS"],
        ["Total Current Assets", f"{data['total_current_assets']} ILS"],

    ]
    t4 = [
        ["Total Assets", f"{data['total_assets']} ILS"],
    ]
    t5 = [
        ["Liabilities and Shareholder's Equity", ""],
    ]
    t6 = [
        ['Shareholders Equity', ''],
        ['- Net income', f"{data['net_income']} ILS"],
        ['- Opening Balance Equity', f"{data['opening_balance_equity']} ILS"],
        ["- Owner's Loan", f"{data['owner_loan']} ILS"],
        ['- Retained Earnings', f"{data['retained_earning']} ILS"],
        ["Total Shareholder's Equity", f"{data['total_shareholder_equity']} ILS"],
    ]
    t7 = [

        ['Total Liabilities and Equity', f"{data['total_liabilities_equity']} ILS"],
    ]

    # Create the table with 2 columns and 10 rows
    table1 = Table(t1, colWidths=[240, 240])
    table2 = Table(t2, colWidths=[240, 240])
    table3 = Table(t3, colWidths=[240, 240])
    table4 = Table(t4, colWidths=[240, 240])
    table5 = Table(t5, colWidths=[240, 240])
    table6 = Table(t6, colWidths=[240, 240])
    table7 = Table(t7, colWidths=[240, 240])

    table1.setStyle(TableStyle([
        ('LINEBELOW', (0, 0), (-1, 0), 2, 'black'),
        ('LINEABOVE', (0, 0), (-1, 0), 2, 'black'),
        # Customize the top border for the first row  # Customize the bottom border for the last row
        ('LINEBEFORE', (0, 0), (0, -1), 0, 'white'),  # Hide the left border
        ('LINEAFTER', (-1, 0), (-1, -1), 0, 'white'),  # Hide the right border
        # Align text in the first column (index 0) to the left
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),

        # Align text in the second column (index 1) to the right
        ('ALIGN', (1, 0), (-1, -1), 'RIGHT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    table2.setStyle(TableStyle([
        ('LINEBELOW', (0, 0), (-1, 0), 2, 'black'),
        ('LINEABOVE', (0, 0), (-1, 0), 2, 'black'),
        # Customize the top border for the first row  # Customize the bottom border for the last row
        ('LINEBEFORE', (0, 0), (0, -1), 0, 'white'),  # Hide the left border
        ('LINEAFTER', (-1, 0), (-1, -1), 0, 'white'),  # Hide the right border
        # Align text in the first column (index 0) to the left
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),

        # Align text in the second column (index 1) to the right
        ('ALIGN', (1, 0), (-1, -1), 'RIGHT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))

    # Add customized borders
    table3.setStyle(TableStyle([
        ('LINEBELOW', (0, 0), (-1, 0), 2, colors.lightgrey),
        ('LINEABOVE', (0, 0), (-1, 0), 2, 'black'),  # Customize the top border for the first row
        ('LINEABOVE', (0, -1), (-1, -1), 2, colors.lightgrey),  # Customize the bottom border for the last row
        ('LINEBELOW', (0, -1), (-1, -1), 2, 'black'),  # Customize the bottom border for the last row
        ('LINEBEFORE', (0, 0), (0, -1), 0, 'white'),  # Hide the left border
        ('LINEAFTER', (-1, 0), (-1, -1), 0, 'white'),  # Hide the right border
        # Align text in the first column (index 0) to the left
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),

        # Align text in the second column (index 1) to the right
        ('ALIGN', (1, 0), (-1, -1), 'RIGHT'),
        ('FONTWEIGHT', (0, 1), (-1, -2), 'BOLD'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    table4.setStyle(TableStyle([
        ('LINEBELOW', (0, 0), (-1, 0), 2, 'black'),
        ('LINEABOVE', (0, 0), (-1, 0), 2, 'black'),
        # Customize the top border for the first row  # Customize the bottom border for the last row
        ('LINEBEFORE', (0, 0), (0, -1), 0, 'white'),  # Hide the left border
        ('LINEAFTER', (-1, 0), (-1, -1), 0, 'white'),  # Hide the right border
        # Align text in the first column (index 0) to the left
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),

        # Align text in the second column (index 1) to the right
        ('ALIGN', (1, 0), (-1, -1), 'RIGHT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    table5.setStyle(TableStyle([
        ('LINEBELOW', (0, 0), (-1, 0), 2, 'black'),
        ('LINEABOVE', (0, 0), (-1, 0), 2, 'black'),
        # Customize the top border for the first row  # Customize the bottom border for the last row
        ('LINEBEFORE', (0, 0), (0, -1), 0, 'white'),  # Hide the left border
        ('LINEAFTER', (-1, 0), (-1, -1), 0, 'white'),  # Hide the right border
        # Align text in the first column (index 0) to the left
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),

        # Align text in the second column (index 1) to the right
        ('ALIGN', (1, 0), (-1, -1), 'RIGHT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    table6.setStyle(TableStyle([
        ('LINEBELOW', (0, 0), (-1, 0), 2, colors.lightgrey),
        ('LINEABOVE', (0, 0), (-1, 0), 2, 'black'),  # Customize the top border for the first row
        ('LINEABOVE', (0, -1), (-1, -1), 2, colors.lightgrey),  # Customize the bottom border for the last row
        ('LINEBELOW', (0, -1), (-1, -1), 2, 'black'),  # Customize the bottom border for the last row
        ('LINEBEFORE', (0, 0), (0, -1), 0, 'white'),  # Hide the left border
        ('LINEAFTER', (-1, 0), (-1, -1), 0, 'white'),  # Hide the right border
        # Align text in the first column (index 0) to the left
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),

        # Align text in the second column (index 1) to the right
        ('ALIGN', (1, 0), (-1, -1), 'RIGHT'),
        ('FONTWEIGHT', (0, 1), (-1, -2), 'BOLD'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    table7.setStyle(TableStyle([
        ('LINEBELOW', (0, 0), (-1, 0), 2, 'black'),
        ('LINEABOVE', (0, 0), (-1, 0), 2, 'black'),
        # Customize the top border for the first row  # Customize the bottom border for the last row
        ('LINEBEFORE', (0, 0), (0, -1), 0, 'white'),  # Hide the left border
        ('LINEAFTER', (-1, 0), (-1, -1), 0, 'white'),  # Hide the right border
        # Align text in the first column (index 0) to the left
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),

        # Align text in the second column (index 1) to the right
        ('ALIGN', (1, 0), (-1, -1), 'RIGHT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))

    elements.append(table1)
    elements.append(table2)
    elements.append(table3)
    elements.append(table4)
    elements.append(table5)
    elements.append(table6)
    elements.append(table7)

    footer_text = f"Accrual Basis {data['today_date_time']}"
    footer = Paragraph(footer_text, paragraph_style)

    def add_footer(canvas, doc):
        canvas.saveState()
        canvas.setFont('Helvetica', 9)
        canvas.setFillColor(colors.gray)  # Set the footer color to gray
        footer_x = (doc.width) / 2  # Calculate the x-coordinate to center the footer
        canvas.drawString(footer_x, doc.bottomMargin + 5, footer_text)  # Center the footer at the bottom of the page
        canvas.restoreState()

    doc.build(elements, onFirstPage=add_footer, onLaterPages=add_footer)

