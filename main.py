import logging
import os
import requests.exceptions
import time
from twilio.base.exceptions import TwilioRestException
from twilio.rest import Client

##Begin Config##
logging.basicConfig(filename='log.log',
                            filemode='a',
                            format='%(asctime)s %(levelname)s %(funcName)s %(lineno)d %(message)s',
                            datefmt="%Y-%m-%dT%H:%M:%S%z",
                            level=logging.DEBUG)
hostnameToPing = ""
timeToSleep = 300
shouldRun = False
shouldText = False
sendTextFeature = False
account_sid = ''
auth_token = ''
fromNumber = ''
toNumber = ''
##End Config##

def pingTheHost(hostname):
    global shouldText
    global sendTextFeature
    response = os.system("ping -c 2 " + hostname)
    if response == 0:
        logging.info(f"Ping of {hostname} was successful")
        if(shouldText and sendTextFeature):
            textErrors = sendTextMessage("The internet was out")
            if(textErrors is None):
                shouldText = False
        return("Success")
    else:
        logging.warn(f"Ping of {hostname} has failed")
        shouldText = True
        return("Failure")

def sendTextMessage(messageText): 
    client = Client(account_sid, auth_token)
    logging.debug(f"Sending a text with message {messageText} to {toNumber}")
    try:
        message = client.messages.create(
                                  body=messageText,
                                  from_=fromNumber,
                                  to=toNumber
                              )
    except requests.exceptions.ConnectionError:
        logging.error("Encountered a network error when sending a message")
        return("Fail")
    except TwilioRestException:
        logging.error("Encountered a twilio error when sending a message")
        return("Fail")
    return (message.error_code)

while shouldRun:
    pingTheHost(hostnameToPing)
    time.sleep(timeToSleep)