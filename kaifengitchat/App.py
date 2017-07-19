#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 19:01:53 2017

@author: kaifeng
"""

import os
import web
import itchat
from sae.ext.storage import monkey

class App:
    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root, 'templates')
        self.render = web.template.render(self.templates_root)
    
    def GET(self):
        monkey.patch_all()
        uuid = itchat.get_QRuuid()
        itchat.get_QR(uuid=uuid,picDir='/s/pic/QR.png')
        return 'logging'