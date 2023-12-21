from django.conf import settings
from twilio.rest import Client
import random
import os

class MessaHandler:
    phone_number = None
    otp = None
    
    def __init__(self, phone_number, otp) -> None: 
        self.phone_number = phone_number
        self.otp = otp
        
    def send_otp_on_phone(self):
        client = Client(settings.ACCOUNT_SID, settings.AUTH_TOKEN)

        message = client.messages \
                        .create(
                            body=f'Your Otp is {self.otp}',
                            from_='+12564725861',
                            to =self.phone_number
                        )

        print(message.sid)
