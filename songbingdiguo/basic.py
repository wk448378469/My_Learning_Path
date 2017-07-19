#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 18:51:28 2017

@author: kaifeng
"""

import urllib
import json

class Basic:
    def __init__(self):
        self.__accessToken = ''
        self.__letfTime = 0
    
    def __real_get_access_token(self):
        appId = 'wx5d9e84f692bec6b8'
        appSecret = 'fb38e7900643729a82add7971f1e5040'
        
        postUrl = ('https://api.weixin.qq.com/cgi-bin/token?grant_type=' 
                   'client_credential&appid=%s&secret=%s' % (appId,appSecret))
        
        urlResp = urllib.urlopen(postUrl)
        returnContent = urlResp.read()
        urlResp = json.loads(returnContent)
              
        self.__accessToken = urlResp['access_token']
        self.__letfTime = urlResp['expires_in']

        
    def get_access_token(self):
        if self.__letfTime < 10:
            self.__real_get_access_token()
        return self.__accessToken