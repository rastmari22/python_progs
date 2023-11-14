
from func5_8 import *
def gameover():
    global wrongs, word, isp,MAX_WRONGS
    if wrongs==MAX_WRONGS:
        print(f'Вы проиграли! Это было слово: {word}')
        return True
    if word==display_word(word, isp) and word!='':
        print(f'Вы выиграли! Это было слово: {word}')
        return True
    return False

def play_game():
    global word,isp,wrongs
    word = choose_word()
    isp = []
    wrongs = 0

    while not gameover():
        w=display_word(word, isp)
        print("Угадайте слово: ",w )
        # print("Уже использованные буквы: ", ", ".join(guessed_letters))

        input_letter = get_guess()

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
