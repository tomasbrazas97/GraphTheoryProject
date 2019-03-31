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

# Thompson's Construction

# NFA's to be executed
class NFA: 
    initial = None
    last = None

    # NFA constructor
    def _init_(self, initial, last):
        self.initial = initial
        self.last = last

# State in a NFA 
# Can't have more than 2 edges and label represents char inputed
class state:
    label = None
    edge1 = None
    edge2 = None

# Testing Shunting Algorithm
# print(shunt('A+B*C'))
# print(shunt('A*(B+C)'))
# print(shunt('A|B.C'))