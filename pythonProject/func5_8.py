# from game5_8 import *
import random
word = ''
isp = []
MAX_WRONGS=8
wrongs=0
def choose_word():
    words = ['лукойл','вишня',"кофе"]
    return random.choice(words)


def display_word(word, guessed_letters):
    # global word
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


