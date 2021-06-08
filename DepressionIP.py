# -*- coding: utf-8 -*-
"""
Created on Fri May  7 23:53:01 2021

@author: kusal
"""

from pydantic import BaseModel
# 2. Class which describes Bank Notes measurements
class DepressionIP(BaseModel):
    Gender: float 
    Age: float 
    Totaltimef: float
    Deepsleepf: float
    REMSf: float
    LightSleepf: float