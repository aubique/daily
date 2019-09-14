#!/usr/bin/env python3
HOUR=60
DAY=24

try:
	variableOne = int(input())
except ValueError:
	print("That's not an integer")
	quit()

variableResult = round(variableOne/HOUR)%DAY
print("{} hours {} minutes have passed".format(variableResult, variableOne%HOUR))
