#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 18:51:28 2017

@author: kaifeng
"""

import media
from basic import Basic
# from sae.storage import Bucket,Connection

def test():

    picurl = '/s/models/test.jpg'
    
    myMedia = media.Media()
    
    accessToken = Basic().get_access_token()
    
    return myMedia.upload(accessToken,picurl,'image')