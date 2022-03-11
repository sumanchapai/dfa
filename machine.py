from dfa import DFA
from dfaState import DFAState

eAeB = DFAState("eAeB", False) 
eAoB = DFAState("eAoB", False) 
oAoB = DFAState("oAoB", False) 
oAeB = DFAState("oAeB", True) 

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

