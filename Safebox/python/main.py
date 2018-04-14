#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ==============================================================================
#
# Author        : lescpsn@aliyun.com
# Generate Data : 2018-04-14
# Desciption    : 基于tornado框架下的web应用开发
#
# ==============================================================================

import os
import signal
import tornado.autoreload
import tornado.ioloop
import tornado.web
import handler

################################################################################
def get_handlers():
    return  [
        (r"/user", handler.user.Handler),
        (r"/friend", handler.friend.Handler),
    ]


################################################################################
def register_signal():
    signal.signal(signal.SIGINT,  signal.SIG_DFL)


################################################################################
def register_app(handlers):
    settings = dict(
           debug=True,
    )

    application = tornado.web.Application(handlers, **settings)
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8080)
    instance = tornado.ioloop.IOLoop.instance()
    tornado.autoreload.start(instance)
    instance.start()


################################################################################
def main():
    register_signal()
    register_app(get_handlers())


################################################################################
if __name__ == '__main__':
    main()