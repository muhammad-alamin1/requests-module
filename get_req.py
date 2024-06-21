import requests


URL = "http://127.0.0.1:8000/api/info/"
SINGLE_URL = f"http://127.0.0.1:8000/api/info/{45}"

response = requests.get(url=SINGLE_URL)
if response.status_code == 200:
    try:
        data = response.json()
        print(data)
    except ValueError:
        print("Response content is not valid JSON")
else:
    print(f"Request failed with status code {response.status_code}")
    print(f"Response content: {response.text}")
