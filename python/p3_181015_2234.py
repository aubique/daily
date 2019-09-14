#!/usr/bin/env python3
#p3_181015_2234.py
# Capitalize each word

def handler(text):
    newString = list()
    string = text.split()
    for word in string:
        if word != string[0]: newString.append(' ')
        newString.append(capitalize(word))
    print(''.join(str(char) for char in newString))

def capitalize(word):
    ordLetter = ord(word[0])
    firstLetter = chr(ordLetter - 32)
    newWord = firstLetter + word[1:]
    return newWord

def main():
    textInput = input()
    handler(textInput)

if __name__ == '__main__':
    main()
