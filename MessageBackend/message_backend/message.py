import os
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

accountSid = os.environ.get('ACCOUNT_SID')
authToken = os.environ.get('AUTH_TOKEN')
fromNo = os.environ.get('FROM_NO')
CALLBACK = os.environ.get('CALL_BACK',
                          'http://6c895f5d5d72.ngrok.io/api/status/')


client = Client(accountSid, authToken)


def send_message(body, to):
    try:
        message = client.messages \
                        .create(
                            body=body,
                            from_=fromNo,
                            status_callback=CALLBACK,
                            to=to
                        )

    except TwilioRestException:
        print('came here')
        return {'sent': False}

    return {'sent': True, 'response': message}
