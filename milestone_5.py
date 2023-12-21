import random

'''
The following creates the class hangman. It defines an object based on a list of possible words.

'''

class Hangman:

        def __init__(self, word_list, num_lives):
            self.word_list = word_list
            self.list_of_guesses = []
            self.num_lives = num_lives
            self.word = random.choice(word_list)
            self.word_guessed = ['_']*len(self.word)
            self.num_letters = len(set(self.word))

        '''
        The following methods check only credible guesses are permissible and update attributes accordingly. 

        '''

        def check_guess(self, guess):
            guess = guess.lower()
            if guess in self.word:
                print("Good guess! {} is in the word.".format(guess))
                for i in range(0, len(self.word)):
                    if self.word[i] == guess:
                        self.word_guessed[i] = guess
                self.num_letters -= 1
                print("The word is... {}".format(self.word_guessed))
            else:
                print("Sorry, {} is not in the word.".format(guess))
                print("The word is... {}".format(self.word_guessed))
                self.num_lives -= 1
                print("You have {} lives left".format(self.num_lives))
            
        def ask_for_input(self):
            while self.num_letters != 0 and self.num_lives > 0:
                guess = input("Please choose a single letter. ")
                if not (guess.isalpha() and len(guess) == 1):
                    print("Invalid letter. Please, enter a single alphabetical character.")
                elif guess in self.list_of_guesses:
                    print("You already tried that letter!")
                else:
                    self.check_guess(guess)
                    self.list_of_guesses.append(guess)

'''
The following function utilizes the hangman object and initializes the game.

'''

def play_game(word_list):
    game = Hangman(word_list, 5)
    terminate = 0
    while terminate == 0:
        if game.num_lives == 0:
            print("You lost!")
            terminate += 1
        elif game.num_letters > 0:
            game.ask_for_input()
        elif game.num_lives > 0 and game.num_letters == 0:
            print("Congratulations. You won the game!")
            terminate += 1
                   
if __name__ == "__main__":

    play_game(['apple', 'pear', 'orange','banana', 'kiwi'])