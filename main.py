import logging
import os
import time

##Config##
logging.basicConfig(filename='log.log',
                            filemode='a',
                            format='%(asctime)s %(levelname)s %(funcName)s %(lineno)d %(message)s',
                            datefmt="%Y-%m-%dT%H:%M:%S%z",
                            level=logging.DEBUG)
hostnameToPing = ""
timeToSleep = 300
shouldRun = False
##

def pingTheHost(hostname):
    response = os.system("ping -c 2 " + hostname)
    if response == 0:
        logging.info("Ping was successful")
    else:
        logging.info("Ping has failed")

while shouldRun:
    pingTheHost(hostnameToPing)
    time.sleep(timeToSleep)