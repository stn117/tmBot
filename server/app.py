import tornado.httpserver
import tornado.ioloop
import tornado.web

from .DefaultHandler import DefaultHandler


def getApp():
    application = tornado.web.Application([
        (r"/", DefaultHandler),
    ])

    return application
