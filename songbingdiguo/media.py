#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 18:47:48 2017

@author: kaifeng
"""


import requests
from poster.streaminghttp import register_openers
from sae.ext.storage import monkey
import ssl

class Media(object):
    def __init__(self):
        register_openers()
    
    def upload(self,accessToken,filePath,mediaType):
        # global certificate verification
        ssl._create_default_https_context = ssl._create_unverified_context
        # let storage can use file system
        monkey.patch_all()

        img_url='https://api.weixin.qq.com/cgi-bin/material/add_material'
        payload_img={
            'access_token':accessToken,
            'type':'image'
        }
        data ={'media':open(filePath,'rb')}
        
        # global certificate verification
        ssl._create_default_https_context = ssl._create_unverified_context
        r=requests.post(url=img_url, params=payload_img, files=data, verify=False)
        dicts =r.json()
        
        try:
            media_id = dicts['media_id']
        except:
            print dicts
        
        return dicts['media_id']