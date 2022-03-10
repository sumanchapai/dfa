class DFA:

    #
    # Constructor
    #

    def __init__(self, name='', states=[], startState=None):
        self.setName(name)
        self.setStartState(startState)
        self.setStates(states)
    
    #
    # Process
    #

    def process(self, subject):
        """Returns if the subject string is accepted or not"""

        currentState = self.getStartState()
        for character in subject:
            currentState = currentState.stateToGoOnCharacter(character)

            # make sure we aren't in undefined state
            assert currentState != None

        result = currentState.isAccepting()

        if result:
            print(f'I accept {subject}')
        else:
            print(f'I reject {subject}')

        return result

    #
    # Mutators
    #

    def setStartState(self, state):
        self.startState = state

    def setName(self, name):
        self.name = name

    def setStates(self, states):
        self.states = states

    def addState(self, state):
        self.states.append(state)

    #
    # Accessors
    #
    
    def toString(self):
        return f"DFA: {self.name}"

    def getName(self):
        return self.name

    def getStates(self):
        return self.states

    def getStartState(self):
        return self.startState

    #
    # Repr & To String
    #

    def __repr__(self):
        return self.toString()

    def __str__(self):
        return self.toString()
