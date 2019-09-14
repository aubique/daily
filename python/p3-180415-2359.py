#!/usr/bin/env python3

countryList = ["Unites States", "Russian Federation", "Germany", "Ireland"]
capitalLetters = [ country[0] for country in countryList ]

for i in range(len(capitalLetters)):
	lineToPrint = str.join(" stands for ", [capitalLetters[i], countryList[i]])
	print(lineToPrint)

