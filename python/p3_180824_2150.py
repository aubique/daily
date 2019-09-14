#!/usr/bin/env python3
#p3_180824_2150.py

# Search synonym
def main():
    myDictionary = dict([
        ("3", ""),
        ("Hello", "Hi"),
        ("Bye", "Goodbye"),
        ("List", "Array"),
        ("Goodbye", "")
    ])
    wordToSearch = getKeySearchWord(myDictionary)
    checkDictionary(myDictionary, wordToSearch)

# Get the word we're looking for
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
