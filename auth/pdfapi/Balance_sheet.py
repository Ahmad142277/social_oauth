import datetime

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


import datetime
from reportlab.lib import colors, styles
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


class BalSheetPDF:
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
        dates = Paragraph(f"As of {self.data['date']}", heading_style)

        elements = [title, heading, dates, Spacer(1, 10)]

        t1 = [['', 'TOTAL'], ]

        t2 = [["Assets", ""], ]

        t3 = [["Current Assets", ""],
              ["- Cash in Bank", f"{self.data['cash_in_bank']} ILS"],
              ["Total Current Assets", f"{self.data['total_current_assets']} ILS"], ]

        t4 = [["Total Assets", f"{self.data['total_assets']} ILS"], ]

        t5 = [["Liabilities and Shareholder's Equity", ""], ]

        t6 = [['Shareholders Equity', ''],
              ['- Net income', f"{self.data['net_income']} ILS"],
              ['- Opening Balance Equity', f"{self.data['opening_balance_equity']} ILS"],
              ["- Owner's Loan", f"{self.data['owner_loan']} ILS"],
              ['- Retained Earnings', f"{self.data['retained_earning']} ILS"],
              ["Total Shareholder's Equity", f"{self.data['total_shareholder_equity']} ILS"], ]

        t7 = [['Total Liabilities and Equity', f"{self.data['total_liabilities_equity']} ILS"], ]
        table1 = self.create_table(t1)
        table2 = self.create_table(t2)
        table3 = self.create_table(t3, True)
        table4 = self.create_table(t4)
        table5 = self.create_table(t5)
        table6 = self.create_table(t6, True)
        table7 = self.create_table(t7)
        elements.extend([table1, table2, table3, table4, table5, table6, table7])

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


# # Usage example
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

# report = BalSheetPDF("profit_loss_report.pdf", data)
# report.generate_report()
