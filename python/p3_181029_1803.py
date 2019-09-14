#!/usr/bin/env python3
#p3_181029_1803.py
# Translating words in the file

ONE     = 'Один'
TWO     = 'Два'
THREE   = 'Три'
FOUR    = 'Четыре'
FIVE    = 'Пять'

class Translation():
    def __init__(self, fileToRead, fileToWrite):
        self.f1 = open(fileToRead, 'rt')
        self.f2 = open(fileToWrite, 'wt')
    def __del__(self):
        self.f1.close()
        self.f2.close()
    def translateData(self):
        # read a whole file without the last symbol
        # and split it by carriage return to get a list of strings
        data = self.f1.read()[:-1].split('\\n')
        dictionary = self.getEnRuDict()
        #[self.disp(dictionary[dataWord]) for dataWord in data if dataWord in dictionary]
        for dataWord in data:
            if dataWord in dictionary:
                self.f2.write(dictionary[dataWord]+'\n')
    def getEnRuDict(self):
        dictEn = ['One', 'Two', 'Three', 'Four', 'Five']
        dictRu = [ONE, TWO, THREE, FOUR, FIVE]
        return dict(zip(dictEn, dictRu))
    def disp(self, text):
        print(text)

class Numbers():
    def __init__(self, pathToFile):
        self.f1 = open(pathToFile, 'rt')
        self.sum = self.countSum()
    def __del__(self):
        self.f1.close()
    def countSum(self):
        prev = totalSum = 0
        numberList = list()
        rawData = self.f1.read()
        # Read letter by letter with index-counting
        for index, char in enumerate(rawData):
            # If there is a WP pull the number out of slice[prev_WP:current_WP]
            # Then update prev_WP, current_WP and increase $totalSum
            if char == ' ':
                number = int(rawData[prev:index])
                numberList.append(number)
                prev = index + 1
                totalSum += number
        return totalSum

def launchTranslation():
    file1 = Translation('files/dataEn.txt', 'files/dataRu.txt')
    file1.translateData()
    del(file1)

def launchCounting():
    file1 = Numbers('files/nums.txt')
    print(file1.sum)
    del(file1)

def main():
    launchTranslation()
    #launchCounting()

if __name__ == '__main__':
    main()
