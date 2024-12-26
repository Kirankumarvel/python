# Continuously making network requests until a successful response is received
import requests

while True:
    response = requests.get('https://example.com')
    if response.status_code == 200:
        break
    print('Retrying...')
print('Success!')