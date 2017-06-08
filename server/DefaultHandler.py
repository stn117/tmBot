import logging
import tornado
import json

class DefaultHandler(tornado.web.RequestHandler):
    def get(self):
        response = "sexy tornado"
        self.write(response)

    def post(self):
        try:
            logging.debug("Got request: %s" % self.request.body)
            update = tornado.escape.json_decode(self.request.body)
            message = update['message']
            text = message.get('text')
            if text:
                logging.info("MESSAGE\t%s\t%s" % (message['chat']['id'], text))

                if text[0] == '/':
                    # command, *arguments = text.split(" ", 1)
                    # response = CMD.get(command, not_found)(arguments, message)
                    response = "sexy"
                    logging.info("REPLY\t%s\t%s" % (message['chat']['id'], response))
                    self.write(response)
        except Exception as e:
            logging.warning(str(e))
