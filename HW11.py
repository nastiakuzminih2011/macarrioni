# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 13:58:15 2018

@author: Анастасия
"""

import re
a = input('file: ')
text = open(a, encoding='utf-8').read()
a = re.findall(r"\bсъе[а-я]+", text, re.IGNORECASE)
for w in set(a):
    print(w)