from django.urls import path
from .views import generate_pdf

urlpatterns = [
    path('balance_sheet_pdf/', generate_pdf, name='generate_pdf'),
]
