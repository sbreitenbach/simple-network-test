import logging
import os

##Log Config##
logging.basicConfig(filename='log.log',
                            filemode='a',
                            format='%(asctime)s %(levelname)s %(funcName)s %(lineno)d %(message)s',
                            datefmt="%Y-%m-%dT%H:%M:%S%z",
                            level=logging.DEBUG)
##

def pingTheHost(hostname):
    response = os.system("ping -c 2 " + hostname)
    if response == 0:
        print("it's up!")
        logging.info("Ping was successful")
    else:
        print("it's down!")
        logging.info("Ping has failed")