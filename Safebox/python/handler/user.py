#!/usr/bin/evn python3
# -*- coding: utf-8 -*-

################################################################################
import tornado.web

################################################################################
class Handler(tornado.web.RequestHandler):
    def get(self):
        self.write("This is UserHandler -> [GET METHOD]\n")

    def post(self):
        self.write("This is UserHandler -> [POST METHOD]\n")