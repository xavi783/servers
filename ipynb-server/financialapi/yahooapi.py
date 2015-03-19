# -*- coding: utf-8 -*-
"""
Created on Wed Nov 05 15:20:59 2014

@author: jserrano
"""
import pprint
import requests
import pandas as pd
import string
from StringIO import StringIO as reader

class YahooAPI(object):
    
    def __init__(self,symbols=None,names=None):
        self.__dict__['Ask']="a"
        self.__dict__['AverageDailyVolume']="a2"
        self.__dict__['AskSize']="a5"
        self.__dict__['Bid']="b"
        self.__dict__['Ask_RealTime']="b2"
        self.__dict__['Bid_RealTime']="b3"
        self.__dict__['BookValue']="b4"
        self.__dict__['BidSize']="b6"
        self.__dict__['Change_PercentChange']="c"
        self.__dict__['Change']="c1"
        self.__dict__['Commission']="c3"
        self.__dict__['Currency']="c4"
        self.__dict__['Change_RealTime']="c6"
        self.__dict__['AfterHoursChange_RealTime']="c8"
        self.__dict__['Dividend_Share']="d"
        self.__dict__['TrailingAnnualDividendYield']="d0"
        self.__dict__['LastTradeDate']="d1"
        self.__dict__['TradeDate']="d2"
        self.__dict__['Earnings_Share']="e"
        self.__dict__['DilutedEPS']="e0"
        self.__dict__['ErrorIndication_returnedforsymbolchanged_invalid']="e1"
        self.__dict__['EPSEstimateCurrentYear']="e7"
        self.__dict__['EPSEstimateNextYear']="e8"
        self.__dict__['EPSEstimateNextQuarter']="e9"
        self.__dict__['TradeLinksAdditional']="f0"
        self.__dict__['FloatShares']="f6"
        self.__dict__['DaysLow']="g"
        self.__dict__['HoldingsGainPercent']="g1"
        self.__dict__['AnnualizedGain']="g3"
        self.__dict__['HoldingsGain']="g4"
        self.__dict__['HoldingsGainPercent_RealTime']="g5"
        self.__dict__['HoldingsGain_RealTime']="g6"
        self.__dict__['DaysHigh']="h"
        self.__dict__['MoreInfo']="i"
        self.__dict__['OrderBook_RealTime']="i5"
        self.__dict__['YearLow']="j"
        self.__dict__['MarketCapitalization']="j1"
        self.__dict__['SharesOutstanding']="j2"
        self.__dict__['MarketCap_RealTime']="j3"
        self.__dict__['EBITDA']="j4"
        self.__dict__['ChangeFrom52WeekLow']="j5"
        self.__dict__['PercentChangeFrom52WeekLow']="j6"
        self.__dict__['YearHigh']="k"
        self.__dict__['LastTrade_RealTime_WithTime']="k1"
        self.__dict__['ChangePercent_RealTime']="k2"
        self.__dict__['LastTradeSize']="k3"
        self.__dict__['ChangeFrom52WeekHigh']="k4"
        self.__dict__['ChangeInPercentFromYearHigh']="k5"
        self.__dict__['LastTrade_WithTime']="l"
        self.__dict__['LastTrade_PriceOnly']="l1"
        self.__dict__['HighLimit']="l2"
        self.__dict__['LowLimit']="l3"
        self.__dict__['DaysRange']="m"
        self.__dict__['DaysRangeRealtime']="m2"
        self.__dict__['MovingAverage50days']="m3"
        self.__dict__['MovingAverage200days']="m4"
        self.__dict__['ChangeFrom200DayMovingAverage']="m5"
        self.__dict__['PercentChangeFrom200DayMovingAverage']="m6"
        self.__dict__['ChangeFrom50DayMovingAverage']="m7"
        self.__dict__['PercentChangeFrom50DayMovingAverage']="m8"
        self.__dict__['Name']="n"
        self.__dict__['Notes']="n4"
        self.__dict__['Open']="o"
        self.__dict__['PreviousClose']="p"
        self.__dict__['PricePaid']="p1"
        self.__dict__['ChangeinPercent']="p2"
        self.__dict__['Price_Sales']="p5"
        self.__dict__['Price_Book']="p6"
        self.__dict__['ExDividendDate']="q"
        self.__dict__['ExDividendDate']="q0"
        self.__dict__['PER']="r"
        self.__dict__['DividendPayDate']="r1"
        self.__dict__['PER_RealTime']="r2"
        self.__dict__['PEGRatio']="r5"
        self.__dict__['Price_EPSEstimateCurrentYear']="r6"
        self.__dict__['Price_EPSEstimateNextYear']="r7"
        self.__dict__['Symbol']="s"
        self.__dict__['SharesOwned']="s1"
        self.__dict__['Revenue']="s6"
        self.__dict__['ShortRatio']="s7"
        self.__dict__['LastTradeTime']="t1"
        self.__dict__['TradeLinks']="t6"
        self.__dict__['TickerTrend']="t7"
        self.__dict__['TargetPrice1yr']="t8"
        self.__dict__['Volume']="v"
        self.__dict__['HoldingsValue']="v1"
        self.__dict__['HoldingsValue_RealTime']="v7"
        self.__dict__['Range52Week']="w"
        self.__dict__['DaysValueChange']="w1"
        self.__dict__['DaysValueChangeRealtime']="w4"
        self.__dict__['StockExchange']="x"
        self.__dict__['DividendYield']="y"
        self.__dict__['TrailingAnnualDividendYieldInPercent']="y0"

    def get_fields(self,fields):
        _fields=[];
        for f in fields:
            if f in self.__dict__.keys():
                _fields.append(f)
        return _fields
        
    def get_data(self,symbols,fields):
        _symbols = string.join(symbols,sep='+')
        _fields = string.join([self.__dict__.get(f) for f in self.get_fields(fields)],sep='');
        _data = pd.read_csv(reader(requests.get('http://finance.yahoo.com/d/quotes.csv?s='+_symbols+'&f='+_fields).text),header=None)
        _data.columns = self.get_fields(fields)
        return _data

    def __repr__(self):
        pprint.pprint(self.__dict__)
        return ''
        
fields = ['Symbol','Name','EBITDA','Volume','My_OwN-FiElD']
o = YahooAPI()
o.get_fields(fields)
data = o.get_data(['GOOG'],fields)

