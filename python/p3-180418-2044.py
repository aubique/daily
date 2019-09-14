#!/usr/bin/env python3
#Swimming in the pool excercise

def getValue():
	try:
		valueInput = int(input())
	except ValueError:
		print("Wrong type")
		quit()
	else:
		return valueInput

def calcResidue(length, coordinate):
	halfOfLength = length / 2
	residue = length - coordinate
	if residue < halfOfLength:
		return residue
	else:
		return coordinate

N = getValue()
M = getValue()
short = getValue()
long = getValue()
shortCalculated = short
longCalculated = long

if M < N:
	shortCalculated = calcResidue(M, short)
else:
	longCalculated = calcResidue(N, long)

if shortCalculated < longCalculated:
	print(shortCalculated)
else:
	print(longCalculated)
