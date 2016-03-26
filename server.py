#
# Author    VinhLH <vinh.le@vn.zalora.com>
# Copyright Mar 2016
#
# Create a http server

import tornado.ioloop
import tornado.web

import config
from src.ResyncHandler import ResyncHandler
from src.HealthCheckHandler import HealthCheckHandler

def make_app():
    return tornado.web.Application([
        (r'/health-check/([a-z-]+)', HealthCheckHandler),
        (r'/resync/([a-zA-Z0-9:\.=-\\s]+)', ResyncHandler)
    ])

if __name__ == '__main__':
    app = make_app()
    app.listen(config.port)
    tornado.ioloop.IOLoop.current().start()
