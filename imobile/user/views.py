from django.shortcuts import render
import requests
from django.http import JsonResponse
from django.contrib.sessions.backends.db import SessionStore
# Create your views here.

def home(request):
     return render(requrest , 'user/home.html')


def login (request):
     if request.method == 'POST':
          url = "https://imobilestore.com.au/api/rest/oauth2/token/client_credentials"
          payload={}
          headers = {
          'Accept': 'application/json',
          'Content-Type': 'application/json',
          'Authorization': 'Basic c2hvcHBpbmdfb2F1dGhfY2xpZW50OnNob3BwaW5nX29hdXRoX3NlY3JldA==',
          }
          access_token = requests.request("POST",url, headers=headers, data=payload).json()['data']['access_token']
          request.session['access_token'] = access_token

          print("::::::::::::>>>>>>>>>>>",access_token)
          print("access_token",request.session.get('access_token'))

          url = "https://imobilestore.com.au/api/rest/login"
          payload="{\n  \"email\": \""+request.POST['email']+"\",\n  \"password\": \""+request.POST['password']+"\"\n}"
          headers = {
          'accept': 'application/json',
          'Authorization': "Bearer " + access_token,
          'Content-Type': 'application/json',
          }
          response = requests.request("POST", url, headers=headers, data=payload)
          # return render(response.json(), 'user/login.html')
          return render(request, 'user/home.html', { 'response' : response.json() })
          # return JsonResponse(response.json())
     return render(request, 'user/login.html')


def logout(request):
     if request.method == 'POST':
          url = "https://imobilestore.com.au/api/rest/logout"
          payload={}
          headers = {
          'Accept': 'application/json',
          'Content-Type': 'application/json',
          'Authorization': "Bearer " + request.session.get('access_token'),
          }
          response = requests.request("POST", url, headers=headers, data=payload)
          print(response.text)
          # return JsonResponse(response.json())
          return render(request, 'user/login.html', { 'response' : response.json() })
     return render(request, 'user/home.html')


def addresses(request):
     if request.method == 'GET':
          url = "https://imobilestore.com.au/api/rest/account/address"
          payload={}
          headers = {
          'Accept': 'application/json',
          'Authorization': 'Bearer '+request.session.get('access_token'),
          }
          response = requests.request("GET", url, headers=headers, data=payload)
          print(response.text)
          return render(request, 'user/address.html', { 'address' : response.json() })