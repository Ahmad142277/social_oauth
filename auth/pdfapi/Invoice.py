import textwrap
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, TableStyle, Table
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch


class InvoicePDF:
    def __init__(self, logo_path, output_path):
        self.logo_path = logo_path
        self.output_path = output_path
        self.styles = getSampleStyleSheet()
        self.paragraph_style = ParagraphStyle(
            'CustomParagraphStyle',
            parent=self.styles['Normal'],
            fontName='Helvetica',
            fontSize=10,
            spaceAfter=2,
            alignment=0,
            textColor=colors.black,
            leading=18,
        )
        self.table_style1 = TableStyle([
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, 0), 10),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 2),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ])
        self.table_style2 = TableStyle([
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, 0), 14),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 14),
            ('TOPPADDING', (0, 0), (-1, 0), 6),
            ('ALIGN', (0, 0), (-1, -1), 'RIGHT'),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
            ('BACKGROUND', (0, 0), (-1, -1), colors.lightgrey),
        ])
        self.table_style3 = TableStyle([
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, 0), 11),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 2),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ])
        self.table_style10 = TableStyle([
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

    def wrap_text(self, text, width):
        wrapped_text = "\n".join(textwrap.wrap(text, width=width, break_long_words=False))
        return wrapped_text

    def create_table(self, data, table_style, story):
        table = Table(data, colWidths=[330, 120, 100])
        table.setStyle(table_style)
        story.append(table)
        return table

    def create_invoice_pdf(self, data):
        name = data.get('from', "")
        business_name = data.get('business_name', "")
        address = data.get('from_address', "")

        doc = SimpleDocTemplate(self.output_path, pagesize=A4, rightMargin=20, leftMargin=20, topMargin=0,
                                bottomMargin=0)
        story = []

        logo = Image(self.logo_path, width=1.0 * inch, height=1.0 * inch)
        logo.hAlign = 'RIGHT'
        story.append(logo)

        t1 = [[f"From: {name}"]]
        t2 = [[f"Business Name: {business_name}"]]
        t3 = [[Paragraph(address, self.paragraph_style)]]

        table1 = Table(t1, colWidths=280)
        table2 = Table(t2, colWidths=280)
        table3 = Table(t3, colWidths=200)
        table1.setStyle(self.table_style1)
        table2.setStyle(self.table_style1)
        table2.hAlign = 'LEFT'
        table3.setStyle(self.table_style1)
        table3.hAlign = 'LEFT'
        table1.hAlign = 'LEFT'

        story.append(table1)
        story.append(table2)
        story.append(table3)
        story.append(Spacer(1, 0.20 * inch))

        t4 = [['INVOICE         ']]
        t5 = [[f"Bill to: {data['bill_to']}", "INVOICE #", f"{data['invoice_no']}"]]
        t6 = [[f"Attn: {data['att']}", "DATE", f"{data['date']}"]]
        t7 = [[f"{data['company_name']}", "DUE DATE", f"{data['due_date']}"]]
        t8 = [["", "TOTAL AMOUNT", f"${data['total_amount']}"]]
        t9 = [["", "TOTAL DUE AMOUNT", f"{data['due_amount']}"]]

        table4 = Table(t4, colWidths=550)
        table4.setStyle(self.table_style2)
        table4.hAlign = 'CENTRE'
        story.append(table4)
        story.append(Spacer(1, 0.20 * inch))

        self.create_table(t5, self.table_style1, story)
        self.create_table(t6, self.table_style1, story)
        self.create_table(t7, self.table_style1, story)
        self.create_table(t8, self.table_style1, story)
        self.create_table(t9, self.table_style1, story)
        story.append(Spacer(1, 0.20 * inch))

        t10 = [["DESCIPTION/MEMO", "AMOUNT"]]
        table10 = Table(t10, colWidths=[410, 100])
        table10.setStyle(self.table_style10)
        table10.hAlign = 'CENTRE'
        story.append(table10)

        for item in data['Purchase_details']:
            row = [[
                Paragraph(item.get("descipt_memo", ""), self.paragraph_style),
                item.get("amount", ""),
            ]]
            table10 = Table(row, colWidths=[410, 100])
            table10.setStyle(self.table_style10)
            table10.hAlign = 'CENTRE'
            story.append(table10)

        row1 = [["TOTAL AMOUNT:", f"${data['total_amount']}"]]
        table10 = Table(row1, colWidths=[410, 100])
        table10.setStyle(self.table_style10)
        table10.hAlign = 'CENTRE'
        story.append(table10)
        story.append(Spacer(1, 1.0 * inch))

        tx = [['Remit to:'], [Paragraph(data['remit_to'], self.paragraph_style)]]
        tablex = Table(tx, colWidths=100)
        tablex.setStyle(self.table_style3)
        tablex.hAlign = 'RIGHT'
        story.append(tablex)

        doc.build(story)