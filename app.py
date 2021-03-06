import csv
import random
from flask import Flask
from twilio.twiml.messaging_response import MessagingResponse


app = Flask(__name__)

with open('truisms.csv', 'r') as f:
    reader = csv.reader(f)
    truisms = list(reader)


@app.route('/sms', methods=['POST'])
def sms():

    truism = random.choice(truisms)[0]

    resp = MessagingResponse()
    resp.message(truism)
    return str(resp)


if __name__ == '__main__':
    app.run()
