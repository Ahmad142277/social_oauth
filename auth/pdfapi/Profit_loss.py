import datetime

from reportlab.lib import colors, styles
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

# data = {
#     'date_from': '2023-01-01',
#     'date_to': '2023-12-31',
#     'revenue_general': 50000,
#     'total_income': 50000,
#     'gross_profit': 30000,
#     'commissions_and_fees': 10000,
#     'office_expenses': 8000,
#     'other_selling_expenses': 2000,
#     'total_expense': 20000,
#     'net_earnings': 10000,
#     'today_date_time': '2023-07-05 12:00:00'
# }


def pro_loss_pdf(file_name, data):
    current_datetime = datetime.datetime.now()

    # Extract date, time, and day
    current_date = current_datetime.date()
    current_time = current_datetime.strftime("%H:%M:%S")
    current_day = current_datetime.strftime("%A")

    # Combine into a single string
    result = f"{current_day}, {current_date},  {current_time}."

    doc = SimpleDocTemplate(file_name, pagesize=A4, rightMargin=72, leftMargin=72, topMargin=60, bottomMargin=60)
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
    dates = Paragraph(f"{data['date_from']} - {data['date_to']}", heading_style)

    elements = []
    elements.append(title)
    elements.append(heading)
    elements.append(dates)
    elements.append(Spacer(1, 10))
    t1 = [
        ['', 'TOTAL'],
    ]
    t2 = [

        ["Income", ""],
        ["- Revenue-General", f"{data['revenue_general']} ILS"],
        ["Total Income", f"{data['total_income']} ILS"],
    ]
    t3 = [
        ["GROSS PROFIT", f"{data['gross_profit']} ILS"],
    ]
    t4 = [
        ["Expenses", ""],
        ["- Commissions and fees", f"{data['commissions_and_fees']} ILS"],
        ["- Office expenses", f"{data['office_expenses']} ILS"],
        ["- Other selling expenses", f"{data['other_selling_expenses']} ILS"],
        ["Total Expenses", f"{data['total_expense']} ILS"],
    ]
    t5 = [
        ["NET EARNINGS", f"{data['net_earnings']} ILS"],
    ]

    # Create the table with 2 columns and 10 rows
    table1 = Table(t1, colWidths=[240, 240])
    table2 = Table(t2, colWidths=[240, 240])
    table3 = Table(t3, colWidths=[240, 240])
    table4 = Table(t4, colWidths=[240, 240])
    table5 = Table(t5, colWidths=[240, 240])

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

    # Add customized borders
    table2.setStyle(TableStyle([
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
    table3.setStyle(TableStyle([
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
    table4.setStyle(TableStyle([
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

    elements.append(table1)
    elements.append(table2)
    elements.append(table3)
    elements.append(table4)
    elements.append(table5)
    footer_text = f"Accrual Basis {result}"
    footer = Paragraph(footer_text, paragraph_style)

    def add_footer(canvas, doc):
        canvas.saveState()
        canvas.setFont('Helvetica', 9)
        canvas.setFillColor(colors.gray)  # Set the footer color to gray
        footer_x = (doc.width) / 2  # Calculate the x-coordinate to center the footer
        canvas.drawString(footer_x, doc.bottomMargin + 5, footer_text)  # Center the footer at the bottom of the page
        canvas.restoreState()

    doc.build(elements, onFirstPage=add_footer, onLaterPages=add_footer)


