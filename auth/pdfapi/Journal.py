from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle
import textwrap

# data = {"from_to": "03/01/2021 to 03/01/2021",
#         "data": [
#
#             {
#                 "date": "03/01/2021",
#                 "trans_type_credit": "Deposit",
#                 "num_credit": "",
#                 "name_credit": "",
#                 "memo_credit": "Opening Balance",
#                 "account_credit": "Cash in bank",
#                 "credit": "23.45",
#                 "memo_debit": "Supplement to the minimum commission for operations",
#                 "account_debit": "Commissions and fees",
#                 "debit": "23.45"
#             },
#             {
#                 "date": "03/02/2021",
#                 "trans_type_credit": "Deposit",
#                 "num_credit": "",
#                 "name_credit": "",
#                 "memo_credit": "Opening Balance",
#                 "account_credit": "Cash in bank",
#                 "credit": "23.45",
#                 "memo_debit": "Supplement to the minimum commission for operations",
#                 "account_debit": "Commissions and fees",
#                 "debit": "23.45"
#             },
#             {
#                 "date": "03/03/2021",
#                 "trans_type_credit": "Deposit",
#                 "num_credit": "",
#                 "name_credit": "",
#                 "memo_credit": "Opening Balance",
#                 "account_credit": "Cash in bank",
#                 "credit": "23.45",
#                 "memo_debit": "Supplement to the minimum commission for operations",
#                 "account_debit": "Commissions and fees",
#                 "debit": "23.45"
#             },
#             {
#                 "date": "03/01/2021",
#                 "trans_type_credit": "Deposit",
#                 "num_credit": "",
#                 "name_credit": "",
#                 "memo_credit": "Opening Balance",
#                 "account_credit": "Cash in bank",
#                 "credit": "23.45",
#                 "memo_debit": "Supplement to the minimum commission for operations",
#                 "account_debit": "Commissions and fees",
#                 "debit": "23.45"
#             },
#             {
#                 "date": "03/02/2021",
#                 "trans_type_credit": "Deposit",
#                 "num_credit": "",
#                 "name_credit": "",
#                 "memo_credit": "Opening Balance",
#                 "account_credit": "Cash in bank",
#                 "credit": "23.45",
#                 "memo_debit": "Supplement to the minimum commission for operations",
#                 "account_debit": "Commissions and fees",
#                 "debit": "23.45"
#             },
#             {
#                 "date": "03/03/2021",
#                 "trans_type_credit": "Deposit",
#                 "num_credit": "",
#                 "name_credit": "",
#                 "memo_credit": "Opening Balance",
#                 "account_credit": "Cash in bank",
#                 "credit": "23.45",
#                 "memo_debit": "Supplement to the minimum commission for operations",
#                 "account_debit": "Commissions and fees",
#                 "debit": "23.45"
#             }, {
#                 "date": "03/01/2021",
#                 "trans_type_credit": "Deposit",
#                 "num_credit": "",
#                 "name_credit": "",
#                 "memo_credit": "Opening Balance",
#                 "account_credit": "Cash in bank",
#                 "credit": "23.45",
#                 "memo_debit": "Supplement to the minimum commission for operations",
#                 "account_debit": "Commissions and fees",
#                 "debit": "23.45"
#             },
#             {
#                 "date": "03/02/2021",
#                 "trans_type_credit": "Deposit",
#                 "num_credit": "",
#                 "name_credit": "",
#                 "memo_credit": "Opening Balance",
#                 "account_credit": "Cash in bank",
#                 "credit": "23.45",
#                 "memo_debit": "Supplement to the minimum commission for operations",
#                 "account_debit": "Commissions and fees",
#                 "debit": "23.45"
#             },
#             {
#                 "date": "03/03/2021",
#                 "trans_type_credit": "Deposit",
#                 "num_credit": "",
#                 "name_credit": "",
#                 "memo_credit": "Opening Balance",
#                 "account_credit": "Cash in bank",
#                 "credit": "23.45",
#                 "memo_debit": "Supplement to the minimum commission for operations",
#                 "account_debit": "Commissions and fees",
#                 "debit": "23.45"
#             },
#             # Add more data objects as needed
#         ]}
import datetime
import textwrap


def wrap_text(text, width):
    wrapped_text = "\n".join(textwrap.wrap(text, width=width, break_long_words=False))
    return wrapped_text


