# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 10:53:04 2018

@author: Анастасия
"""

n = input()
n = n.split()
v = 'bcdfghjklmnpqrstvwxz'
trans = ''
for i in n:
    for m in i:
        if m.lower() in v:
            m = m + 'aig'
        trans += m
    trans += ' '
print(trans)