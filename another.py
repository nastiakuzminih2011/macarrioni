a = 'abracadabra'
for i in range(len(a) // 2 + len(a) % 2):
    print(a[i:len(a)-i])
