# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 11:14:26 2018

@author: Анастасия
"""

import re
import os
from collections import defaultdict
spisok = os.listdir('news')
folder = 'news'

#Первое задание
for filename in spisok: 
    new_f = os.path.join(folder, filename)
    file_read = open(new_f, 'r').read()
    new_name = re.match(r'[^.]+', filename).group() + '.txt'
    file_path = os.path.join(folder, new_name)
    text = open(file_path, 'w', encoding='cp1251')
    title = re.search(r'<title>([^<]+)</title>', file_read).group(1)
    text.write(title + "\n")
    
    clean = re.sub(title,'', file_read)
    clean = re.sub(r'<[^>]+>', ' ', clean)
    clean = re.sub(r'`|/', '', clean)
    clean = re.sub(r'\n', '', clean)
    text.write(clean)
    text.close()
    
# Второе задание
dictionary = defaultdict(int)
cols = ['найденное имя', 'количество вхождений']
f = open('table.csv', 'w')
f.write(", ".join(cols) + "\n")
for filename in spisok:
    new_f = os.path.join(folder, filename)
    file_read = open(new_f, 'r').read()
    words = re.findall(r'<w><ana lex="[А-ЯA-Z]{2,}[^<]+</ana>([^<]+)</w>', file_read)
    for name in words:
        dictionary[name] += 1

for key, value in dictionary.items():
    f.write(key + '\t')
    f.write(str(value) + '\n')
f.close()    
        
        
        
        
        
        
        
        
        
        
        
