# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 17:28:20 2014

@author: xavi783
"""

from modules.gapi import Driver as gp
from tornado.web import RequestHandler

class Pin13Handler(RequestHandler):
    
    def initialize(self):
        self.key = 1
        driver = gp.Driver()
        driver.chmod("/sys/class/gpio/export",0777)
        self.pin13 = driver.find_gpio(pin=13)
        driver.config_write(self.pin13['level'],"out","strong",0)
        driver.config_gpio(self.pin13['linux'],"out","strong")
        self.driver = driver

    def get(self):
        self.key = 1 - self.driver.write_gpio(self.pin13['linux'],self.key)
        frase = "off" if self.key else "on"
        self.write({'data': frase})
        self.flush()