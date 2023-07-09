import textwrap
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, TableStyle, Table
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch


def inv_pdf(data, logo_path, output_path):
    # Load data from JSON object
    name = data.get('from', "")
    business_name = data.get('business_name', "")
    address = data.get('from_address', "")

    # Create the PDF document
    doc = SimpleDocTemplate(output_path, pagesize=A4, rightMargin=20, leftMargin=20, topMargin=0, bottomMargin=0)

    # Define styles
    styles = getSampleStyleSheet()
    logo_style = ParagraphStyle('logo', parent=styles['Normal'], fontSize=8)
    data_style = ParagraphStyle('data', parent=styles['Normal'], fontSize=12)

    # Create the story (elements to be added to the PDF)
    story = []

    # Add logo to the top right corner
    logo = Image(logo_path, width=1.0 * inch, height=1.0 * inch)
    logo.hAlign = 'RIGHT'
    story.append(logo)

    t1 = [
        [f"From: {name}"],

    ]
    t2 = [
        [f"Business Name: {business_name}"],

    ]
    paragraph_style = ParagraphStyle(
        'CustomParagraphStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        spaceAfter=2,
        alignment=0,
        textColor=colors.black,
        leading=18,
    )
    t3 = [
        [Paragraph(address, paragraph_style)],
    ]
    table_style1 = TableStyle([  # Customize the top border for the first row
        # Customize the bottom border for the first row
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 2),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),

        # Set vertical alignment to 'MIDDLE' for all cells
        # Enable word wrapping for all cells
    ])
    table_style3 = TableStyle([  # Customize the top border for the first row
        # Customize the bottom border for the first row
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, 0), 11),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 2),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),

        # Set vertical alignment to 'MIDDLE' for all cells
        # Enable word wrapping for all cells
    ])

    table_style2 = TableStyle([  # Customize the top border for the first row
        # Customize the bottom border for the first row
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 14),
        ('TOPPADDING', (0, 0), (-1, 0), 6),
        ('ALIGN', (0, 0), (-1, -1), 'RIGHT'),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('BACKGROUND', (0, 0), (-1, -1), colors.lightgrey),
        # Set vertical alignment to 'MIDDLE' for all cells
        # Enable word wrapping for all cells
    ])
    # Add data to the left side
    table1 = Table(t1, colWidths=280)
    table2 = Table(t2, colWidths=280)
    table3 = Table(t3, colWidths=200)
    table1.setStyle(table_style1)
    table2.setStyle(table_style1)
    table2.hAlign = 'LEFT'
    table3.setStyle(table_style1)
    table3.hAlign = 'LEFT'
    table1.hAlign = 'LEFT'

    story.append(table1)
    story.append(table2)
    story.append(table3)
    story.append(Spacer(1, 0.20 * inch))
    t4 = [
        ['INVOICE         '],
    ]
    t5 = [
        [f"Bill to: {data['bill_to']}", "INVOICE #", f"{data['invoice_no']}"],

    ]
    t6 = [[f"Attn: {data['att']}", "DATE", f"{data['date']}"], ]
    t7 = [
        [f"{data['company_name']}", "DUE DATE", f"{data['due_date']}"],
    ]
    t8 = [["", "TOTAL AMOUNT", f"${data['total_amount']}"],
          ]
    t9 = [["", "TOTAL DUE AMOUNT", f"{data['due_amount']}"], ]
    table4 = Table(t4, colWidths=550)
    table4.setStyle(table_style2)
    table4.hAlign = 'CENTRE'
    story.append(table4)
    story.append(Spacer(1, 0.20 * inch))
    table5 = Table(t5, colWidths=[330, 120, 100])
    table5.setStyle(table_style1)
    story.append(table5)
    table6 = Table(t6, colWidths=[330, 120, 100])
    table6.setStyle(table_style1)
    story.append(table6)
    table7 = Table(t7, colWidths=[330, 120, 100])
    table7.setStyle(table_style1)
    story.append(table7)
    table8 = Table(t8, colWidths=[330, 120, 100])
    table8.setStyle(table_style1)
    story.append(table8)
    table9 = Table(t9, colWidths=[330, 120, 100])
    table9.setStyle(table_style1)
    story.append(table9)
    story.append(Spacer(1, 0.20 * inch))
    table_style10 = TableStyle([
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 11),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LINEBELOW', (0, 0), (-1, -1), 0.1, colors.lightgrey),
        ('LINEABOVE', (0, 0), (-1, -1), 0.1, colors.lightgrey),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
        ('TOPPADDING', (0, 0), (-1, 0), 10),
        ('GRID', (0, 0), (-1, -1), 0.1, colors.lightgrey),
    ])
    t10 = [
        ["DESCIPTION/MEMO", "AMOUNT"],
    ]
    paragraph_style1 = ParagraphStyle(
        'CustomParagraphStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=11,
        spaceAfter=2,
        alignment=0,
        textColor=colors.black,
        leading=18,
    )
    table10 = Table(t10, colWidths=[410, 100])
    table10.setStyle(table_style10)
    table10.hAlign = 'CENTRE'
    story.append(table10)

    for item in data['Purchase_details']:
        row = [[
            Paragraph(item.get("descipt_memo", ""), paragraph_style1),
            item.get("amount", ""),
        ]]
        table10 = Table(row, colWidths=[410, 100])
        table10.setStyle(table_style10)
        table10.hAlign = 'CENTRE'
        story.append(table10)

    row1 = [
        ["TOTAL AMOUNT:", f"${data['total_amount']}"]
    ]
    table10 = Table(row1, colWidths=[410, 100])
    table10.setStyle(table_style10)
    table10.hAlign = 'CENTRE'
    story.append(table10)
    story.append(Spacer(1, 1.0 * inch))
    tx = [['Remit to:'],
          [Paragraph(data['remit_to'], paragraph_style)]]
    tablex = Table(tx, colWidths=100)
    tablex.setStyle(table_style3)
    tablex.hAlign = 'RIGHT'
    story.append(tablex)
    doc.build(story)