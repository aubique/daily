#!/usr/bin/env python3
#p3_180908_2229.py
# Compare skills of the workers

import random

MAX_SKILL = 5
MIN_SKILL = 1

class Person:
    def __init__(self, name=None, surname=None, skill=1):
        self.name = name
        self.surname = surname
        self.skill = skill
    def __del__(self):
        print("Goodbye, mr.{}".format(self.surname))
    def displayInfo(self):
        print("Name: {}\t| Surname: {}\t| Skill: {}".format(
        self.name, self.surname, self.skill))

def main():
    worker1 = Person("Grigory", "Temiryazev", getRand())
    worker2 = Person("Steve", "Goldstein", getRand())
    worker3 = Person("Michael", "Kimchi", getRand())
    workerList = [worker1, worker2, worker3]
    [worker.displayInfo() for worker in workerList]
    unskiller = compareSkills(workerList)
    displayConclusion(unskiller)
    del unskiller
    input()

def getRand():
    return random.randint(MIN_SKILL, MAX_SKILL)

def displayConclusion(worker):
    print("Mr. {} ({}) is the most unskilled out of our team".format(
        worker.surname, worker.skill))

def compareSkills(listOfWorkers):
    lowest = 99
    for worker in listOfWorkers:
        if worker.skill < lowest:
            lowest = worker.skill
            unskilledWorker = worker
    return unskilledWorker

if __name__ == '__main__':
    main()
