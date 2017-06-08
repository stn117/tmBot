#!/usr/bin/env python3

import tornado
import os

from server.app import getApp
from server.config import PORT

if __name__ == '__main__':
    application = getApp()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(PORT)
    tornado.ioloop.IOLoop.instance().start()
