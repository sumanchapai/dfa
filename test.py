from dfa import DFA
from dfaState import DFAState
from machine import machine

print('\nTestOutYourselfUntilYouEnter: Enter Key')

toTest = input(": ")
while toTest != "":
    machine.process(toTest)
    toTest = input(": ")
