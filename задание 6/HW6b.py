abc = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
with open('word_HW6.txt', 'w', encoding='utf-8') as f:
    a = " "
    while a != '':
        a = str(input('Введите слово: '))
        a_good = True
        for k in a:
            if k not in abc:
                a_good = False
        if a_good and len(a) >= 2 and a[-2] == 'e' and a[-1] == 'd':
            f.write(a + '\n')
        elif a_good == False:
            print('Можно использовать только латинский алфавит.')
