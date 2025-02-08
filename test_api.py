import requests

# URL of your Flask API
url = "http://127.0.0.1:5000/predict"

# Data to send to the API
data = {
    "text": "i love me"
}

# Send POST request to the API
response = requests.post(url, json=data)

# Print the response from the Flask API
print(response.json())
