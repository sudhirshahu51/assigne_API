from django.shortcuts import render
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CountrySerializer

from rest_framework.authtoken.models import Token


from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class Auth(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        # Validate the credentials (you can customize this)
        if username == 'username' and password == 'password':#changed user name and password
            token, created = Token.objects.get_or_create(user=username)  # Create or get the token
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        

class CountryDetail(APIView):
    def get(self, request, country_name):
        try:
            # Fetch country data from the REST Countries API
            response = requests.get(f'https://restcountries.com/v3/name/{country_name}')
            response.raise_for_status()
            country_data = response.json()[0]

            # Serialize the data and return it as a JSON response
            serializer = CountrySerializer(country_data)
            return Response(serializer.data)

        except requests.exceptions.RequestException as e:
            return Response({'error': 'Error fetching country data'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CountryList(APIView):
    def get(self, request):
        try:
            # Fetch a list of countries from the REST Countries API
            response = requests.get('https://restcountries.com/v3.1/all')
            response.raise_for_status()
            countries_data = response.json()

            # Serialize the data and return it as a JSON response
            serializer = CountrySerializer(countries_data, many=True)
            return Response(serializer.data)

        except requests.exceptions.RequestException as e:
            return Response({'error': 'Error fetching countries data'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        


# Create your views here.
