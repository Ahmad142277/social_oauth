# social_oauth

# pdf_api
## urls:
http://127.0.0.1:8000/api/balance_sheet_pdf/

http://127.0.0.1:8000/api/profit_loss_pdf/

http://127.0.0.1:8000/api/journal_pdf/

http://127.0.0.1:8000/api/invoice_pdf/


## test input for pdf api
### for journal

{
    "from_to": "03/01/2021 to 03/01/2021",
    "data": [
        {
            "date": "03/01/2021",
            "trans_type_credit": "Deposit",
            "num_credit": "",
            "name_credit": "",
            "memo_credit": "Opening Balance",
            "account_credit": "Cash in bank",
            "credit": "23.45",
            "memo_debit": "Supplement to the minimum commission for operations",
            "account_debit": "Commissions and fees",
            "debit": "23.45"
        },
        {
            "date": "03/02/2021",
            "trans_type_credit": "Deposit",
            "num_credit": "",
            "name_credit": "",
            "memo_credit": "Opening Balance",
            "account_credit": "Cash in bank",
            "credit": "23.45",
            "memo_debit": "Supplement to the minimum commission for operations",
            "account_debit": "Commissions and fees",
            "debit": "23.45"
        },
        {
            "date": "03/03/2021",
            "trans_type_credit": "Deposit",
            "num_credit": "",
            "name_credit": "",
            "memo_credit": "Opening Balance",
            "account_credit": "Cash in bank",
            "credit": "23.45",
            "memo_debit": "Supplement to the minimum commission for operations",
            "account_debit": "Commissions and fees",
            "debit": "23.45"
        },
        {
            "date": "03/04/2021",
            "trans_type_credit": "Deposit",
            "num_credit": "",
            "name_credit": "",
            "memo_credit": "Opening Balance",
            "account_credit": "Cash in bank",
            "credit": "23.45",
            "memo_debit": "Supplement to the minimum commission for operations",
            "account_debit": "Commissions and fees",
            "debit": "23.45"
        },
        {
            "date": "03/05/2021",
            "trans_type_credit": "Deposit",
            "num_credit": "",
            "name_credit": "",
            "memo_credit": "Opening Balance",
            "account_credit": "Cash in bank",
            "credit": "23.45",
            "memo_debit": "Supplement to the minimum commission for operations",
            "account_debit": "Commissions and fees",
            "debit": "23.45"
        }
    ]
}

### Balance sheet

{
    "date": "2023-07-05",
    "cash_in_bank": 50000,
    "total_current_assets": 50000,
    "total_assets": 100000,
    "net_income": 20000,
    "opening_balance_equity": 10000,
    "owner_loan": 5000,
    "retained_earning": 1000,
    "total_shareholder_equity": 31000,
    "total_liabilities_equity": 100000
}

### for Profit loss

{
    "date_from": "2023-01-01",
    "date_to": "2023-12-31",
    "revenue_general": 50000,
    "total_income": 50000,
    "gross_profit": 30000,
    "commissions_and_fees": 10000,
    "office_expenses": 8000,
    "other_selling_expenses": 2000,
    "total_expense": 20000,
    "net_earnings": 10000
}

### for invoice

{
    "from": "John Doe",
    "business_name": "ABC Company",
    "from_address": "123 Main St, City, State, ZIP",
    "bill_to": "Jane Smith",
    "att": "Accounting Department",
    "company_name": "XYZ Corp",
    "invoice_no": "INV-001",
    "date": "2023-07-09",
    "due_date": "2023-08-09",
    "total_amount": 1000.0,
    "due_amount": 750.0,
    "remit_to": "Agmandkan aksgjahs ahsgujsh sahjasjka agjsjokad",
    "Purchase_details": [
        {
            "descipt_memo": "Item 1",
            "amount": 100.0
        },
        {
            "descipt_memo": "Item 2",
            "amount": 200.0
        },
        {
            "descipt_memo": "Item 3",
            "amount": 300.0
        }
    ]
}

