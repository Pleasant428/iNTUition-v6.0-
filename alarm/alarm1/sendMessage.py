# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
def sms():
    account_sid = 'AC07d173bb1598092747760c83d3cbd008'
    auth_token = 'b3fca9108b44cacf696fbb08e09fad35'
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                         body="I can't wake up, please wake me up HAHA",
                         from_='+12562083796',
                         to='+6586189225'
                     )

    print(message.sid)
