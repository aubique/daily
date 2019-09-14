#!/usr/bin/env python3
#p3_180923_2105.py

# Example with ARGS
def main():
    argList = list()
    while True:
        argument = input()
        if argument == "":
            break
        argList.append(argument)
    print(argList)

if __name__ == '__main__':
    main()
