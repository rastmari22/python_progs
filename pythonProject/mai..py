import random
import re
import string
import wordlist
import game

def play_game():
    chosen_word = random.choice(wordlist.words)
    game.initialize(chosen_word)
    while not game.game_over():
        user_input = get_user_input()
        game.process_input(user_input)

def get_user_input():
    while True:
        user_input = input("Введите букву: ")
        return user_input.lower()

if __name__ == '__main__':
    play_game()
