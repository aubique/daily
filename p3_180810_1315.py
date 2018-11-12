#!/usr/bin/env python3
#p3_180810_1315.py

def main():
	quitSequence = ["quit", "q", "quit()", "exit", "exit()"]
	condition = True

	while condition:
		stringToPrint = input("Enter something over here: ")
		for tempString in quitSequence:
			if stringToPrint == tempString:
				condition = False
		print("The length of the string is {}".format(len(stringToPrint)))
	print("Exiting...")

if __name__ == "__main__":
	main()
