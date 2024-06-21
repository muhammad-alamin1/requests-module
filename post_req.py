import requests
import json


URL = "http://127.0.0.1:8000/api/bruass/teacher/create/"
headers = {
    'Content-Type': 'application/json',
}
data = {
    "teacher_name": "Muhammad",
    "course_name" : "Django",
    "course_duration": 1,
    "seat": 50
}

json_data = json.dumps(data)
req = requests.post(url=URL, data=json_data, headers=headers)
res = req.json()
print(res)
