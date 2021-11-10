import requests
import json
response = requests.post('http://127.0.0.1:5000/predictions', '{"data": "Cars374.png"}')
#response = requests.post('http://127.0.0.1:5000/predictions', '{"data": "Cars387.png"}')
#response = requests.post('http://127.0.0.1:5000/predictions', '{"data": "Cars18.png"}')
print(response.json())
