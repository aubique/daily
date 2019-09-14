#!/usr/bin/env python3
#p3_181001_2026.py
# Composition lesson
# https://younglinux.info/oopython/arrangement.php

STR_WIDTH   = "WIDTH"
STR_LENGTH  = "LENGTH"
STR_HEIGHT  = "HEIGHT"
STR_SQUARE  = "SQUARE"
STR_SURFACE = "SURFACE"

# Parent class for any square objects
class SquareObject:
    def __init__(self, w, l):
        self.width  = w
        self.length = l
        self.calculateSquare()
    def calculateSquare(self):
        self.square = self.width * self.length
    def displaySquare(self):
        displayFunc(STR_SQUARE, self.square)
    def getValues(self):
        self.width  = inputDataFunc(STR_WIDTH)
        self.length = inputDataFunc(STR_LENGTH)
        self.calculateSquare()
    def displayValues(self):
        displayFunc(STR_WIDTH, self.width)
        displayFunc(STR_LENGTH, self.length)

class Room(SquareObject):
    def __init__(self, w, l, h):
        print("\nRoom")
        self.height = h
        self.wd     = []
        SquareObject.__init__(self, w, l)
        self.calculateSquare()
    def calculateSquare(self):
        self.square = 2 * self.height * (self.width + self.length)
    def addWD(self, w, h):
        self.wd.append(WinDoor(w, h))
    # Creating a list of items for the room
    def addWD2(self):
        print("adding new WD to the room...")
        newObjWD = WinDoor(0, 0)
        newObjWD.getValues()
        self.wd.append(newObjWD)
    # Calculate how much surface is left with no items
    def workSurface(self):
        new_square = self.square
        for item in self.wd:
            new_square -= item.square
        return new_square
    def displaySurface(self):
        displayFunc(STR_SURFACE, self.workSurface())
    def getValues(self):
        self.height = inputDataFunc(STR_HEIGHT)
        SquareObject.getValues(self)
    def displayValues(self):
        SquareObject.displayValues(self)
        displayFunc(STR_HEIGHT, self.height)

# Class of room items
class WinDoor(SquareObject):
    def __init__(self, w, l):
        print("\nCreating a new WD:")
        SquareObject.__init__(self, w, l)

# Class for wallpaper rolls
class WallpaperRoll(SquareObject):
    def __init__(self, w, l):
        print("\nA roll of wallpaper:")
        SquareObject.__init__(self, w, l)
    # Calculate how much rolls we need for the left surface (without items)
    def calculateAmount(self, roomObj):
        return roomObj.workSurface() / self.square

def inputDataFunc(s):
    return float(input("Enter value of {}: ".format(s)))

def displayFunc(s, v):
    print("Value of {} = {}".format(s, v))

def main():
    kitchen = Room(6, 3, 2.7)
    kitchen.displaySquare()

    kitchen.getValues()
    kitchen.displaySquare()

    kitchen.addWD2()
    kitchen.displaySurface()

    roll = WallpaperRoll(1, 2.7)
    roll.getValues()

    print(roll.calculateAmount(kitchen))

if __name__ == '__main__':
    main()
