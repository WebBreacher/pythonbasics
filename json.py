'''
Script to demonstrate how to retrieve a web page
using the requests library and parsing with json
'''

# Import the contents of the requests library
import requests

# URL to make the request to
url = 'http://en.gravatar.com/fyodor.json'

# Make the request, don't check for HTTPS certificate issues and store response in 'response'
print('Making a request to {}'.format(url))
response = requests.get(url, timeout=30, verify=False)
json_out = response.json()

# The Gravatar output is in JSON format so we do not need to convert.
# We do need to correctly parse each element whether dictionary or list.
# Here we look in the 'entry' element, then take the first item from the
# list (element 0) and, within that, look for a dictionary entry with 'id'
# as the key.
print('The ID is: {0}'.format(json_out["entry"][0]["id"]))