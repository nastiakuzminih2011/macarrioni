# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 11:57:11 2018

@author: Анастасия
"""

import re
addr = 'wiki.html'
x = open(addr, encoding="utf8").read()
matc = re.search(r'<tbody>[^<]*<tr>[^<]*<td[^>]*>Семейство[^<]*</td>[^<]*<td[^>]*>[^<]*<a[^>]*>([^<]*)</a>', x)
f = open('file.txt','w', encoding='utf-8')
f.write(str(matc.group(1)))
f.close()
