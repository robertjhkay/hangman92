import random

class Hangman:

    def __init__(self, word_list):
        self.word_list = word_list
        self.list_of_guesses = []
        self.num_letters = 26
        self.num_lives = 5
        self.word = random.choice(word_list)
        self.word_guessed = ['_']*len(self.word)

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print("Good guess! {} is in the word.".format(guess))
            for i in range(0, len(self.word)):
                if self.word[int(i)] == guess:
                    self.word_guessed[i] = guess
            self.num_letters -= 1
        else:
            print("Sorry, {} is not in the word.".format(guess))
            self.num_lives -= 1
            print("You have {} lives left".format(self.num_lives))
        

    def ask_for_input(self):
        while True:
            guess = input("Please choose a single letter. ")
            if not (guess.isalpha() and len(guess) == 1):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.word_guessed.append(guess)

Hangman.ask_for_input(Hangman(['apple', 'banana', 'cocunut']))
