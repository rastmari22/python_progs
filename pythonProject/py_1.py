MAX_ATTEMPTS = 8

chosen_word = ''
guessed_letters = []
wrong_attempts = 0

def initialize(word):
    global chosen_word, guessed_letters, wrong_attempts
    chosen_word = word
    guessed_letters = []
    wrong_attempts = 0

def process_input(letter):
    global guessed_letters, wrong_attempts
    if letter in guessed_letters:
        print(f"Вы уже использовали букву '{letter}'. Попробуйте другую.")
    else:
        guessed_letters.append(letter)
        if letter in chosen_word:
            print(f"Буква '{letter}' есть в загаданном слове!")
            print_word_progress()
            if word_guessed():
                print("Вы выиграли!")
        else:
            wrong_attempts += 1
            print(f"Буквы '{letter}' нет в загаданном слове.")
            print(f"Неверные попытки: {wrong_attempts}/{MAX_ATTEMPTS}")
            if wrong_attempts >= MAX_ATTEMPTS:
                print("Вы проиграли!")

def word_guessed():
    return set(chosen_word) == set(guessed_letters)

def print_word_progress():
    progress = "".join([letter if letter in guessed_letters else "_" for letter in chosen_word])
    print(f"Угаданное слово: {progress}")

def game_over():
    return word_guessed() or wrong_attempts >= MAX_ATTEMPTS
