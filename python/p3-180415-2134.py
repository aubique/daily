#!/usr/bin/env python3
stringTemp1 = "The string n.01"
stringTemp2 = "String Two"

typeOfStrings = ", ".join([str(type(stringTemp1)), str(type(stringTemp2))])
#print(typeOfStrings)

listOfStrings = [stringTemp1, stringTemp2]
for currentString in listOfStrings:
	print(currentString + " = " + str(type(currentString)))
