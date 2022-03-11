def drawDFA(machine):
    states = machine.getStates()
    start = machine.getStartState()
    
    print("digraph G {")

    ###
    ### Transitions for states
    ###

    # create a map between states ids and names
    mapIdName = {}
    for state in states:
        mapIdName[id(state)] = state.getName()

    for state in states:
        myName = state.getName()

        # Label for state
        print(f'{id(state)} [label="{myName}"];')
        
        my_transitions = state.getTransitions()

        # serialize data
        my_transition_chars = my_transitions.keys()
        sanitized_transitions = {}

        for char in my_transition_chars:
           sanitized_transitions[char] = id(my_transitions[char])

        # optimized valKey
        optimizedValKey = optimize(sanitized_transitions)
        
        ###
        ### this optimization is to avoid drawing individual arrows going to
        ### same state for different transitions
        ###
        for key, values in optimizedValKey.items():
            print(f"{id(state)} -> {key} [label={','.join(values)}];")

    print("}")




###
### if keyValDict = {"a": "q1", "b": "q2", "c": "q1"}
### what you must return is like this :
### {"q1": ["a", "c"], "q2": ["b"]
###
def optimize(keyValDict):

    valKeyDict =  {}
    values = list(keyValDict.values())

    ### initialize
    for value in values:
        valKeyDict[value] = []

    for key, value in keyValDict.items():
        valKeyDict[value].append(key)

    return valKeyDict

def testOptimize():
    a = {}
    assert optimize(a) == {}

    a = {'suman': 'chapai'}
    assert optimize(a) == {'chapai': ['suman']}

    a = {'suman': 'chapai', 'hari': 'chapai'}
    assert optimize(a) == {'chapai': ['suman', 'hari']}

    a = {'suman': 'chapai', 'hari': 'chapai', 'shyam': 'narayan'}
    assert optimize(a) == {'chapai': ['suman', 'hari'], 'narayan': ['shyam']}
