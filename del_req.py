import requests
import json


# Correct URL with the actual ID
URL = "http://127.0.0.1:8000/api/bruass/teacher/delete/4"
headers = {
    'Content-Type': 'application/json',
}

response = requests.delete(url=URL, headers=headers)
try:
    response_data = response.json()
    print(response_data)
except json.JSONDecodeError:
    if response.status_code == 204:
        print("Successfully Deleted data.")
    else:
        print("Error: No JSON Response. Status code ", response.status_code)