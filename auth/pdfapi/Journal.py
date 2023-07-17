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


class JournalPDF:
    def __init__(self, file_name, data):
        self.file_name = file_name
        self.data = data
        self.doc = SimpleDocTemplate(
            self.file_name,
            pagesize=A4,
            rightMargin=72,
            leftMargin=72,
            topMargin=60,
            bottomMargin=63
        )
        self.styles = getSampleStyleSheet()
        self.table_style1 = TableStyle([
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.black),
            ('LINEABOVE', (0, 0), (-1, 0), 2, colors.black),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 9),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ])
        self.table_style2 = TableStyle([
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, 0), 9),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 2),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ])
        self.table_style3 = TableStyle([
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 9),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 2),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ])

    def wrap_text(self, text, width):
        wrapped_text = "\n".join(textwrap.wrap(text, width=width, break_long_words=False))
        return wrapped_text

    def create_title(self):
        title_style = self.styles['Heading2']
        title_style.alignment = 1
        title = Paragraph("PBCIX", title_style)
        return title

    def create_heading(self):
        heading_style = self.styles['Heading3']
        heading_style.alignment = 1
        heading = Paragraph("Journal", heading_style)
        return heading

    def create_dates(self):
        heading_style = self.styles['Heading3']
        heading_style.alignment = 1
        dates = Paragraph(f"{self.data['from_to']}", heading_style)
        return dates

    def create_table(self):

        t1 = [['Date', 'TRANSACTION\nTYPE', 'NO.', 'NAME', 'MEMO/\nDESCRIPTION', 'ACCOUNT', 'DEBIT', 'CREDIT']]
        table1 = Table(t1, colWidths=[60, 70, 40, 80, 120, 80, 60, 60])
        table1.setStyle(self.table_style1)
        return table1

    def create_row(self, item):
        row = [
            [item.get("date", ""),
             item.get("trans_type_credit", ""),
             item.get("num_credit", ""),
             item.get("name_credit", ""),
             item.get("memo_credit", ""),
             item.get("account_credit", ""),
             '',
             item.get("credit", "") + " ILS"]
        ]
        row2 = [
            ['', '', '', '', self.wrap_text(item.get("memo_debit", ""), width=16),
             self.wrap_text(item.get("account_debit", ""), width=11), item.get("debit", "") + " ILS", '']
        ]
        row3 = [
            ['', '', '', '', '', '', item.get("debit", "") + " ILS", item.get("credit", "") + " ILS"]
        ]
        table2 = Table(row, colWidths=[60, 70, 40, 80, 120, 80, 60, 60])
        table3 = Table(row2, colWidths=[60, 70, 40, 80, 120, 80, 60, 60])
        table4 = Table(row3, colWidths=[60, 70, 40, 80, 120, 80, 60, 60])

        table2.setStyle(self.table_style2)
        table3.setStyle(self.table_style2)
        table4.setStyle(self.table_style3)
        return [table2, table3, table4]

    def create_total_row(self, t_debit, t_credit):
        t2 = [['TOTAL', '', '', '', '', '', f'{round(t_debit, 2)} ILS', f'{round(t_credit, 2)} ILS']]
        table5 = Table(t2, colWidths=[60, 70, 40, 80, 120, 80, 60, 60])

        table5.setStyle(self.table_style1)
        return table5

    def create_footer(self):
        paragraph_style = self.styles['Normal']
        paragraph_style.alignment = 1
        current_datetime = datetime.datetime.now()
        current_date = current_datetime.date()
        current_time = current_datetime.strftime("%H:%M:%S")
        current_day = current_datetime.strftime("%A")
        result = f"{current_day}, {current_date},  {current_time}."
        footer_text = f"Accrual Basis {result}"
        footer = Paragraph(footer_text, paragraph_style)
        return footer

    def add_footer(self, canvas, doc):
        canvas.saveState()
        canvas.setFont('Helvetica', 9)
        canvas.setFillColor(colors.gray)
        footer_x = (doc.width) / 2
        canvas.drawString(footer_x, doc.bottomMargin + 3, self.footer_text)
        canvas.restoreState()

    def generate_pdf(self):
        elements = []
        elements.append(self.create_title())
        elements.append(self.create_heading())
        elements.append(self.create_dates())
        elements.append(Spacer(1, 10))
        table1 = self.create_table()
        elements.append(table1)
        t_debit = 0
        t_credit = 0
        i = 0
        for item in self.data['data']:
            row_elements = self.create_row(item)
            t_debit += float(item.get("debit", ""))
            t_credit += float(item.get("credit", ""))
            for element in row_elements:
                elements.append(element)
            i += 1
            if i % 6 == 0:
                elements.append(Spacer(1, 40))
                elements.append(self.create_title())
                elements.append(self.create_heading())
                elements.append(self.create_dates())
                elements.append(Spacer(1, 10))
                elements.append(table1)
        elements.append(self.create_total_row(t_debit, t_credit))
        self.footer_text = f"Accrual Basis {datetime.datetime.now()}"
        footer = self.create_footer()
        self.doc.build(elements, onFirstPage=self.add_footer, onLaterPages=self.add_footer)
