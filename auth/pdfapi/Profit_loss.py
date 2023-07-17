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

class ProfitLossPDF:
    def __init__(self, file_name, data):
        self.file_name = file_name
        self.data = data

    def generate_report(self):
        current_datetime = datetime.datetime.now()
        current_date = current_datetime.date()
        current_time = current_datetime.strftime("%H:%M:%S")
        current_day = current_datetime.strftime("%A")
        result = f"{current_day}, {current_date},  {current_time}."

        doc = SimpleDocTemplate(
            self.file_name,
            pagesize=A4,
            rightMargin=72,
            leftMargin=72,
            topMargin=60,
            bottomMargin=60
        )
        styles = getSampleStyleSheet()
        title_style = styles['Heading2']
        heading_style = styles['Heading3']
        paragraph_style = styles['Normal']
        paragraph_style.alignment = 1
        title_style.alignment = 1
        heading_style.alignment = 1

        title = Paragraph("PBCIX", title_style)
        heading = Paragraph("Profit and Loss", heading_style)
        dates = Paragraph(f"{self.data['date_from']} - {self.data['date_to']}", heading_style)

        elements = [title, heading, dates, Spacer(1, 10)]

        t1 = [['', 'TOTAL']]
        t2 = [
            ["Income", ""],
            ["- Revenue-General", f"{self.data['revenue_general']} ILS"],
            ["Total Income", f"{self.data['total_income']} ILS"],
        ]
        t3 = [["GROSS PROFIT", f"{self.data['gross_profit']} ILS"]]
        t4 = [
            ["Expenses", ""],
            ["- Commissions and fees", f"{self.data['commissions_and_fees']} ILS"],
            ["- Office expenses", f"{self.data['office_expenses']} ILS"],
            ["- Other selling expenses", f"{self.data['other_selling_expenses']} ILS"],
            ["Total Expenses", f"{self.data['total_expense']} ILS"],
        ]
        t5 = [["NET EARNINGS", f"{self.data['net_earnings']} ILS"]]

        table1 = self.create_table(t1)
        table2 = self.create_table(t2, True)
        table3 = self.create_table(t3)
        table4 = self.create_table(t4, True)
        table5 = self.create_table(t5)

        elements.extend([table1, table2, table3, table4, table5])

        footer_text = f"Accrual Basis {result}"
        footer = Paragraph(footer_text, paragraph_style)

        def add_footer(canvas, doc):
            canvas.saveState()
            canvas.setFont('Helvetica', 9)
            canvas.setFillColor(colors.gray)
            footer_x = (doc.width) / 2
            canvas.drawString(footer_x, doc.bottomMargin + 5, footer_text)
            canvas.restoreState()

        doc.build(elements, onFirstPage=add_footer, onLaterPages=add_footer)

    def create_table(self, data, use_custom_style=False):
        table_style = self.get_table_style(use_custom_style)
        table = Table(data, colWidths=[240, 240])
        table.setStyle(table_style)
        return table

    def get_table_style(self, use_custom_style):
        if use_custom_style:
            return TableStyle([
                ('LINEBELOW', (0, 0), (-1, 0), 2, colors.lightgrey),
                ('LINEABOVE', (0, 0), (-1, 0), 2, 'black'),
                ('LINEABOVE', (0, -1), (-1, -1), 2, colors.lightgrey),
                ('LINEBELOW', (0, -1), (-1, -1), 2, 'black'),
                ('LINEBEFORE', (0, 0), (0, -1), 0, 'white'),
                ('LINEAFTER', (-1, 0), (-1, -1), 0, 'white'),
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('ALIGN', (1, 0), (-1, -1), 'RIGHT'),
                ('FONTWEIGHT', (0, 1), (-1, -2), 'BOLD'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
                ('TOPPADDING', (0, 0), (-1, -1), 6),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
            ])
        else:
            return TableStyle([
                ('LINEBELOW', (0, 0), (-1, 0), 2, 'black'),
                ('LINEABOVE', (0, 0), (-1, 0), 2, 'black'),
                ('LINEBEFORE', (0, 0), (0, -1), 0, 'white'),
                ('LINEAFTER', (-1, 0), (-1, -1), 0, 'white'),
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('ALIGN', (1, 0), (-1, -1), 'RIGHT'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
                ('TOPPADDING', (0, 0), (-1, -1), 6),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
            ])
