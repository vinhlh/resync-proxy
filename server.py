#
# Author    VinhLH <vinh.le@vn.zalora.com>
# Copyright Mar 2016
#
# Create a http server

import tornado.ioloop
import tornado.web
from tornado.options import options

import config
from src.ResyncHandler import ResyncHandler
from src.HealthCheckHandler import HealthCheckHandler

def makeApp():
    return tornado.web.Application([
        (r'/health-check/([a-z-]+)', HealthCheckHandler),
        (r'/resync/([a-zA-Z0-9:\.=-\\s]+)', ResyncHandler)
    ])

if __name__ == '__main__':
    app = makeApp()

    # add logger
    options.log_file_prefix = config.log
    options.parse_command_line()

    app.listen(config.port)
    tornado.ioloop.IOLoop.current().start()
