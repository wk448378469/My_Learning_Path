#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 19:34:51 2017

@author: kaifeng
"""
'''
import time
import itchat
from sae.ext.storage import monkey
import ssl

class itChat(object):
    
    def __init__(self):
        monkey.patch_all()
        ssl._create_default_https_context = ssl._create_unverified_context
        self.uuid = itchat.get_QRuuid()
        self.picPath = '/s/pic/QR.png'
    
    def generateQr(self):
        while self.uuid is None:
            self.uuid = itchat.getuuid()
            time.sleep(1)
        
        itchat.get_QR(uuid=self.uuid,picDir=self.picPath)
        self.output_info('Please scan the QR Code')
    
    def output_info(self,msg):
        print '[INFO] %s' % msg
    
    def checkLoging(self):
        waitForConfirm = False
        while 1:
            status = itchat.check_login(self.uuid)
            if status == '200':
                self.output_info('logging')
                break
            elif status == '201':
                if waitForConfirm:
                    self.output_info('Please press confirm')
                    waitForConfirm = True
            elif status == '408':
                self.output_info('Reloading QR Code')
                self.uuid = itchat.get_QRuuid()
                itchat.get_QR(uuid=self.uuid,picDir=self.picPath)
                waitForConfirm = False
'''