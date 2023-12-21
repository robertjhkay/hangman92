# Hangman

# Table of contents
1. [Introduction](#introduction)
2. [Installation](#section2)
3. [File Structure](#section3)
4. [License Information](#section4)

## 1. Introduction <a name="introduction"></a>
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

## 2. Installation <a name="section2"></a>
The repository for this program can be copied using the following command:

```
git clone https://github.com/robertjhkay/hangman92.git

```

To use the final program run the following:

```
python milestone_5.py
```
This program will work on python 3.

## 3. File Structure <a name="section3"></a>
milestone_2.py contains variables for the game.

milestone_3.py contains the functions check_guess and ask_for_input. The check_guess function will take the guessed letter as an argument and check if the letter is in the word. The ask_for_input will iteratively check if the input is a valid guess.

milestone_4.py contains the python class Hangman. It defines the attributes of the game as well as methods that update these attributes once play starts.

milestone_5.py initiates the game using the function play_game which requires a list of words as an input.

## 4. License Information <a name="section4"></a>
MIT License

Copyright (c) [2023] [Robert Kay]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to  the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
