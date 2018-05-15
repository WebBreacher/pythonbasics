'''
Script to demonstrate how to retrieve a web page
using the requests library
'''

# Import the contents of the requests library
import requests

# URL to make the request to
url = 'http://whatu.info'

# Make the request, don't check for HTTPS certificate issues and store response in 'response'
response = requests.get(url, timeout=30, verify=False)

print(response.text)