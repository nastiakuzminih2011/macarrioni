while True:
    a = input('Введите слово: ')
    for i in range(len(a) // 2):
        print(a[i])
    for i in range(len(a) - len(a) // 2):
        print(a[len(a) - 1 - i])
        
        
