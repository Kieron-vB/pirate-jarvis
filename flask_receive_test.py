#Imports
from flask import Flask, request, jsonify

#Create an instance of Flask
app = Flask(__name__)

@app.route('/webhook/textbee', methods=['POST'])
def webhook():
    payload = request.json
    event = payload.get('webhookEvent')
    if event == 'MESSAGE_RECEIVED':
        print(f"Received from {payload.get('sender')}: {payload.get('message')}")
    return jsonify({'success': True}), 200

if __name__ == '__main__':
    #Run the app on port 127.0.0.1:3030
    app.run(port=3030)
