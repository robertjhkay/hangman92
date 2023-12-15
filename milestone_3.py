import random
word_list = ['apple', 'pear', 'orange','banana', 'kiwi']
word = random.choice(word_list)

guess = input("Please choose a single letter. ")

def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print("Good guess! {} is in the word.".format(guess))
    else: print("Sorry, {} is not in the word. Try again.".format(guess))

def ask_for_input(guess):
    x = guess.isalpha()
    y = len(guess)
    while (x == False) or (y != 1):
        guess = input("Invalid letter. Please, enter a single alphabetical character. ")
        x = guess.isalpha()
        y = len(guess)
    check_guess(guess)

ask_for_input(guess)