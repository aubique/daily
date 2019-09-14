#!/usr/bin/env python3
#p3_180923_2259.py
# Strategy game with soldiers and heroes
# https://younglinux.info/oopython/inheritance.php

import random

class Human:
    count = 0
    def __init__(self, objectID, team):
        type(self).count += 1
        self.objectID = objectID
        self.team = team
    def __del__(self):
        type(self).objectID -= 1
    def countUp(self):
        self.num += 1

class Soldier(Human):
    def __init__(self):
        self.team = random.randint(1, 2)
        self.objectID = Human.count
        Human.__init__(self, self.objectID, self.team)
    def follow(self, heroObj):
        print("Soldier(id:{},team:{}) is following Hero(id:{},team:{},level:{})".format(
            self.objectID, self.team, heroObj.objectID,
            heroObj.team, heroObj.level))
    def display(self):
        print("ID: {}\t|\tTeam: {}\t|\tLevel: {}".format(
            self.objectID, self.team, self.level))

class Hero(Human):
    def __init__(self, team):
        Human.__init__(self, team)
        self.level = 0
    def levelUp(self):
        self.level += 1
        return self.level
    def display(self):
        print("ID: {}\t|\tTeam: {}".format(self.objectID, self.team))

def main():
    #soldierList = [Soldier(i, random.randint(1, 2)) for i in range(2, 7)]
    soldierList = [Soldier() for i in range(7)]
    team1, team2 = fillUpTeams(soldierList)
    hero, followingSoldier = compareTeams(team1, team2)
    hero.levelUp()
    followingSoldier.follow(hero)
    displayList(soldierList)

def compareTeams(listTeam1, listTeam2):
    if len(listTeam1) > len(listTeam2):
        biggestList = listTeam1
    else:
        biggestList = listTeam2
    hero = biggestList[0]
    randomSoldier = biggestList[random.randint(1, len(biggestList)-1)]
    return hero, randomSoldier

def fillUpTeams(soldierList):
    team1 = list([Hero(1)])
    team2 = list([Hero(2)])
    for soldier in soldierList:
        if soldier.team == 1: team1.append(soldier)
        elif soldier.team == 2: team2.append(soldier)
    print("Team #1: {} | Team #2: {}".format(len(team1), len(team2)))
    return team1, team2

def displayList(listed):
    for item in listed:
        print("ID: {}\t|\tTeam: {}".format(item.objectID, item.team))

if __name__ == '__main__':
    main()
