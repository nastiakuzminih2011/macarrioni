# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 21:14:42 2018

@author: Анастасия
"""

import re
f = open('wiki.html', encoding='utf-8').read()
new = re.sub(r'диноз.вр(?=(а|у|ом|е|ы|ов|ам|ами|ах|\b))', 'кот', f)
new = re.sub(r'Диноз.вр(?=(а|у|ом|е|ы|ов|ам|ами|ах|\b))', 'Кот', new)
text = open('new.html', 'w', encoding='utf-8')
text.write(str(new))
text.close()
