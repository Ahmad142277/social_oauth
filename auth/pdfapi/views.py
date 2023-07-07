import os
import tempfile

from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from tempfile import NamedTemporaryFile
from django.http import HttpResponse, Http404
import os
from .Balance_sheet import bal_sheet_pdf
from .Journal import jour_pdf
from .Profit_loss import pro_loss_pdf


@api_view(['POST'])
@csrf_exempt
def bs_pdf(request):
    data = request.data

    # Generate the PDF file
    temp_dir = tempfile.mkdtemp()
    temp_file_path = os.path.join(temp_dir, 'balance_sheet.pdf')
    bal_sheet_pdf(temp_file_path, data)

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
    temp_file_path = os.path.join(temp_dir, 'Profit_loss.pdf')
    pro_loss_pdf(temp_file_path, data)

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
    temp_file_path = os.path.join(temp_dir, 'Journal.pdf')
    jour_pdf(temp_file_path, data)

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
