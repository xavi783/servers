# -*- coding: utf-8 -*-
"""
Created on Fri Oct 10 09:01:07 2014

@author: jserrano

test con DB 'world' from MySQL
"""
import MySQLdb as mql
import json
from os import path

config = open( path.join(path.dirname(__file__),'config/properties.json') ); # personal folder with sensitive info
prop   = json.load(config);
config.close();

def retrieve_data(minid, maxid): 
    
    cnn = mql.connect(host   = prop['db']['host'],
                      user   = prop['db']['user'],
                      passwd = prop['db']['passwd'],
                      db     = prop['db']['name']);
    cr  = cnn.cursor();    
    cr.execute('SELECT * FROM world.city where id >= {} and id <= {};'.format(minid, maxid));    
    
    ncols = [0,2,3,1]
    rows  = [[row[i] for i in ncols] for row in cr.fetchall()];
    cols  = [cr.description[i][0] for i in ncols];    
    cr.close(); cnn.close();    
    return [dict(zip(cols,r)) for r in rows]