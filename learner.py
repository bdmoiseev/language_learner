# -*- coding: utf8 -*-

from random import randint, random, shuffle

def found(input, cur):
    for word in cur[1:len(cur)]:
        if input == word:
            return True
    return False

def randomLearner(n, range1, range2):
    priorities = [1.0]*n
    while True:
        priorities = [p/sum(priorities) for p in priorities]
        rand = random()
        cur_numb = 0
        iterator = priorities[0]
        while iterator <= rand:
            cur_numb += 1
            iterator += priorities[cur_numb]
        cur_numb = min(cur_numb, n-1)
        cur = f[range1 + cur_numb].split()
        incorrect = checkOneWord(cur)
        if incorrect == 0:
            priorities[cur_numb] /= n
        else:
            priorities[cur_numb] *= n*incorrect

def checkOneWord(cur):
    correct = 0
    incorrect = 0
    while correct == 0:
        input = raw_input(cur[0])
        if input == "q":
            exit()
        if input == "show":
            stroka = ""
            for word in cur:
                stroka += " " + word
            print stroka
            continue
        if found(input, cur):
            print "correct!"
            correct = 1
        else:
            print "incorrect, please try again!"
            incorrect += 1
    return incorrect

def allRepeater(n, range1, range2):
    sequence = range(range1, range2 + 1)
    shuffle(sequence)
    incorrect = 0
    for i in range(range1, range2 + 1):
        print str(i) + ": "
        cur =f[sequence[i]].split()
        if checkOneWord(cur) != 0:
            incorrect += 1
    print "You have (out of " + str(n) + "):"
    print str(incorrect) + " - incorrect"
    print str(n - incorrect) + " - correct"

def Cycle(n):
    print "Hello! There is " + str(n) + " words in vocabulary"
    r = raw_input("Wanna choose range?(y/n)")
    if r == "y":
        range1 = int(raw_input("please, choose left range")) - 1
        range2 = int(raw_input("please, choose right range")) - 1
    elif r == "n":
        range1 = 0
        range2 = n-1
    elif r == "q":
        quit()
    else:
        Cycle(n)
    n1 = range2 - range1 + 1
    choice = raw_input("please, input mode:\nl - learner\nr - repeater\n")
    if choice == "l":
        randomLearner(n1, range1, range2)
    elif choice == "r":
        allRepeater(n1, range1, range2)
        Cycle(n)
    elif choice == "q":
        exit()
    else:
        Cycle(n)

f = open("vocabulary.txt", "r").readlines()
n = len(f)
Cycle(n)

