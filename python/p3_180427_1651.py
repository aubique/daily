#!/usr/bin/env python3
# p3_180427_1651.py
# 2nd letter match within string

def main(inputString):
	LETTER = 'f'
	# First item shifted from 0 to 1
	firstMatchIndex = inputString.find(LETTER) + 1
	secondMatchIndex = inputString.find(LETTER, firstMatchIndex)
	# If not an error
	if secondMatchIndex != -1:
		return secondMatchIndex
	else:
		return "No matches"

if __name__ == "__main__":
	print("Second match:", main("afasf"))
