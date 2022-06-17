from db import words
from random import randint, random, shuffle

def jumble(word):
    jumbled = list(word)
    shuffle(jumbled)

    return ''.join(jumbled)

randomNumber = randint(0,500)
randomWord = words[randomNumber]
jumbledWord = jumble(randomWord['word'])

print(randomNumber)
print(jumbledWord)
print(randomWord['word'])

