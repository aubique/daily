#!/usr/bin/env python3
#p3_180824_2354.py

# Search synonym #2
# Format:
# Number_of_lines
# Key (space) Value
# Key_word
def main():
    num = input()
    myDictionary = getDictionary(num)
    word = input()
    #wordToSearch = getKeySearchWord(myDictionary)
    checkDictionary(myDictionary, word)

# Fill dictionary with input lines
def getDictionary(numberOfLines):
    myDictionary = dict()
    listTemp = list()

    for i in range(int(numberOfLines)):
        listTemp.append(input().split(' '))

    myDictionary = dict(listTemp)
    return myDictionary

# Get the word we're looking for
# Not used
def getKeySearchWord(synonymDict):
    keyList = list(synonymDict.keys())
    keyIndex = int(keyList[0])+1
    keyWord = keyList[keyIndex]
    return keyWord

# Get a synonym for key-word
def checkDictionary(synonymDict, keyWord):
    for wordsN1, wordsN2 in synonymDict.items():
        if wordsN1 == keyWord:
            synonymDict.update({keyWord: wordsN2})
            break
        if wordsN2 == keyWord:
            synonymDict.update({keyWord: wordsN1})
            break
    print(synonymDict[keyWord])

if __name__ == '__main__':
    main()
