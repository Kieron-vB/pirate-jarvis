import requests

DEVICE_ID = '6a13553c5ccc2dc46e0ea6d5'
API_KEY = '2fa5110c-ae5e-4a80-8157-0a69fad8cc99'
SMS_ID = 'c92c99c4-90a0-44dc-b007-c09e70c8b95a'


headers = {"x-api-key": API_KEY}
response = requests.get(f"https://api.textbee.dev/api/v1/gateway/devices/{DEVICE_ID}/messages",
                         headers = headers)
print(response.json())

