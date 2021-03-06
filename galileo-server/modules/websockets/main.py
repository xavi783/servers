# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 17:28:20 2014

@author: xavi783
"""

import os
import json
import base64
from tornado.websocket import WebSocketHandler

LISTENERS = []

class RTPHandler(WebSocketHandler):

    __decoder = json.JSONDecoder()

    def initialize(self, assets_path):
        self.assets_path = assets_path
        self.__video = VideoImagesHandler(os.path.join(self.assets_path,"video"))

    def open(self):
        LISTENERS.append(self)

    def on_message(self,message):
        self.write_message(self.__video.get("image.jpg"))

    def on_close(self):
        LISTENERS.remove(self)

class VideoImagesHandler(object):

    encoder = json.JSONEncoder()
    data = {"pfx": "data:image/jpg;base64,", "src": False}
    
    def __init__(self, assets_path):
        self.assets_path = assets_path

    def get(self,source):
        with open(os.path.join(self.assets_path,source),'r') as fd:
            self.data["src"]=self.data["pfx"]+base64.standard_b64encode(fd.read())
        return self.encoder.encode(self.data)  
