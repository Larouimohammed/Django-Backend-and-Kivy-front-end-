import requests
import json
headers = {'Accept': 'application/json'}
response = requests.get('http://127.0.0.1:8000/boutique',headers=headers).json()

print(f"Response: {response}")
print(f"type: {type(response)}")
name =response.split(",")

for line in response.split(","):
    print(f"type: {str(line)}")
  
  
