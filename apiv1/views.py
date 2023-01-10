from datetime import datetime

import pytz
from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication

from drugstore.settings import TOKEN_EXPIRE
from .serializers import ProductSerializer
from main.models import Product



class ProductViewSet(ModelViewSet):
    queryset = Product.objects.filter(is_published=True)
    serializer_class = ProductSerializer



class AuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        Token.objects.filter(user=user).delete()
        token, created = Token.objects.get_or_create(user=user)
        # try:
        #     token = Token.objects.get(user=user)
        # except Token.DoesNotExist:
        #     token, created = Token.objects.get_or_create(user=user)
        # else:
        #     token.delete()
        #     token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})


class EcpiredTockenAuthentication(TokenAuthentication):

    def authenticate_credentials(self, key):
        user, token = super().authenticate_credentials(key=key)
        utc_now = datetime.utcnow()
        utc_now = utc_now.replace(tzinfo=pytz.utc)
        if token.created < utc_now + TOKEN_EXPIRE:
            pass
