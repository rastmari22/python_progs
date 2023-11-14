# import game
# from game import word,words, wrongs,zv,s_w
# def whatTheWord():
#     global wrongs
#     # p=game.gameover()
#     while not game.gameover():
#
#         s_w=game.start_word()
#         if game.gameover(): return
#
#         print("Угадайте слово: ",word,'    ', s_w)
#
#         if "".join(zv) == word:
#             game.gameover()
#         input_letter = input('Введите букву: ')
#
#         try:
#             if not input_letter.isalpha():
#                 raise ValueError(f'Вы ввели что-то не то..\nИспользованные буквы: {game.isp_out()}')
#         except ValueError as err:
#             print(err)
#         else:
#             ispol=game.get_isp()
#             if input_letter in ispol:
#                 print('Вы уже вводили эту букву')
#                 print('Использованные быквы: ', game.isp_out())
#             else:
#                 game.to_isp(input_letter)
#                 if not input_letter in word:
#                     wrr=game.add_wrongs()
#                     print("Неправильная буква! Ошибок: ", wrr)
#
#
# whatTheWord()
import random
word = ''
isp = []
wrongs=0
def choose_word():
    words = ["яблоко", "апельсин", "банан", "груша", "киви"]
    return random.choice(words)


def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "*"
    return display


def get_guess():
    input_letter = input("Введите букву: ")
    return input_letter

def gameover():
    global wrongs, word, isp
    if wrongs==8:
        print(f'Вы проиграли! Это было слово: {word}')
        return True
    if word==display_word(word, isp):
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

        # if guess in guessed_letters:
        #     print("Вы уже ввели эту букву!")
        # else:
        #     guessed_letters.append(guess)
        #     if guess not in word:
        #         wrong_guesses += 1
        #         print("Неправильная попытка!")
        #         print("Количество неудачных попыток:", wrong_guesses)
        #
        #         if wrong_guesses >= 8:
        #             print("Вы проиграли!")
        #             break
        #
        #     if all(letter in guessed_letters for letter in word):
        #         print("Вы выиграли!")
        #         break


play_game()
