from django.urls import path, re_path
from .views import bs_pdf, bs_download_pdf, pl_pdf, pl_download_pdf, j_pdf, j_download_pdf

urlpatterns = [
    path('balance_sheet_pdf/', bs_pdf, name='balance_sheet_pdf'),
    path('profit_loss_pdf/', pl_pdf, name='profit_loss_pdf'),
    path('journal_pdf/', j_pdf, name='journal_pdf'),
    re_path(r'^j_pdf/(?P<file_path>.+)$', j_download_pdf, name='j_pdf'),
    re_path(r'^PL_pdf/(?P<file_path>.+)$', pl_download_pdf, name='bs_pdf'),
    re_path(r'^BS_pdf/(?P<file_path>.+)$', bs_download_pdf, name='bs_pdf'),
]
