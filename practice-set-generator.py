import os
from random import randrange, choice

# User input
number_of_words = 10000
min_word_length = 3
max_word_length = 5
characters = "ujlo"
filename = "ujlo.txt"


output = ""
character = ""

for i in range(number_of_words):
    for j in range(randrange(min_word_length, max_word_length + 1)):
        available_characters = characters.replace(character, "")
        character = choice(characters)
        output += character
    output += " "

f = open(filename, 'w')
f.write(output)
f.close()
