# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 10:20:21 2018

@author: Анастасия
"""

n = input()
n = n.split()
v = 'aeiou'
dot = """!.,?-"""
trans = ''
for i in n:
    i = i.lower()
    if i[0] in v:
        if i[-1] in dot:
            trans += i[:-1] + 'way' + i[-1]
        else:
            trans += i + 'way '
    else:
        if len(i)> 1:
            if i[1] in v:
                if i[-1] in dot:
                    trans += i[1:-1] + i[0] + 'ay' + i[-1]
                else:
                    trans += i[1:] + i[0] + 'ay '
            else:
                if i[-1] in dot:
                    trans += i[2:-1] + i[0:2] + 'ay' + i[-1]
                else:
                    trans += i[2:] + i[0:2] + 'ay '
        else:
            trans += i +'ay '
print(trans[0].upper() + trans[1:])