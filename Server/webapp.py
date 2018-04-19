#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ==============================================================================
#
# Author        : lescpsn@aliyun.com
# Generate Data : 2018-04-19
# Desciption    : 基于tornado框架下的web服务端应用，主要提供REST-API服务
#
# ==============================================================================

import signal
import tornado.autoreload
import tornado.ioloop
import tornado.web

class UserHandler(tornado.web.RequestHandler):

    def get(self):
        self.write("UserHandler GET Method\012")

    def post(self):
        self.write("UserHandler POST Method\012")

################################################################################
def get_handlers():
    return  [
        (r"/user", UserHandler),
    ]

################################################################################
def register_signal():
    signal.signal(signal.SIGINT,  signal.SIG_DFL)



################################################################################
def register_webapp(handlers):
    settings = dict(
           debug=True,
    )

    application = tornado.web.Application(handlers, **settings)
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(80)
    instance = tornado.ioloop.IOLoop.instance()
    tornado.autoreload.start(instance)
    instance.start()

################################################################################
def main():
    register_signal()
    register_webapp(get_handlers())

################################################################################
if __name__ == '__main__':
    main()