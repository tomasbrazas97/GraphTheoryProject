# Tomas Brazas - G00349242
# Graph Theory 2019 Assignment
# -- Application Description/Tasks --
# 1)"Parse the regular expression from infix to postfix notation."
# 2)"Build a series of small NFA's for parts of the regular expression."
# 3)"Use the smaller NFA's to create the overall NFA."
# 4)"Implement the matching algorithm using the NFA."

# Shunting Yard Algorithm
def shunt(infix):
    """Converts infix regular expressions to postfix notations"""
    # Special Character precendence on the stack
    specialChars = {'*':50, '+':40, '?':35, '.':30, '|':25}

    # Stores characters and operators in order of precendence 
    stack = ''
    # Stores characters and operators into a postfix notation
    postfix = ''

    # For loop that loops throughout the length of the input
    for i in infix:
        # Brackets are not used in postfix and they need to be exterminated
        if i == '(':
            # Adds '(' to the stack
            stack = stack + i
        elif i == ')':
            # Reviews the stack to see if last char is '('
            while stack[-1] != '(':
                # Adds last char to postfix
                postfix, stack = postfix + stack[-1], stack[:-1]
            # Exterminates '(' from the stack
            stack = stack[:-1]
        # Handles the special characters listed in the script
        elif i in specialChars:
            # Compares char to char in specialChars and checks the precedence 
            while stack and specialChars.get(i, 0) <= specialChars.get(stack[-1], 0):
                # Adds read chars to the stack
                postfix, stack = postfix + stack[-1], stack[:-1]
            stack = stack + i
        # Adds character to postfix notation, this handles all characters such as a-z, A-Z
        else:
            postfix = postfix + i

    while stack:
        # Adds last char to the stack
        postfix, stack = postfix + stack[-1], stack[:-1]
    # Returns full postfix
    return postfix

# --Testing Shunting Algorithm--
# print(shunt('A+B*C'))
# print(shunt('A*(B+C)'))
# print(shunt('A|B.C'))

# Thompson's Construction

# NFA's to be executed
class NFA: 
    initial = None
    last = None

    # NFA constructor
    def __init__(self, initial, last):
        self.initial = initial
        self.last = last

# State in a NFA 
# Can't have more than 2 edges and label represents char inputed
class state:
    label = None
    edge1 = None
    edge2 = None

def compile(postfix):
    """Compiles a postfix regular notation into a NFA"""
    nfastack = []
 
    for c in postfix:
        if c == '.':
            # Pop 2 NFAs off the stack
            NFA2 = nfastack.pop()
            NFA1 = nfastack.pop()
            # Connect first NFAs last state to the seconds initial state
            NFA1.last.edge1 = NFA2.initial
            # Push the new NFA to the stack
            nfastack.append(NFA(NFA1.initial, NFA2.last))
        
        # Or
        elif c == '|':
            # Pop 2 NFAs off the stack
            NFA2 = nfastack.pop()
            NFA1 = nfastack.pop()
            # Create a new initial state, connect it to initial states of
            # the two NFAs popped from the stack
            initial = state()
            initial.edge1 = NFA1.initial
            initial.edge2 = NFA2.initial
            # Create a new last state, connecting the last states of
            # the two NFAs popped from the stack to the new last state
            last = state()
            NFA1.last.edge1 = last
            NFA2.last.edge1 = last
            # Push the new NFA to the stack
            nfastack.append(NFA(initial, last))
        
        # 0 or more
        elif c == '*':
            # Pop a single NFA from the stack
            NFA1 = nfastack.pop()
            # Create new initial and last states
            initial = state()
            last = state()
            # Merge the new initial state to NFA1s initial state and to the new last state
            initial.edge1 = NFA1.initial
            initial.edge2 = last
            # Merge the old last state to the new last state and to NFA1s initial state
            NFA1.last.edge1 = NFA1.initial
            NFA1.last.edge2 = last
            # Push the new NFA to the stack
            nfastack.append(NFA(initial, last))
        
        # 1 or more
        elif c == '+':
            # Pop a single NFA from the stack
            NFA1 = nfastack.pop()
            # Create new initial and last states
            initial = state()
            last = state()
            # Merge the new initial state to NFA1s initial state
            initial.edge1 = NFA1.initial
            # Merge the old last state to the new last state and to NFA1s initial state
            NFA1.last.edge1 = NFA1.initial
            NFA1.last.edge2 = last
            # Push the new NFA to the stack
            nfastack.append(NFA(initial, last))
        
        # 0 or 1
        elif c == '?':
            # Pop a single NFA from the stack
            NFA1 = nfastack.pop()
            # Create new initial and last states
            initial = state()
            last = state()
            # Merge the new initial state to NFA1s initial state and to the new last state
            initial.edge1 = NFA1.initial
            initial.edge2 = last
            # Merge the old last state to the new last state
            NFA1.last.edge2 = last
            # Push the new NFA to the stack
            nfastack.append(NFA(initial, last))
        
        else:
            # Create new initial and last states
            last = state()
            initial = state()
            # Merge the initial state and the last state labelled c
            initial.label = c
            initial.edge1 = last
            # Push the new NFA to the stack
            nfastack.append(NFA(initial, last))
    return nfastack.pop()

