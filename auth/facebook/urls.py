from django.urls import path
from .views import facebookLoginAPIView, facebookCallbackAPIView

urlpatterns = [
    path("login", facebookLoginAPIView.as_view(), name='facebook_login'),
    path("callback", facebookCallbackAPIView.as_view(), name="callback"),
]