# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 11:07:12 2018

@author: 凯风
"""

from interface import Voltage5, Voltage220

class VoltageAdapter(Voltage220, Voltage5):
    
    def output5V(self):
        src = self.output220V()
        print("适配器工作开始，适配电压")
        dst = src / 44
        print("适配完成后输出电压：" + str(dst))
        return dst