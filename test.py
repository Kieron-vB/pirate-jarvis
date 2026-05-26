import requests

DEVICE_ID = '6a13553c5ccc2dc46e0ea6d5'
API_KEY = '2fa5110c-ae5e-4a80-8157-0a69fad8cc99'

def send_SMS(recipient, message):
    req_fields = {"recipients": [recipient], 
                  "message": message}
    headers = {"Content-Type":"application/json",
               "x-api-key": API_KEY}
    response = requests.post(f"https://api.textbee.dev/api/v1/gateway/devices/{DEVICE_ID}/send-sms",
                             json=req_fields,
                             headers = headers)
    return response.json()

send_SMS("+4168041060", "API Test")
