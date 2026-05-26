axios = require('axios');

const DEVICE_ID = 'YOUR_DEVICE_ID';
const API_KEY = 'YOUR_API_KEY';

async function sendSMS(recipient, message) {
  const response = await axios.post(
    `https://api.textbee.dev/api/v1/gateway/devices/${DEVICE_ID}/send-sms`,
    {
      recipients: [recipient],
      message,
      // simSubscriptionId: 1,
    },
    {
      headers: {
        'Content-Type': 'application/json',
        'x-api-key': API_KEY,
      },
    }
  );

  return response.data;
}

// Usage
sendSMS('+1234567890', 'Hello from textbee.dev!');
