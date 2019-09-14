#!/usr/bin/env python3
#p3_180814_1531.py

# Create and read text files
def main():
    fileName = "tempFile.txt"
    createTestFile(fileName)
    readTestFile(fileName)

# Create file to read it later
def createTestFile(pathToFile):
    listOfNumbersRU = ["Раз", "Два", "Три", "Четыре"]
    fileToCreate = open(pathToFile, 'w')
    fileToCreate.writelines(listOfNumbersRU)
    fileToCreate.close()

def readTestFile(pathToFile):
    listOfNumbersEN = ["One", "Two", "Three", "Four"]
    fileToRead = open(pathToFile, 'r')
    fileToRead.close()
    # TODO rewrite file with russian list

if __name__ == '__main__':
    main()
