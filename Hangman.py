import time
# import this
from random import randint
import string


# Intro
alphabet = list(string.ascii_lowercase)
input_name = input("What's your name? ")
print("Hello " + input_name + ", " + " let's play Hangman!")


# Begin Game

list_of_words = ["yasuo", "morgana", "ziggs", "ashe", "trundle", "mordekaiser"]

secret_word = list_of_words[randint(0, len(list_of_words)-1)]

guess_letter = ""
lives = 5
secret_word_hidden = [len(secret_word)*"__ "]
print("The secret word contains {} letters and you have {} lives".format(len(secret_word), lives))
print(secret_word_hidden)
# add function that will allow upper and lower case letter to be correct

while lives > 0:
    guess_letter = input("Guess: ")
    if guess_letter.lower() not in secret_word:
        print("wrong!")
    else:
        print("correct!")


print("GG EZ")

guess = input("Guess a letter: ")

