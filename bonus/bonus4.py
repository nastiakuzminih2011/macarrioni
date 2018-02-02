# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 10:38:25 2018

@author: Анастасия
"""

n = input()
n = n.split()
vow = 'аеёиоуыэюя'
trans = ''
for i in n:
    i = i.lower()
    for m in i:
        if m in vow:
            m = m + 'c' + m
        trans += m
    trans += ' '
print(trans[0].upper() + trans[1:])