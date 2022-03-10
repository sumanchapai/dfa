from dfa import DFA
from dfaState import DFAState

#
# Machine to accept {a, b}* with odd lengths of A and even lengths of B
# example: a, abb, abaab, etc.
#

#
# States
#

# abbreviation: eAoB = even A odd B

eAeB = DFAState("even A even B", False) 
eAoB = DFAState("even A odd B", False) 
oAoB = DFAState("odd A odd B", False) 
oAeB = DFAState("odd A even B", True) 

#
# transitions
#

# even A even B
eAeB.addTransition(eAoB, 'b')
eAeB.addTransition(oAeB, 'a')

# even A odd B
eAoB.addTransition(eAeB, 'b')
eAoB.addTransition(oAoB, 'a')

# odd A odd B
oAoB.addTransition(eAoB, 'a')
oAoB.addTransition(oAeB, 'b')

# odd A even B
oAeB.addTransition(eAeB, 'a')
oAeB.addTransition(oAoB, 'b')


# Machine
machine = DFA("oddA evenB", \
        states=[eAeB, eAoB, oAoB, oAeB],\
        startState=eAeB)


print('\nTestOutYourselfUntilYouEnter: Enter Key')

toTest = input(": ")
while toTest != "":
    machine.process(toTest)
    toTest = input(": ")
