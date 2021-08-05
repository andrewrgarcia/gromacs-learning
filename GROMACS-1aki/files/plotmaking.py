#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 13:12:50 2021

@author: andrew
"""

import matplotlib.pyplot as plt
import numpy as np

import pandas


def batch(sheet='Sheet1'):
    df = pandas.read_excel('data.xlsx', sheet_name = sheet, usecols = "A,B", header=None)
    
    x,y = df[0], df[1]
    
    dftit = pandas.read_excel('data.xlsx', sheet_name = sheet, usecols = "I", header=None,nrows=1)
    
    title = dftit[8].iloc[0]
    
    plt.figure()
    plt.plot(x,y)
    plt.title(title)
    plt.xlabel('Time (ps)')
    

sheetnos = np.arange(1,6)

[batch(sheet='Sheet'+str(i)) for i in sheetnos]

sheet = 'Sheet6'

df = pandas.read_excel('data.xlsx', sheet_name = sheet, usecols = "A,B,C", header=None)

x,y,y2 = df[0], df[1], df[2]

dftit = pandas.read_excel('data.xlsx', sheet_name = sheet, usecols = "I", header=None,nrows=1)

title = dftit[8].iloc[0]


plt.figure()
plt.plot(x,y,label='Equilibrated')
plt.plot(x,y2,label='Crystal')

plt.legend()
plt.title(title)
plt.xlabel('Time (ps)')
    