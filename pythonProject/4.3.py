import random
words=['лукойл','вишня',"кофе"]
def whatTheWord():
    word=random.choice(words)
    isp=[]
    wrongs=0
    while wrongs<8:
        zv = []
        for b in word:
            if b in isp:
                zv.append(b)
            else:
                zv.append('*')
        print("Угадайте слово: ", " ".join(zv))
        if "".join(zv)==word:
            print("Вы выиграли! Это слово: ", "".join(zv))
            return
        input_letter=input('Введите букву: ')
        if not input_letter.isalpha():
            print( 'Вы ввели что-то не то..')
            print('Использованные быквы: ', ", ".join(isp))
            continue
        if  input_letter in isp:
            print( 'Вы уже вводили эту букву')
            print('Использованные быквы: ', ", ".join(isp))
            continue
        isp.append(input_letter)
        if not input_letter in word:
            wrongs+=1
            print("Неправильная буква! Ошибок: ",wrongs)
    print("Вы проиграли! Загаданное слово было: ",(word))



whatTheWord()