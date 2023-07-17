import os
import tempfile

from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from tempfile import NamedTemporaryFile
from django.http import HttpResponse, Http404
import os
from .Balance_sheet import BalSheetPDF
from .Invoice import InvoicePDF
from .Journal import JournalPDF
from .Profit_loss import ProfitLossPDF


@api_view(['POST'])
@csrf_exempt
def bs_pdf(request):
    data = request.data

    # Generate the PDF file
    temp_dir = tempfile.mkdtemp()
    temp_file_path = os.path.join(temp_dir, 'balance_sheet.pdf')
    report=BalSheetPDF(temp_file_path, data)
    report.generate_report()
    # Return the download link in the response
    download_link = request.build_absolute_uri(f'/api/BS_pdf/{temp_file_path}')
    response = {'download_link': download_link}
    return Response(response)


@api_view(['POST'])
@csrf_exempt
def pl_pdf(request):
    data = request.data

    # Generate the PDF file
    temp_dir = tempfile.mkdtemp()
    temp_file_path = os.path.join(temp_dir, 'profit_loss.pdf')
    report = ProfitLossPDF(temp_file_path, data)
    report.generate_report()

    # Return the download link in the response
    download_link = request.build_absolute_uri(f'/api/PL_pdf/{temp_file_path}')
    response = {'download_link': download_link}
    return Response(response)
@api_view(['GET'])
@csrf_exempt
def bs_download_pdf(request, file_path):
    # Verify if the file path exists
    if not os.path.exists(file_path):
        raise Http404

    # Serve the file as a download
    with open(file_path, 'rb') as pdf_file:
        response = HttpResponse(pdf_file.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=balance_sheet.pdf'
        return response

@api_view(['GET'])
@csrf_exempt
def pl_download_pdf(request, file_path):
    # Verify if the file path exists
    if not os.path.exists(file_path):
        raise Http404

    # Serve the file as a download
    with open(file_path, 'rb') as pdf_file:
        response = HttpResponse(pdf_file.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=profit_loss.pdf'
        return response

@api_view(['POST'])
@csrf_exempt
def j_pdf(request):
    data = request.data
    # Generate the PDF file
    temp_dir = tempfile.mkdtemp()
    temp_file_path = os.path.join(temp_dir, 'journal.pdf')
    report = JournalPDF(temp_file_path, data)
    report.generate_pdf()
    # Return the download link in the response
    download_link = request.build_absolute_uri(f'/api/j_pdf/{temp_file_path}')
    response = {'download_link': download_link}
    return Response(response)
@api_view(['GET'])
@csrf_exempt
def j_download_pdf(request, file_path):
    # Verify if the file path exists
    if not os.path.exists(file_path):
        raise Http404

    # Serve the file as a download
    with open(file_path, 'rb') as pdf_file:
        response = HttpResponse(pdf_file.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=journal.pdf'
        return response

@api_view(['POST'])
@csrf_exempt
def in_pdf(request):
    data = request.data

    # Generate the PDF file
    temp_dir = tempfile.mkdtemp()
    temp_file_path = os.path.join(temp_dir, 'Invoice.pdf')
    logo = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logo.png")
    report = InvoicePDF(logo, temp_file_path)
    report.create_invoice_pdf(data)
    # Return the download link in the response
    download_link = request.build_absolute_uri(f'/api/in_pdf/{temp_file_path}')
    response = {'download_link': download_link}
    return Response(response)

@api_view(['GET'])
@csrf_exempt
def in_download_pdf(request, file_path):
    # Verify if the file path exists
    if not os.path.exists(file_path):
        raise Http404

    # Serve the file as a download
    with open(file_path, 'rb') as pdf_file:
        response = HttpResponse(pdf_file.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=invoice.pdf'
        return response
