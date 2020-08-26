import logging
import platform
import os
import requests.exceptions
import time
from twilio.base.exceptions import TwilioRestException
from twilio.rest import Client

##Begin Config##
# Necessary flags and values
host_to_ping = ""
timeToSleep = 5
should_the_script_run = False
should_the_script_send_texts = False
# Twilio Credentials
account_sid = ""
auth_token = ""
text_from_number = ""
text_to_number = ""
# Logging
logging.basicConfig(filename='log.log',
                    filemode='a',
                    format='%(asctime)s %(levelname)s %(funcName)s %(lineno)d %(message)s',
                    datefmt="%Y-%m-%dT%H:%M:%S%z",
                    level=logging.INFO)
##End Config##


send_text_alert = False


def ping_the_host(hostname):
    global send_text_alert
    global should_the_script_send_texts
    os_ping_count_param = '-n' if platform.system().lower() == 'windows' else '-c'
    response = os.system("ping " + os_ping_count_param + " 2 " + hostname)
    if response == 0:
        logging.info(f"Ping of {hostname} was successful")
        if(send_text_alert and should_the_script_send_texts):
            textErrors = send_text_message("The internet was out")
            if(textErrors is None):
                send_text_alert = False
        return("Success")
    else:
        logging.warn(f"Ping of {hostname} has failed")
        send_text_alert = True
        return("Failure")


def send_text_message(message_text):
    client = Client(account_sid, auth_token)
    logging.debug(
        f"Sending a text with message {message_text} to {text_to_number}")
    try:
        message = client.messages.create(
            body=message_text,
            from_=text_from_number,
            to=text_to_number
        )
    except requests.exceptions.ConnectionError:
        logging.error("Encountered a network error when sending a message")
        return("Fail")
    except TwilioRestException:
        logging.error("Encountered a twilio error when sending a message")
        return("Fail")
    return (message.error_code)


while should_the_script_run:
    ping_the_host(host_to_ping)
    time.sleep(timeToSleep)