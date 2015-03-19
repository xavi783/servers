# -*- coding: utf-8 -*-
"""
Created on Mon Oct 06 12:12:54 2014

@author: jserrano
"""

from flask import Flask, request, jsonify
import modules.mydb as dao
import modules.templater as tp

app = Flask(__name__);
    
#------------------------------------------------------------------------------
    
ids   = zip(xrange(1,21,5), xrange(5,21,5))
tags  = lambda x: str(x[0])+'_'+str(x[1]);
lnker = lambda x: '/table'+str(x[0])+'_'+str(x[1])+'/';

#unique names
links  = lambda ids: [{'type':0, 'href':lnker(x),'name':'Tabla de ciudades '+str(x[0])+' - '+str(x[1])} for x in ids];
links2 = lambda ids: [{'type':1, 'href':lnker(x)+'data/','name':'Datos de ciudades '+str(x[0])+' - '+str(x[1])} for x in ids];
starts     = [tp.make_page('/','index',['GET'],'index.html',links(ids)+links2(ids))];
tables     = [tp.make_page(lnker(x),'table'+tags(x),['GET'],'table_test.html',dao.retrieve_data(x[0],x[1])) for x in ids];
table_data = [tp.make_page(lnker(x)+'data/','data_table'+tags(x),['GET'],'table_test.html',dao.retrieve_data(x[0],x[1])) for x in ids];

pages  = starts+tables;
t_data = table_data;

#receiving pages
@app.route('/set_intervals/', methods=['POST'])
def get_ajax():
    d   = map(lambda x,y,t: request.args.get(x,y,type=t), ['min','max','step'], [1,20,5], [int,int,int]);
    ids = zip(xrange(d[0],d[1],d[2]), xrange(d[2],d[1],d[2]));
    return jsonify({'ids':ids})

# for static pages or info (only depending on server not client)
tp.templater(app,pages);
tp.jsonifier(app,t_data); # sending dasta by ajax, processing on client

if __name__ == "__main__":
    app.run(debug='true')