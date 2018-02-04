# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 04:53:23 2018

@author: Анастасия
"""

def name():
    x = input('Enter file: ')
    return x
    
def readf(x):
    f = open(x)
    read = f.read()
    s = """,.“”!"?:;"""
    for i in s:
        if i in s:
            read = read.replace(i, ' ')
    splited = read.split()
    return splited

def word_ous(x):
    dict = {'ous':0, 'len':0}
    for words in x:
        if words[-3:] == 'ous':
            dict['ous'] += 1
            dict['len'] += len(words)
    return(dict)
def mid(x,y):
    m = int(x) / int(y)
    return m
    

dict = word_ous(readf(name()))
print('Кол-во прилагательных с суффиксом -ous: ', dict['ous'])
print('Средняя длина: ', round(mid(dict['len'], dict['ous']), 2))