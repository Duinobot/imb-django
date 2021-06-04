import requests

url = "https://imobilestore.com.au/api/rest/oauth2/token/client_credentials"

payload={}
headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': 'Basic c2hvcHBpbmdfb2F1dGhfY2xpZW50OnNob3BwaW5nX29hdXRoX3NlY3JldA==',
#   'Cookie': 'language=en-gb; currency=AUD; OCSESSID=ca82397adf19a79b9e1987f380'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
