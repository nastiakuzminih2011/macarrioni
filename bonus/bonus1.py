# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 09:01:56 2018

@author: Анастасия
"""

n = 1
s = 0
l = []
while n != '':
    n = input()
    if n == '':
        break
    n = n.replace(' ', '')
    if '.' in n:
        n = float(n)
        s += n
        l.append(n)
    else:
        n = int(n)
        s += n
        l.append(n)
min = l[0]
max = l[0]
for i in l:
    if min > i:
        min = i
    if max < i:
        max = i
print('max =',max,'min =', min,'average =', s/2)