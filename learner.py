# -*- coding: utf8 -*-

import sys
from random import randint, random, shuffle
sys.path.insert(0, 'util')
import argparse

def weightedChoise(weights):
    weights = [w / sum(weights) for w in weights]
    rand_value = random()

    s = 0.0
    for i in range(len(weights)):
        s += weights[i]
        if s >= rand_value:
            return i
    return len(weights) - 1

def randomLearner(vocabulary):
    priorities = [1.0] * len(vocabulary)
    while True:
        priorities = [p / sum(priorities) for p in priorities]
        choise = weightedChoise(priorities)
        word = vocabulary[choise]

        incorrect = checkOneWord(word)
        if incorrect == 0:
            priorities[choise] /= len(vocabulary)
        else:
            priorities[choise] *= len(vocabulary) * incorrect

def checkOneWord(word):
    incorrect = 0
    while True:
        input = raw_input(word[0] + ' ')

        if input == "q":
            exit()
        if input == "s" or input == "":
            print " ".join(word)
            incorrect += 1
            continue
        if input in word:
            print "correct!"
            break
        else:
            print "incorrect, please try again!"
            incorrect += 1
    return incorrect

def allRepeater(words):
    sequence = range(len(words))
    shuffle(sequence)
    incorrect = 0
    for i in range(len(words)):
        print str(i) + ": "
        choise = words[sequence[i]]
        if checkOneWord(choise) != 0:
            incorrect += 1
    print "You have (out of " + str(len(words)) + "):"
    print str(incorrect) + " - incorrect"
    print str(len(words) - incorrect) + " - correct"

if __name__ == '__main__':
    argument_parser = argparse.ArgumentParser(add_help=True)
    argument_parser.add_argument('-v', '--vocabulary', action='store', required=True,
        metavar='VOCABULARY_FILE', dest='vocabulary_path', help='file with vocabulary')
    argument_parser.add_argument('-r', '--range', action='store', required=False, nargs=2,
        metavar=('LEFT', 'RIGHT'), dest='range', type=int, help='range of vocubulary to learn')
    argument_parser.add_argument('-m', '--mode', action='store', required=True,
        metavar=('MODE'), dest='mode', help='program mode: r (repeater) or l (learner)')
    arguments = argument_parser.parse_args()

    vocabulary = [v.split() for v in open(arguments.vocabulary_path, "r").readlines()]
    
    # Detecting range
    if arguments.range:
        if (arguments.range[0] < 0 or arguments.range[1] > len(vocabulary) or arguments.range[0] > arguments.range[1]):
            raise RuntimeError("Bad range values: %d %d for %d words in dictionary" %
                (arguments.range[0], arguments.range[1], len(vocabulary)))
        vocabulary = vocabulary[arguments.range[0] : arguments.range[1] + 1]

    if arguments.mode == "l":
        randomLearner(vocabulary)
    elif arguments.mode == "r":
        allRepeater(vocabulary)
    else:
        raise RuntimeError("Bad program mode: " + arguments.mode)
