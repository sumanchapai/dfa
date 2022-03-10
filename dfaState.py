class DFAState:

    def __init__(self, name="",  accepting=False):
        self.name = name
        self.myTransitions = {}
        self.accepting = accepting

    def addTransition(self, transitionTo, character):
        """Writes/Renames transition from self to transitionTo on character"""

        #        
        # might be troublesome in testing if char isn't string 
        #
        assert type(character) is str

        self.myTransitions[character] = transitionTo
    

    def stateToGoOnCharacter(self, character):
        """Returns the character to goto on given character"""

        # go to itself in empty character
        if character == " ":
            return self
        else:
            try:
                result = self.myTransitions[character]
            except KeyError:
                print(f"\n\nError: Transition not defined for {character} " + \
                        f"from state {self.getName()}\n\n")
                result = None
            return result

    #
    # Accessors
    #

    def isAccepting(self):
        """Returns if the state is accepting or not"""
        return self.accepting

    def getName(self):
        return self.name

    def toString(self, brief=True):
        if brief:
            return f"State: {self.getName()} {'Accepting' if self.isAccepting() else 'Rejecting'}"
        else:
            details = f"State {self.getName()} {'Accepting' if self.isAccepting() else 'Rejecting'}\n"
            for key, value in self.myTransitions.items():
                details += f'{key} -> {value.getName()}\n'
            return details
    #
    # repr
    #
    def __repr__(self):
        return self.toString()

    def __str__(self):
        return self.toString(brief=False)
