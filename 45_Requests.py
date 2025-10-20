# Installation
# To install requests library via pip, use the following command:

# pip install requests

# Syntax
# requests.get(url, params={key: value}, **kwargs)


# Making a Simple GET Request
import requests
response = requests.get("https://www.geeksforgeeks.org/")
print(response.status_code)


# Sending GET Requests with Parameters
import requests
response = requests.get("https://api.github.com/users/naveenkrnl")
print(response.status_code)
print(response.content)


# Response object
import requests
response = requests.get('https://api.github.com/')
print(response.url)
print(response.status_code)


# POST Request Example
import requests
payload = {'username': 'test', 'password': 'test123'}
response = requests.post("https://httpbin.org/post", data=payload)
print(response.text)


# Authentication using Python Requests
import requests
from requests.auth import HTTPBasicAuth
response = requests.get('https://api.github.com/user', auth=HTTPBasicAuth('user', 'pass'))
print(response.status_code)


# SSL Certificate Verification
import requests
response = requests.get('https://expired.badssl.com/', verify=False)
print(response.status_code)


# Providing a custom certificate:
import requests
response = requests.get('https://github.com/', verify='/path/to/certfile')
print(response.status_code)


# Error Handling with Requests
import requests

try:
    response = requests.get("https://www.example.com/", timeout=5)
    response.raise_for_status()
except requests.exceptions.HTTPError as errh:
    print("HTTP Error:", errh)
except requests.exceptions.ConnectionError as errc:
    print("Connection Error:", errc)
except requests.exceptions.Timeout as errt:
    print("Timeout Error:", errt)
except requests.exceptions.RequestException as err:
    print("Something Else:", err)