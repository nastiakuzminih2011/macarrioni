# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 12:46:31 2018

@author: Анастасия
"""
import random

with open('Word.txt', 'r', encoding='utf-8') as f:
    text = f.read().split()
    
text[0] = text[0][1:]

d = dict(zip(text[:-1:2], text[1::2]))

a = random.choice(list(d.keys()))
b = input(a +'...')
coun = 1
while b != d[a]:
    print('Не угадал.')
    print('Количество попыток: '+ str(coun))
    coun += 1
    b = input('...')
print('Правильно.')
print('Количество попыток: '+ str(coun))