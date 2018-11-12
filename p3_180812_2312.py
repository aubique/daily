#!/usr/bin/env python3
#p3_180812_2312.py
import re

# Determine date and print it
def main():
	dictOfMonths = dict(zip([
	"January", "February", "March", "April",
	"May", "June", "July", "August", "September",
	"October", "November", "December"
	],list(range(1, 13))))

	userDate = getUserDate()
	determineDate(dictOfMonths, userDate)

# Get slices of user-date and print the date using dictionary
def determineDate(dictOfMonths, data):
	dayData = int(data[0:2])
	monthData = int(data[3:5])
	yearData = int(data[6:10])

	for monthKey, monthNum in dictOfMonths.items():
		if monthNum == monthData:
			break

	print("{} day of {} and {} year".format(dayData, monthKey, yearData))

# Get date from user and check whether the date format is correct or not
def getUserDate():
	datePattern = re.compile("^(\d{2}[\/\-\.]){2}\d{4}$")

	# Loop-and-a-half-construction to make sure one execution is performed
	while True:
		userDate = input("Enter the date (xx/mm/yyyy):")

		if datePattern.fullmatch(userDate) != None:
			break
		else:
			print("Incorrect date format. Try again.")

	return userDate

if __name__ == '__main__':
	main()
