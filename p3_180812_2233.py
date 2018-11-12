#!/usr/bin/env python3
#p3_1800812_2233.py

# test
def main():
	CountLenOfInterSets()

def CountLenOfInterSets():
	setA = set([1, 3, 2])
	setB = set([4, 3, 2])
	setC = set()
	setC = setA.intersection(setB)
	print(len(setC))

if __name__ == '__main__':
	main()
