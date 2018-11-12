#!/usr/bin/env python3
#p3_180907_0858.py
# Fight of warriors

import random
DECREASE_HP_STEP = 20
ORIGINAL_HP = 100
NUMBER_OF_WARRIORS = 2

class Warrior:
    hp = ORIGINAL_HP
    def __init__(self, num=None):
        self.num = num
    def getNumber(self):
        return self.num
    def setHP(self, newValue):
        self.hp = newValue
    def decreaseHP(self):
        self.hp -= DECREASE_HP_STEP
    def getHP(self):
        return self.hp

def main():
    listOfWarriors = createWarriors(NUMBER_OF_WARRIORS)
    fightWarriors(listOfWarriors, NUMBER_OF_WARRIORS)

# Create a list with n-amount of warriors
def createWarriors(rangeValue):
    warriorList = [Warrior(i) for i in range(rangeValue)]
    return warriorList

# Decrease HP from randomly picked warrior until one's dead
def fightWarriors(warriorList, numOfWarriors):
    while True:
        currentWarrior = warriorList[random.randint(0, numOfWarriors-1)]
        currentWarrior.decreaseHP()
        if currentWarrior.hp <= 0:
            displayListOfWarriors(warriorList)
            displayDeadWarrior(currentWarrior.num, currentWarrior.hp)
            break

def displayDeadWarrior(warriorIndex, health):
    print("The warrior with index {} has {} hp".format(warriorIndex, health))
    print("Game is over for him")

# Display attributes of each warrior
def displayListOfWarriors(warriorList):
    for warrior in warriorList:
        print("Warrior:{} | HP:{}".format(warrior.num, warrior.hp))

if __name__ == '__main__':
    main()
