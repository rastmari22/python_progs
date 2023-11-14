import random

words=['лукойл','вишня',"кофе"]
word=random.choice(words)

isp=[]
wrongs=0
zv=''
def start_word():
    zv = []
    for b in word:
        if b in isp:
            zv.append(b)
        else:
            zv.append('*')
    stw = " ".join(zv)
    print("Угадайте слово: ",stw )

    return stw

def input_letter():
    global zv, wrongs

    if "".join(zv) == word:
        gameover()

    input_letter = input('Введите букву: ')


    try:
        if not input_letter.isalpha():
            raise ValueError(f'Вы ввели что-то не то..\nИспользованные буквы: {", ".join(isp)}')
    except ValueError as err:
        print(err)
    else:
        if input_letter in isp:
            print('Вы уже вводили эту букву')
            print('Использованные быквы: ', ", ".join(isp))
        isp.append(input_letter)
        if not input_letter in word:
            wrongs += 1
            print("Неправильная буква! Ошибок: ", wrongs)

def gameover():
    global wrongs,zv
    if "".join(zv) == word:
        print("Вы выиграли! Это слово: ", "".join(zv))
        return
    if wrongs==8:
        print("Вы проиграли! Загаданное слово было: ", (word))
        return

while wrongs < 8:
    sw=start_word()
    input_letter()
gameover()
