# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 12:29:31 2018

@author: Анастасия
"""
import random

def name1(b):
    name1 = random.choice(b)
    return name1.capitalize()
    
def verb(c):
    verb = random.choice(c)
    return verb[0:-2] + 'ла'
    
def verb2(c):
    verb2 = random.choice(c)
    return verb2[0:-2] +'л'
def verbpr(c):
    verbpr = random.choice(c)
    return verbpr[0:]
    
def name(a):
    name = random.choice(a)
    return name[0:-1] + 'е'
    
def nameY(M):
    nameY = random.choice(M)
    return nameY[:] + 'у'
    
def namecc(a):
    nameA = random.choice(a)
    return nameA
def add(a):
    add = random.choice(a)
    return add[0:-2] + 'в'
    
f = open('File.txt')
text = f.read()
a = text.split()    

f = open('File2.txt')
text = f.read()
ver = text.split()    

f = open('File3.txt')
text = f.read()
Maxi = text.split()    

f = open('File4.txt')
text = f.read()
acc = text.split()

f = open('File5.txt')
text = f.read()
acc1 = text.split()    

f = open('File6.txt')
text = f.read()
acc2 = text.split()    

f = open('File7.txt')
text = f.read()
acc3 = text.split()    

f = open('File8.txt')
text = f.read()
con = text.split(', ')    

f = open('File9.txt')
text = f.read()
adverb = text.split()    

f = open('File10.txt')
text = f.read()
adv = text.split()    

f = open('File11.txt')
text = f.read()
adr = text.split()    


s = []
s.append(Maxi)
s.append(a)
ac = []
ac.append(acc)
ac.append(acc1)
ac.append(acc2)
ac.append(acc3)

num = 0
while num <= 5:
    i = random.randint(0, 1)
    result = name1(s[i])
    ad = random.randint(0,1)
    if ad == 0:
        result += ', ' + add(adr) + ','
    if i == 0:
        result += ' '+ verb2(ver) + ' '
    else:
        result += ' ' + verb(ver) + ' ' 
                      
    m = random.randint(0, 1)
    d = random.randint(0,3)
    if m == 0:
        result += nameY(Maxi) + ' '
        result += namecc(ac[d]) + ', ' + namecc(con)+ ' он'
        c = random.randint(0,2)
        if c == 0:
            result += ' ' + namecc(adverb) +' ' + verb2(ver)+ ' ' 
        elif c == 1:
            result += ', ' + namecc(adv) + ', ' + verb2(ver) + ' '
        elif c == 2:
            result += ' ' + verb2(ver) + ' '
        if i == 0:
            result += 'ему' + ' '
        else:
            result += 'ей' + ' '
    else:
        result += name(a) + ' '
        result += namecc(ac[d]) + ', ' + namecc(con)+ ' она'
        c = random.randint(0,2)
        if c == 0:
            result += ' ' + namecc(adverb) + ' ' + verb(ver)+ ' ' 
        elif c == 1:
            result += ', ' + namecc(adv) + ', ' + verb(ver) + ' '
        elif c == 2:
            result += ' ' + verb(ver) + ' '
        if i == 0:
            result += 'ему' + ' '
        else:
            result += 'ей' + ' '
    d = random.randint(0,3)
    result += namecc(ac[d]) + '. '
    
    с = random.randint(0,1)
    if c == 0:        
        c == random.randint(0, 2)
        if c == 0:
            result += name1(adverb) + ' '
            if i == 0:
                result += 'он не ' + verb2(ver) 
            else:
                result += 'она не ' + verb(ver)
           
        elif c == 1:
            result += name1(adv) + ', '
            if i == 0:
                result += 'он не ' + verb2(ver) 
            else:
                result += 'она не ' + verb(ver)   
        elif c == 2 and i == 0:
            result += 'Он не ' + verb2(ver) 
        elif c == 2 and i == 1:
            result += 'Она не ' + verb(ver) 
        d = random.randint(0,3)
        result += ' ' + namecc(ac[d]) + ', '
        if d == 0:
            result += 'который '
        elif d == 1:
            result += 'которое '
        elif d == 2:
            result += 'которую '
        else:
            result += 'которые '
        i = random.randint(0,1)
        if i == 0:
            result += verb2(ver)
        else:
            result += verb(ver)
        result += ' ' + namecc(s[i]) + '. '
        print(result, end='')
        num += 2
    else:
        print(result, end='') 
        num += 1
        continue
