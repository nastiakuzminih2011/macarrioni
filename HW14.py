import os
import re
file_list = os.listdir()
n = 0
m = []
for i in file_list:
    if re.match(r"^([a-zA-Zа-яА-Я0-9\(\)\-_]+\b\s*){2,}$", i):
        n += 1
        if i not in m:
            m.append(i)
            print(i)
print('count:', n)
