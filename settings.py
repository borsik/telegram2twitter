#!/usr/bin/env python

# https://my.telegram.org/auth and @BotFather

telegram = {'channel': '',  # channel name
        'token': '',  # your bot token
        'api_id': 0,
        'api_hash': '',
        'phone': ''}

#get this from https://apps.twitter.com/

twitter = {'consumer_key': '',
            'consumer_secret': '',
            'access_token': '',
            'access_token_secret': ''}

util = {'start': "2018-01-01 00:00:00",     #date from old posts will be tweeted
        'end': '2018-01-20 00:00:00',       #date until old posts will be tweeted
        'format': '%Y-%m-%d %H:%M:%S',      #date format
        'delay': 1}                         #delay time between tweets for client.py