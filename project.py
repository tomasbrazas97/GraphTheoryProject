# Tomas Brazas - G00349242
# Graph Theory 2019 Assignment
# -- Application Description/Tasks --
# 1)"Parse the regular expression from infix to postfix notation."
# 2)"Build a series of small NFA's for parts of the regular expression."
# 3)"Use the smaller NFA's to create the overall NFA."
# 4)"Implement the matching algorithm using the NFA."

# Task 1) Shunting Yard Algorithm
def shunt(infix):
    """Converts infix regular expressions to postfix notations"""
    # Special Character precendence on the stack
    specialChars = {'*':50, '+':40, '?':35, '.':30, '|':25}

    stack = ''
    postfix = ''

    # For loop that loops throughout the length of the input
    for i in infix:
        if i == '(':
            stack = stack + i
        elif i == ')':
            while stack[-1] != '(':
                postfix, stack = postfix + stack[-1], stack[:-1]
            stack = stack[:-1]
        elif i in specialChars:
            while stack and specialChars.get(i,0) <= specialChars.get(stack[-1], 0):
                postfix, stack = postfix + stack[-1], stack[:-1]
            stack = stack + i
        else:
            postfix = postfix + i

    while stack:
        postfix, stack = postfix + stack[-1], stack[:-1]

    return postfix
