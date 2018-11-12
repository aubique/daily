#!/usr/bin/env python3
#p3_180810_2059.py

def main():
#	countVariousNumbers("1 2 3 4 5 1 2 1 2 7 3")
	intersectionOfMany("1 2 6 4 5 7", "10 2 3 4 8")

def intersectionOfMany(numbers1, numbers2):
	setOfNumbers1 = set(numbers1)
	setOfNumbers2 = set(numbers2)
	listOfInterNumbers = list(setOfNumbers1.intersection(setOfNumbers2))
	listOfInterNumbers.sort(reverse=True)

	try:
		listOfInterNumbers.remove(" ")
	except ValueError:
		pass

	print(listOfInterNumbers)

def countVariousNumbers(numbers):
	setOfNumbers = set(numbers)
	setOfNumbers.discard(" ")
	print("Number of various numbers is {}".format(len(setOfNumbers)))

if __name__ == '__main__':
	main()