# Checks the edges of the states and returns the set of states that are connected to state
def followEdge(state):
    """Return the set of states that can be reached from state following edge arrows"""
    # Create a new set, with state as its only member
    states = set()
    states.add(state)

    # Checks if states label is a special char
    if state.label is None:
        # Check if edge1 is directed to a state
        if state.edge1 is not None:
            # If there's an edge1 follow it
            states |= followEdge(state.edge1)
        # Check if edge2 is directed to a state
        if state.edge2 is not None:
            # If there's an edge2 follow it
            states |= followEdge(state.edge2)
    # Return states
    return states

def match(infix, string):
    """Matches output string to infix regular expression"""
    # Shunt and compile the regular expression
    postfix = shunt(infix)
    NFA = compile(postfix)
    # Current set of states and next set of states
    currentstate = set()
    nextstate = set()
    # Add the initial state to the current set
    currentstate |= followEdge(NFA.initial)
    # Loop through the characters in the string
    for s in string:
        # Loop through the current set of states
        for c in currentstate:
            # Check if that state has label s
            if c.label == s:
                # Add the edge1 state to the next set
                nextstate |= followEdge(c.edge1)
        # Set currentstate to nextstate, and clear out nextstate
        currentstate = nextstate
        nextstate = set()
    # Check if the last state is in the set of current sets
    return (NFA.last in currentstate)

# --TESTING--
# '*' char test
#testList = [
#    ('a*', ''),
#    ('a*', 'a'),
#    ('a*', 'aaaa')
#]
# Test data in the '*' list
#print('Test "*" operator')
#for exp, res in testList: 
#    print(match(exp, res), exp, res)

# '+' char test
#testList = [
#    ('a+a', ''),
#    ('a+a', 'a'),
#    ('a+a', 'aaaa')
#]
# Test data in the '+' list
#print('Test "+" operator')
#for exp, res in testList: 
#    print(match(exp, res), exp, res)

# '?' char test
# testList = [
#    ('c?', ''),
#    ('c?', 'c'),
#    ('c?', 'ccc')
#]
# Test data in the '?' list
# print('Test "?" operator')
# for exp, res in testList: 
#     print(match(exp, res), exp, res)

# '|' char test
# testList = [
#     ('a|b', 'a'),
#     ('a|b', 'aa'),
#     ('a|b', 'b')
# ]
# Test data in the '|' list
# print('Test "|" operator')
# for exp, res in testList: 
#     print(match(exp, res), exp, res)

# '.' char test
# testList = [
#   ('a.b', 'a'),
#    ('a.b', 'ab'),
#    ('a.b', 'aa')
#]
# Test data in the '.' list
#print('Test "." operator')
#for exp, res in testList: 
#    print(match(exp, res), exp, res)

