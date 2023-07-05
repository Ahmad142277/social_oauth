from django.urls import path
from .views import GoogleLoginAPIView, GoogleCallbackAPIView

urlpatterns = [
    path('login/', GoogleLoginAPIView.as_view(), name='google-login'),
    path('callback/', GoogleCallbackAPIView.as_view(), name='google-callback'),
]
