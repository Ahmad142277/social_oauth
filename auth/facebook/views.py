from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import os

from django.views.decorators.csrf import csrf_exempt
from requests_oauthlib import OAuth2Session
from django.shortcuts import render
from .models import FBUserData

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "2"

FACEBOOK_CLIENT_ID = "284677667401381"
FACEBOOK_CLIENT_SECRET = "6b3701e37321474826bf88e99d70b294"
REDIRECT_URI = "https://127.0.0.1:8000/callback"

authorization_base_url = "https://www.facebook.com/v14.0/dialog/oauth"
token_url = "https://graph.facebook.com/v14.0/oauth/access_token"
scope = ["email"]

class facebookLoginAPIView(APIView):
    @csrf_exempt
    def get(self, request):
        facebook = OAuth2Session(
            client_id=FACEBOOK_CLIENT_ID,
            redirect_uri=REDIRECT_URI,
            scope=scope,
        )
        authorization_url, state = facebook.authorization_url(authorization_base_url)
        request.session["state"] = state
        return Response({"authorization_url": authorization_url}, status=status.HTTP_200_OK)

class facebookCallbackAPIView(APIView):
    @csrf_exempt
    def get(self, request):
        if "error" in request.GET:
            return Response({"message": "Invalid state parameter"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        if not request.session["state"] == request.GET["state"]:
            return Response({"message": "Invalid state parameter"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        facebook = OAuth2Session(
            client_id=FACEBOOK_CLIENT_ID,
            redirect_uri=REDIRECT_URI,
            scope=scope,
        )

        token_response = facebook.fetch_token(
            token_url,
            client_secret=FACEBOOK_CLIENT_SECRET,
            authorization_response=request.build_absolute_uri(),
        )

        request.session["access_token"] = token_response["access_token"]

        # Fetch user's data using the Graph API
        user_response = facebook.get("https://graph.facebook.com/me?fields=id,name,email")
        user_data = user_response.json()

        request.session["facebook_id"] = user_data.get("id")
        request.session["name"] = user_data.get("name")
        request.session["email"] = user_data.get("email")
        data={
            'token': request.session["facebook_id"],
            'email': request.session["email"]
        }
        if FBUserData.objects.filter(facebook_id=data['email'],token=data['token']).exists():
            return Response({'msg': 'user already exist'}, status=status.HTTP_200_OK)

        FBUserData.objects.create(
            facebook_id=request.session["email"],
            token=request.session["facebook_id"],
            name=request.session["name"]
        )

        return Response(data, status=status.HTTP_200_OK)
