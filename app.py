from flask import Flask
import logging
app = Flask(__name__)
logging.basicConfig(filename='appServer.log', level=logging.INFO, format='%(asctime)s - %(message)s')


@app.route('/azSimpleFlask')
def hello_world():  # put application's code here
    logging.info('Hello World route was called, call completed')

    print('Hello World inside route!')


    return 'Hello World!'


if __name__ == '__main__':
    app.run()
