from io import BytesIO

from django.http import HttpResponse, FileResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .Balance_sheet import bal_sheet_pdf


@api_view(['POST'])
def generate_pdf(request):
    data = request.data

    # Generate the PDF using ReportLab
    buffer = BytesIO()
    bal_sheet_pdf(buffer, data)
    buffer.seek(0)

    # Create the response with the PDF file
    response = FileResponse(buffer, as_attachment=True, filename='bal_sheet.pdf')
    return response
