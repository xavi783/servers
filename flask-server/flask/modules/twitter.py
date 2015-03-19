# -*- coding: utf-8 -*-
"""
Created on Sun Oct 12 16:55:12 2014

@author: Usukuma
"""
from twython import Twython
import json
from os import path

config = open( path.join(path.dirname(__file__),'config/twitter.json') ); # personal folder with sensitive info
prop   = json.load(config);
config.close();

APP_KEY = prop['auth']['key'];
APP_SECRET = prop['auth']['secret'];

twitter = Twython(APP_KEY, APP_SECRET)
auth = twitter.get_authentication_tokens();

OAUTH_TOKEN = auth['oauth_token']
OAUTH_TOKEN_SECRET = auth['oauth_token_secret']
print auth['auth_url']

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

final_step = twitter.get_authorized_tokens(6280780);