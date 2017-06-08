import tornado.httpserver
import tornado.ioloop
import tornado.web
import requests
import signal
import logging

from .DefaultHandler import DefaultHandler
from .config import *
from .globals import *

def signal_term_handler(_signo, _stack_frame):
    # Raises SystemExit(0):
    sys.exit(0)

def getApp():
    signal.signal(signal.SIGTERM, signal_term_handler)
    try:
        set_hook = api.get(BOT_URL + "setWebhook?url=%s" % MyURL)
        print (BOT_URL + "setWebhook?url=%s" % MyURL)
        if set_hook.status_code != 200:
            logging.error("Can't set hook: %s. Quit." % set_hook.text)
            exit(1)
        application = tornado.web.Application([
            (r"/", DefaultHandler),
        ])
    except KeyboardInterrupt:
        signal_term_handler(signal.SIGTERM, None)
    return application
