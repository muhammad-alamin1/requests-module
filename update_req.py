import requests
import json

# Correct URL with the actual ID
URL = "http://127.0.0.1:8000/api/bruass/teacher/update/6"
headers = {
    'Content-Type': 'application/json',
}
data = {
    "teacher_name": "Sumon",
    "seat": 30
}

# Convert data to JSON format
json_data = json.dumps(data)

# Make the PUT request
res = requests.put(url=URL, data=json_data, headers=headers)

# Check if the response is empty
if res.status_code == 204 or not res.content:
    print("No content in response.")
else:
    try:
        extrack_data = res.json()
        print(extrack_data)
    except json.JSONDecodeError:
        print("Response content is not in JSON format")
