# -*- coding: utf-8 -*-
"""
Created on Wed Nov 26 14:17:47 2014

@author: jserrano
"""
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class GpioValueHandler(FileSystemEventHandler):
    def __init__(self, path):
        self.path = path        
        
    def on_modified(self,event):
        with open(self.path+'/value','r') as fd:
            value = fd.read()
        if callbacks.has_key('on_modified'):
            callbacks['on_modified'](value)            
        print "{}: {} = {}".format(event.event_type,self.path,value)

class GpioDirectionHandler(FileSystemEventHandler):
    def __init__(self, path):
        self.path = path        
        
    def on_modified(self,event):
        with open(self.path+'/direction','r') as fd:
            value = fd.read()
        if callbacks.has_key('on_modified'):
            callbacks['on_modified'](value)            
        print "{}: {} = {}".format(event.event_type,self.path,value)

class GpioDriveHandler(FileSystemEventHandler):
    def __init__(self, path, callbacks):
        self.path = path        
        
    def on_modified(self,event):
        with open(self.path+'/direction','r') as fd:
            value = fd.read()
        if callbacks.has_key('on_modified'):
            callbacks['on_modified'](value)
        print "{}: {} = {}".format(event.event_type,self.path,value)

class GpioHandler():

    def __init__(self,path,callbacks):
        self.__path = path
        self.__callbacks = {'value':{}, 'direction':{}, 'drive':{}}
        self.__callbacks.extends(callbacks)
        self.__observer = Observer()
        self.__value = GpioValueHandler(self.__path,self.__callbacks['value'])
        self.__direction = GpioDirectionHandler(self.__path,self.__callbacks['direction'])
        self.__drive = GpioDriveHandler(self.__path,self.__callbacks['drive'])
        observer.schedule(self.__value, self.__path, recursive=False)
        observer.schedule(self.__direction, self.__path, recursive=False)
        observer.schedule(self.__drive, self.__path, recursive=False)

    def run(self):
        observer = Observer()
        observer.schedule(event_handler, path, recursive=False)
        observer.start()
        observer.join()

    @property
    def observer(self):
        return self._observer

#if __name__ == "__main__":
#    path = '/home/ubuntu/gpio/gpio30'
#    event_handler = MyHandler(path)
#    observer = Observer()
#    observer.schedule(event_handler, path, recursive=False)
#    observer.start()
#    observer.join()