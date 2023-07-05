from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import os
import requests
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
from pip._vendor import cachecontrol
import google.auth.transport.requests
from django.views.decorators.csrf import csrf_exempt

from .models import UserData

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

client_secrets_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "client_secret.json")

flow = Flow.from_client_secrets_file(
     client_secrets_file=client_secrets_file,
     scopes=["https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email", "openid"],
     redirect_uri="http://127.0.0.1:8000/google/callback"
   )

GOOGLE_CLIENT_ID = "750007652305-5hgjrsifqmevqn3r22p7kti0e3m5a6fd.apps.googleusercontent.com"

class GoogleLoginAPIView(APIView):
    @csrf_exempt
    def get(self, request):

        authorization_url, state = flow.authorization_url()
        request.session["state"] = state

        return Response({"authorization_url": authorization_url}, status=status.HTTP_200_OK)

class GoogleCallbackAPIView(APIView):
    @csrf_exempt
    def get(self, request):
        flow.fetch_token(authorization_response=request.build_absolute_uri())

        if not request.session["state"] == request.GET["state"]:
            return Response({"message": "Invalid state parameter"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        credentials = flow.credentials
        request_session = requests.session()
        cached_session = cachecontrol.CacheControl(request_session)
        token_request = google.auth.transport.requests.Request(session=cached_session)

        id_info = id_token.verify_oauth2_token(
            id_token=credentials._id_token,
            request=token_request,
            audience=GOOGLE_CLIENT_ID
        )

        request.session["google_id"] = id_info.get("email")
        request.session["token"] = id_info.get("sub")
        request.session["name"] = id_info.get("name")
        data = {
            'google_id': request.session["google_id"],
            'token': request.session["token"]
        }
        if UserData.objects.filter(google_id=data['google_id'],token=data['token']).exists():
            return Response({'msg': 'user already exist'}, status=status.HTTP_200_OK)

        UserData.objects.create(
            google_id=request.session["google_id"],
            token=request.session["token"],
            name=request.session["name"]
        )
        return Response(data, status=status.HTTP_200_OK)