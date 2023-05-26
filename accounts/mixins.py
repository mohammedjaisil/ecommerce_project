# from django.conf import settings
# from twilio.rest import Client
# import random

# class Messagehandler:
#     otp = None
#     phone_number = None

#     def __init__(self, otp ,phone_number ):
#         self.otp = otp
#         self.phone_number = phone_number
        
#     def sent_otp_phone(self):
#         # account_sid = os.environ['TWILIO_ACCOUNT_SID']
#         # auth_token = os.environ['TWILIO_AUTH_TOKEN']
#         Client = Client(settings.ACCOUNT_SID, settings.AUTH_TOKEN)
#         message = Client.messages.create(
#                                         body=f'Your otp is {self.otp}',
#                                         from_='+8586306903',
#                                         to=self.phone_number
#                                     )

#         print(message.sid)