def jour_pdf(file_name, data):
    # Get current date and time
    current_datetime = datetime.datetime.now()

    # Extract date, time, and day
    current_date = current_datetime.date()
    current_time = current_datetime.strftime("%H:%M:%S")
    current_day = current_datetime.strftime("%A")

    # Combine into a single string
    result = f"{current_day}, {current_date},  {current_time}."

    # Print the resul

    doc = SimpleDocTemplate(file_name, pagesize=A4, rightMargin=72, leftMargin=72, topMargin=60, bottomMargin=63)
    styles = getSampleStyleSheet()
    title_style = styles['Heading2']
    heading_style = styles['Heading3']
    paragraph_style = styles['Normal']
    paragraph_style.alignment = 1
    title_style.alignment = 1
    heading_style.alignment = 1  # Center alignment

    # Title
    title = Paragraph("PBCIX", title_style)
    heading = Paragraph("Journal", heading_style)
    dates = Paragraph(f"{data['from_to']}", heading_style)

    elements = []
    t2 = []
    elements.append(title)
    elements.append(heading)
    elements.append(dates)
    elements.append(Spacer(1, 10))
    table_style = TableStyle([
        ('LINEBELOW', (0, 0), (-1, 0), 2, colors.black),  # Customize the top border for the first row
        ('LINEABOVE', (0, 0), (-1, 0), 2, colors.black),  # Customize the bottom border for the first row
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),  # Enable word wrapping for all cells
    ])
    table_style1 = TableStyle([  # Customize the top border for the first row
        # Customize the bottom border for the first row
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 2),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        # Set vertical alignment to 'MIDDLE' for all cells
        # Enable word wrapping for all cells
    ])
    table_style2 = TableStyle([  # Customize the top border for the first row
        # Customize the bottom border for the first row
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 2),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        # Set vertical alignment to 'MIDDLE' for all cells
        # Enable word wrapping for all cells
    ])
    t1 = [
        ['Date', 'TRANSACTION\nTYPE', 'NO.', 'NAME', 'MEMO/\nDESCRIPTION', 'ACCOUNT', 'DEBIT', 'CREDIT'],
    ]
    table1 = Table(t1, colWidths=[60, 70, 40, 80, 120, 80, 60, 60])
    table1.setStyle(table_style)
    elements.append(table1)
    i = 0
    t_debit = 0
    t_credit = 0
    for item in data['data']:
        row = [[
            item.get("date", ""),
            item.get("trans_type_credit", ""),
            item.get("num_credit", ""),
            item.get("name_credit", ""),
            item.get("memo_credit", ""),
            item.get("account_credit", ""),
            '',
            item.get("credit", "") + " ILS"
        ], ]
        row2 = [[
            '',
            '',
            '',
            '',
            wrap_text(item.get("memo_debit", ""), width=16),
            wrap_text(item.get("account_debit", ""), width=11),
            item.get("debit", "") + " ILS",
            ''
        ], ]
        row3 = [[
            '',
            '',
            '',
            '',
            '',
            '',
            item.get("debit", "") + " ILS",
            item.get("credit", "") + " ILS"
        ], ]
        t_debit += float(item.get("debit", ""))
        t_credit += float(item.get("credit", ""))
        table2 = Table(row, colWidths=[60, 70, 40, 80, 120, 80, 60, 60])
        table3 = Table(row2, colWidths=[60, 70, 40, 80, 120, 80, 60, 60])
        table4 = Table(row3, colWidths=[60, 70, 40, 80, 120, 80, 60, 60])
        table2.setStyle(table_style1)
        table3.setStyle(table_style1)
        table4.setStyle(table_style2)
        elements.append(table2)
        elements.append(table3)
        elements.append(table4)
        i = i + 1
        if i % 6 == 0:
            elements.append(Spacer(1, 40))
            elements.append(title)
            elements.append(heading)
            elements.append(dates)
            elements.append(Spacer(1, 10))
            elements.append(table1)

    t2 = [
        ['TOTAL', '', '', '', '', '', f'{round(t_debit, 2)} ILS', f'{round(t_credit, 2)} ILS'],
    ]
    # Create the table with adjusted column widths
    table5 = Table(t2, colWidths=[60, 70, 40, 80, 120, 80, 60, 60])
    # Set style for table cell
    table5.setStyle(table_style)
    elements.append(table5)
    footer_text = f"Accrual Basis {result}"
    footer = Paragraph(footer_text, paragraph_style)

    def add_footer(canvas, doc):
        canvas.saveState()
        canvas.setFont('Helvetica', 9)
        canvas.setFillColor(colors.gray)  # Set the footer color to gray
        footer_x = (doc.width) / 2  # Calculate the x-coordinate to center the footer
        canvas.drawString(footer_x, doc.bottomMargin + 3, footer_text)  # Center the footer at the bottom of the page
        canvas.restoreState()

    doc.build(elements, onFirstPage=add_footer, onLaterPages=add_footer)