import tornado.httpserver
import tornado.ioloop
import tornado.web
import signal
import logging
import sys

from .DefaultHandler import DefaultHandler
from .config import *
from .globals import *

import tornado.options as to
to.options.logging = 'debug'
to.parse_command_line()

def signal_term_handler(_signo, _stack_frame):
    # Raises SystemExit(0):
    sys.exit(0)

def getApp():
    signal.signal(signal.SIGTERM, signal_term_handler)
    try:
        set_hook = api.get(BOT_URL + "setWebhook?url=%s" % MyURL)
        if set_hook.status_code != 200:
            logging.error("Can't set hook: %s. Quit." % set_hook.text)
            exit(1)
        application = tornado.web.Application([
            (r"/", DefaultHandler),
        ])
    except KeyboardInterrupt:
        signal_term_handler(signal.SIGTERM, None)
    return application
