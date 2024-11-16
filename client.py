import requests
import logging
import time

logging.basicConfig(filename='appClient.log', level=logging.INFO, format='%(asctime)s - %(message)s')

while True:
    time.sleep(10)
    logging.info('Hello World route was called, now trying to request')
    try:
        requests.get('http://localhost:5000/azSimpleFlask')
        logging.info('Hello World route was called, call completed')
    except Exception as e:
        logging.info('Call reached exception')

