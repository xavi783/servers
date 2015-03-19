# -*- coding: utf-8 -*-
"""
Created on Wed Oct 01 09:12:14 2014

@author: jserrano
"""
import pp
import urllib
import urllib2
import bs4
import string
from functools import partial

alphabet = string.uppercase;
prs = [bs4.BeautifulSoup(urllib.urlopen('http://www.advfn.com/nyse/newyorkstockexchange.asp?companies='+letter)) for letter in alphabet]

def tag_by_id(clases,tag):
    return (tag.get('id') in clases) if tag.has_attr('id') else False

tickers = []
for page in prs:
    for tt in page.find_all(class_ = lambda x: x in ['ts0','ts1']):
        tickers.append(str([ch for ch in tt.children][1].getText()))
ntickers = len(tickers)

def get_quote(ticker):
    # Last, Beta, Volume, BPA
    prs2 = bs4.BeautifulSoup(urllib2.urlopen('https://es.finance.yahoo.com/q?s='+ticker));
    try:
        quote = (float(str(prs2.select('.time_rtq_ticker > span')[0].getText()).replace(',','.')), \
                 float(str(prs2.select('td.yfnc_tabledata1')[5].getText()).replace(',','.')), \
                 float(str(prs2.select('td.yfnc_tabledata1')[10].getText()).replace('.','').replace(',','.')), \
                 float(str(prs2.select('td.yfnc_tabledata1')[13].getText()).replace(',','.')))
    except:
        quote = []
    return quote

# cogemos los quotes de todos los tickers
server = pp.Server()
jobs   = [server.submit(get_quote, (arg,), modules=("bs4","urllib2")) for arg in tuple(tickers)]
quotes = [q() for q in jobs];

# id de tickers existentes en yahoo (existen si su quote no es [])
id = [];
__ = [(id.append(i) if q != [] else []) for q, i in zip(quotes,xrange(len(quotes)))]
if len(tickers)==ntickers:
    tickers = [tickers[i] for i in id] # tickers que estan en yahoo (A GUARDAR)
    quotes  = [quotes[i] for i in id] # tickers que estan en yahoo (A GUARDAR)
    stocks = [tuple([tk]+list(q[:])) for tk,q in zip(tickers,quotes)];
    

filters = [lambda x: abs(x[2])>0.95 and abs(x[2])<1.05,\
           lambda x: x[1]>0 and x[1]<20, \
           lambda m,x: x[4] > m]
bpa_mean = reduce(lambda y,x: mean([y,x]), map(lambda x: x[4], stocks))
bpa_90   = np.percentile(map(lambda x: x[4], stocks),90);
#fstocks = filter(partial(filters[2], bpa_mean), stocks)
fstocks = filter(filters[1], filter(partial(filters[2], bpa_90), stocks))
len(fstocks)

