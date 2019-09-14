#!/usr/bin/env python3
# p3-180420-1324.py
import timeit

def main():
	wordExample = "abrocadabreaux"
	listOfVowels = ['a', 'e', 'i', 'o', 'u']
	
	wordExampleListed = list(wordExample)
	lengthOfWord =  len(wordExampleListed)
	upperCaseWordListed = [0] * lengthOfWord
	for i in range(lengthOfWord):
		upperCaseWordListed[i] = wordExampleListed[i].upper()
	upperCaseWordOne = ''.join(upperCaseWordListed)
	#print(upperCaseWordOne, ": old algorithm")
	
	upperCaseWordTwo = ''.join(letter.upper() for letter in list(wordExample))
	print(upperCaseWordTwo, ": new algorithm")
	
	listOfVowels = listOfVowels + list(''.join(vowel.upper() for vowel in listOfVowels))
	sortedWord = ''.join(letter for letter in upperCaseWordTwo if letter in listOfVowels)
	print(sortedWord, ": vowels taken out of the word")

if __name__ == "__main__":
	main()
