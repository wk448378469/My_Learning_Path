# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 11:25:27 2018

@author: 凯风
"""

from adapter import VoltageAdapter

class Mobile(object):
    def charging(self, voltage5):
        if (voltage5.output5V() == 5):
            print("\n电压刚刚好5V， 手机开始充电")
        else:
            print("\n你这是要搞事情啊~")



if __name__ == "__main__":
    mobile = Mobile()
    mobile.charging(VoltageAdapter())

