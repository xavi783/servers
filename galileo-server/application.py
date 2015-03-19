#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 17:28:20 2014

@author: xavi783
"""

import sys
sys.path.append('./modules')

import os
#from modules.torduino import pins
from tornado.web import Application, StaticFileHandler, RequestHandler
from tornado.ioloop import IOLoop, PeriodicCallback
from modules.websockets import main as ws
from functools import partial

from tornado.log import enable_pretty_logging
enable_pretty_logging()

settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "template_path": os.path.join(os.path.dirname(__file__), "templates"),
    "assets_path": os.path.dirname(__file__),
    "debug": True
}

class MainHandler(RequestHandler):
    def get(self):
        self.render("index.html", title="My title")

def ws_loop():
    io_loop = IOLoop.instance()
    for elements in ws.LISTENERS:
        io_loop.add_callback(partial(elements.on_message, "new_image"))

if __name__ == "__main__":
    application = Application([
        (r"/", MainHandler),
#       (r"/turn_light/", pins.Pin13Handler),
        (r"/websocket", ws.RTPHandler, dict(assets_path=settings['assets_path'])),
        (r"/(.*)", StaticFileHandler, dict(path=settings['static_path']))
    ], **settings)
    application.listen(8888)
    main_loop = IOLoop.instance()
    sched = PeriodicCallback(ws_loop, 160, io_loop=main_loop)
    sched.start()
    main_loop.start()
