import random
word_list = ['apple', 'pear', 'orange','banana', 'kiwi']
word = random.choice(word_list)
print(word)

guess = input("Please choose a single letter ")

def input_check(x):
    if len(x) == 1:
        print("Good guess!")
    else: print("Oops! That is not a valid input.")