import logging
import os
import time
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
            sendTextMessage("The internet was out")
            shouldText = False
        return("Success")
    else:
        logging.warn(f"Ping of {hostname} has failed")
        shouldText = True
        return("Failure")

def sendTextMessage(messageText): 
    client = Client(account_sid, auth_token)
    logging.debug(f"Sending a text")
    message = client.messages.create(
                              body=messageText,
                              from_=fromNumber,
                              to=toNumber
                          )
    return (message.error_code,message.body)

while shouldRun:
    pingTheHost(hostnameToPing)
    time.sleep(timeToSleep)