import random
word_list = ['apple', 'pear', 'orange','banana', 'kiwi']
word = random.choice(word_list)
print(word)

guess = input("Please choose a single letter ")

if len(guess) == 1:
    print("Good guess!")
else: print("Oops! That is not a valid input.")