# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 09:21:06 2018

@author: Анастасия
"""

import re
x = open('mystem.xml', encoding='utf8').read()
mtc = re.findall(r'gr="A=[(]?[,|местн|зват|парт|полн|пр|мн|ед|кр|вин|неод|им|род|дат|твор|притяж|прев|срав|од]*жен[^/>]*([^<]*)</w>',x)
f = open('new.txt', 'w', encoding='utf8')
f.write(str(mtc))
f.close()
h ='mystem.csv'
y = open(h).read()
red = re.sub(r'[<body>|<w>|<se>|<ana lex="|"|/>|</w>|gr="]*', ' ', y)
red2 = re.findall(r'(\S*)')
ff = open('new2.txt', 'w', encoding='utf-8')
ff.write(red2)
ff.close()