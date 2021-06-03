from django.shortcuts import render
import requests
from django.http import JsonResponse
# Create your views here.

def login (request):
     
     if request.method == 'POST':
          print("request >>>>>>",request.POST)
          url = "https://imobilestore.com.au/api/rest/login"

          payload="{\n  \"email\": \""+request.POST['email']+"\",\n  \"password\": \""+request.POST['password']+"\"\n}"
          headers = {
          'accept': 'application/json',
          'Authorization': 'Bearer 954a595ecd9ed153c9b29994530a834907c92e4e',
          'Content-Type': 'application/json',
          'Cookie': 'OCSESSID=c513d47c2f2d2c4986f06512c0; language=en-gb; currency=AUD; mailchimp_integration_popup=triggered'
          }

          response = requests.request("POST", url, headers=headers, data=payload)

          print( ">>>>>>>>>>>",response.text)
          return JsonResponse(response.json())

     return render(request, 'user/login.html')


