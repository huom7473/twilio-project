# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from text_bot import get_price

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_ahoy_reply():
    """Respond to incoming messages with a friendly SMS."""
    body = request.values.get("Body", None).strip().lower()
    # Start our response
    resp = MessagingResponse()

    message_dict = {'btc': get_price()}
    error_msg = f"Not a valid command. Try {', '.join(message_dict.keys())}"
    # Add a message
    resp.message(message_dict.get(body, error_msg))

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
