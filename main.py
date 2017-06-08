#!/usr/bin/env python3

import tornado
import os

from server.app import getApp

if __name__ == '__main__':
    application = getApp()
    # http_server = tornado.httpserver.HTTPServer(application)
    application.listen(os.environ.get("PORT", 5000))
    tornado.ioloop.IOLoop.current().start()
