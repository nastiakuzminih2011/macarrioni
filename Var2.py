with open('freq.txt', encoding='utf-8') as f:
    text = f.read()
    text_splited = text.split('\n')
    
    VB = 'гл '
    VB2 = 'перех '
    for line in text_splited:
        if VB in line and VB2 in line:
            print(line)
    text_spl = text_splited.split('|')
    print(text_spl)

    chast = 'част '
    s = []
    for i in text_splited:
        if chast in i:
            print(i)
    
    word = ' '
    s = []
    while word != '':
        word = str(input('Введите слово: '))
        word_ex = word + ' '
        for m in text_splited:
            if word_ex in m and word_ex[0] == m[0]:
                print(m)
                s.append(m)
            else:
                print('Слово не найдено. ')
            
