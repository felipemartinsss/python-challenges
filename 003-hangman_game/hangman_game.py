import os
import random

# create a words database
words = ['Felipe', 'Regina', 'Nina']


def present_word_characters_by_status(word, discovered):
    i = 0
    while i < len(word):
        if discovered[i]:
            print(f"{word[i]} ", end='')
        else:
            print("_ ", end='')
        i += 1
    print("\n")


def init_secret_word_discovered_status(word):
    discovered = []
    i = 0
    while i < len(word):
        discovered.append(False)
        i += 1
    return discovered


def update_word_discovered_status(word, position, discovered):
    letter_that_belong_to_word = word[position]
    for idx in range(0, len(word)):
        if word[idx] == letter_that_belong_to_word:
            discovered[idx] = True
    return discovered


def is_all_words_discovered(discovered):
    all_words_discovered = True
    for d in discovered:
        if not d:
            return False
    return all_words_discovered


def user_interaction_for_letter(word):
    letter = input('Type a letter: ')
    letter_position = word.find(letter.upper())
    return letter_position


def user_interaction_for_word(word, discovered):
    guess_word = input('Type a word: ')
    for letter in guess_word:
        letter_position = word.find(letter.upper())
        discovered = update_word_discovered_status(word, letter_position, discovered)
    return word.upper() == guess_word.upper(), discovered_status


def user_interaction(word, discovered_status, current_errors):
    prompt = 'You have two options now: '
    prompt += '\n' + '1 - Guess a letter'
    prompt += '\n' + '2 - Guess the whole word'
    prompt += '\n'
    try:
        user_input = int(input(prompt))
    except ValueError:
        print("Accepted values: 1 or 2")
        return user_interaction(word, discovered_status, current_errors)

    print("You typed: ", user_input)
    if user_input == 1:
        position = user_interaction_for_letter(word)
        if position != -1:
            print("You have a good guess")
            discovered_status = update_word_discovered_status(word, position, discovered_status)
        else:
            print("You missed one shot")
            current_errors += 1
    elif user_input == 2:
        is_guess_right, discovered_status = user_interaction_for_word(word, discovered_status)
        if is_guess_right:
            print("Congratulations, you discovered the word")
        else:
            current_errors = 6
    else:
        print("Invalid user input")
    return current_errors, discovered_status

def print_hangman_status(errors):
    hangman_parts = ["", "     o", "     |", "    /|", "    /|\\", "    /", "    / \\ \nGAME OVER!!!"]
    print("_____")
    print("     |")
    if errors >= 1:
        print(hangman_parts[1])
    else:
        print("")

    # awesome
    if 2 <= errors <= 4:
        print(hangman_parts[errors])
        print("")

    if errors < 2:
        print("")

    # awesome again
    if 5 <= errors <= 6:
        print(hangman_parts[4])
        print(hangman_parts[errors])

    if errors < 5:
        print("")


if __name__ == '__main__':
    word_to_be_discovered = random.choice(words).upper()
    max_errors = 6 # one for each body part
    current_errors = 0
    discovered_status = init_secret_word_discovered_status(word_to_be_discovered)
    while current_errors < max_errors and not is_all_words_discovered(discovered_status):
        print("Welcome to the Hangman Game")
        print_hangman_status(current_errors)
        present_word_characters_by_status(word_to_be_discovered, discovered_status)
        current_errors, discovered_status = user_interaction(word_to_be_discovered, discovered_status, current_errors)
        os.system("clear")
    present_word_characters_by_status(word_to_be_discovered, discovered_status)
    print_hangman_status(current_errors)

