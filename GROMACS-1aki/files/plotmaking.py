# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 11:08:18 2019

@author: garci
"""

import matplotlib.pyplot as plt
import numpy as np
import csv
import xlwings as xw
import pandas
import os

import sys
sys.path.append('C:/Users/garci/Dropbox (Personal)/scripts/python_import/')
from process_output import readxl

path = r'C:\Users\garci\Dropbox (Personal)\scripts\GROMACS-learning\GROMACS-1aki/files/'
file = 'data.xlsx'
readxl(path,file,sheet='Sheet1')
readxl(path,file,sheet='Sheet2')
readxl(path,file,sheet='Sheet3')
readxl(path,file,sheet='Sheet4')
readxl(path,file,'Rg',sheet='Sheet5')
