# -*- coding: utf-8 -*-
"""
Created on Sun Oct 12 13:12:49 2014

@author: Usukuma
"""
from flask import render_template, jsonify
from functools import partial

def make_page(url='', name='', method=['GET'], template='', data=[], function=lambda x:x):
    return {'url':url, 'name':name, 'method': method, 'template':template, 'data':data, 'function':function};

def make_template(template_name, data):    
    return render_template(template_name, data=data)

def make_json(this_list):
    f = lambda x: dict(zip(xrange(len(x)),x)); # turns list of dicts in dict of dicts
    return jsonify(f(this_list))

def receive_ajax(func, data):
    return func(data);
    
def templater(app,pages):
    for page in pages:
        solver = partial(make_template, page['template'], page['data']);
        solver.__name__ = page['name'];    
        app.add_url_rule(rule = page['url'], methods = page['method'], view_func = solver);
        
def jsonifier(app,pages):
    for page in pages:
        solver = partial(make_json, page['data']);
        solver.__name__ = page['name'];    
        app.add_url_rule(rule = page['url'], methods = page['method'], view_func = solver);
        
def ajax_receiver(app,pages):
    for page in pages:
        solver = partial(receive_ajax, page['function']);
        solver.__name__ = page['name'];    
        app.add_url_rule(rule = page['url'], methods = page['method'], view_func = solver);