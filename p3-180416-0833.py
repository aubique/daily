#!/usr/bin/env python3
import random

listOfLetters = ['a', 'b', 'e', 'h', 'i', 'p', 'x', 'o', 'y']
randomWord = ''
randomWordReversed = ''

randomLength = random.randint(1, len(listOfLetters))
for i in range(randomLength):
	randomWord = ''.join([randomWord, random.choice(listOfLetters)])
print(randomWord + "(word)")

randomWordListed = list(randomWord)
#C: for (int i = len(array); i > -1; i--)
for i in range(len(randomWordListed) - 1, -1, -1):
	randomWordReversed = ''.join([randomWordReversed, randomWord[i]])
print(randomWordReversed + "(reversed)")
