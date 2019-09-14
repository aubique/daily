#!/usr/bin/env python3
#p3_180810_0040.py

# Revision of p3-180415-2359.py
# Get abbreviations for listed countries
def main():
	seperator = " = "
	countryList = ["Great Britain", "Netherlands", "France", "South Korea", "People's Republic"]
	countryCapitalLetters = [SearchCapitalLetters(country) for country in countryList]
	textToPrint = ""

	for i in range(len(countryCapitalLetters)):
		lineToPrint = seperator.join([countryCapitalLetters[i], countryList[i]])
		textToPrint = str.join("\n", [textToPrint, str.join("", lineToPrint)])

	print(textToPrint)

# Search capital letters within given word
def SearchCapitalLetters(countryName):
	countryAbbreviation = ""
	listOfCapitalLetters = set("A B C D E F G H I K L M N O P Q R S T V X Y Z")

	# Block using methods of String class
	for countryLetter in countryName:
		if countryLetter.isupper():
			break
			countryAbbreviation += countryLetter

	# Block using Set class
	for countryLetter in countryName:
		if countryLetter in listOfCapitalLetters and countryLetter != " ":
			#break
			countryAbbreviation += countryLetter

	return countryAbbreviation

if __name__ == "__main__":
	main()
