# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 04:53:23 2018

@author: Анастасия
"""

import re

def name():
    x = input('Enter file: ')
    return x
    
def readf(x):
    f = open(x)
    text = f.read()
    text = re.sub('\W',' ',text).lower()
    splited = text.split()
    return splited

def word_ous(x):
    dicto = {'ous':0, 'len':0}
    for words in x:
        if words[-3:] == 'ous':
            dicto['ous'] += 1
            dicto['len'] += len(words)
    return(dicto)

def mid(x,y):
    m = x / y
    return m

dicto = word_ous(readf(name()))
print('Кол-во прилагательных с суффиксом -ous: ', dicto['ous'])
print('Средняя длина: ', round(mid(dicto['len'], dicto['ous']), 2))