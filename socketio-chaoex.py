import logging

from socketIO_client import SocketIO, LoggingNamespace

import logging
logging.getLogger('socketIO-client').setLevel(logging.DEBUG)
logging.basicConfig()
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36,android'};


def on_bbb_response(*args):
    print('on_bbb_response', args)


def on_connect():
    print('[Connected]')


options = {
    'transports': ['websocket']
};

with SocketIO(host='http://39.106.135.162',
             transports='websocket', header=headers) as socketIO:
    socketIO.emit('entrust', {'baseCurrencyId': 1, 'tradeCurrencyId': 2})
    socketIO.on('entrust', on_bbb_response)

socketIO.on('connect', on_connect)

socketIO.wait(seconds=1)
