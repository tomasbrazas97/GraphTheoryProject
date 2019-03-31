# GraphTheoryProject
--------------------------------------------
Tomas Brazas G00349242
Graph Theory Assignment 2019
--------------------------------------------

You must write a program in the Python programming language that can
build a non-deterministic finite automaton (NFA) from a regular expression,
and can use the NFA to check if the regular expression matches any given
string of text. You must write the program from scratch and cannot use the
re package from the Python standard library nor any other external library.

---------------------------------------------
# Infix to Postfix
---------------------------------------------
Shunting Yard Algorithm
---------------------------------------------

The first task of the project is: "Parse the regular expression from infix to postfix notation". This is done 
so that computer does not have to read and process the regular expression multiple times, it can read the postfix notation once to succesfully
process it. The Shunting Yard Algorithm was created by Edsger Dijkstra. It uses the stack to change the order of characters
in the regular expression, therefore serving as a storage structure. 

The "shunt" function in the project covers all of this. Special characters such as "+" and "." are given precedence values which determines
their execution order when the parsing begins. A for loop that continues the length of the string with if/elif/else statements is used to handle and remove 
bracket symbols and to read in special characters. The first if handles '(' character  and adds it to the stack. The first elif handles ')' character, this elif only
begins when the last value on the stack is a ')' bracket, if not apparent the stack is added to the postfix notation string and the stack is popped. Then the '(' char is removed
from stack. The second elif handles any special characters entering the stack that are present in the specialChars dictionary. While loop checks the dictionary and their precedence. The
higher the number the higher precedence the special character has. Once all have been added to the postfix notation the stack is set equal to its second last character. The else in the
function handles any characters that are not brackets or special chars and they are added to postfix notation. Characters such as a-z,A-Z,1.

Once the infix is read to the end, the postfix notation is returned.

---------------------------------------------
# Build series of small NFA's for parts of the regular expression
---------------------------------------------
Thompson's Construction
---------------------------------------------
The second task of the project is: "Build series of small NFA's for parts of the regular expression". Thompsons Construction was created by Ken Thompson.
It is used to convert a postfix notation into a "non-deterministic finite automata". 

Two classes are used in the assignment and the states that make up the NFA's. A NFA class constructor is present that initialises.
The "compile" function handles the postfix notation and turns it into NFAs. A stack is created for NFAs.

. Concatenate
-----------------------------------------------
Previous 2 characters must be together in order. 2 NFAs are popped off stack and both states are connected, nfa1 last state connects to nfa initial state and is pushed to the stack.

| Or
-----------------------------------------------
Any one of 2 characters may appear. 2 NFAs are popped off stack. New last and initial states are created for this. The initial state is merged NFAs state and the new last state.
The old last state is merged to the new last state and to the NFAs initial state. This produced NFA is pushed to stack.

+ 1 or more
------------------------------------------------
The character mst be present atleast once. NFA is popped off stack. New states are created. The new initial is joined to the NFA's initial state. Old last is merged to the new last state and to NFAs
initial. Produced NFA is pushed to stack.

* 0 or more
------------------------------------------------
The character can be present any amount of times, 0 is acceptable. NFA is popped off stack. New states are created. New initial is merged to the NFA's initial state and new last state.
Old last is merged to the new last and to NFAs initial. Produced NFA is pushed to stack.

? 0 or 1 
------------------------------------------------
The character may appear once or not at all. NFA is popped off stack. New states are created. New initial state is merged to NFAs initial and new last state.
Old last is merged to new last. Produced NFA is pushed to stack.

Normal Characters
------------------------------------------------
NFA is popped off stack. New states are created. The initial state is merged to the last state. Produced NFA is pushed to stack.

At the end, the stack should consist of one NFA.

-------------------------------------------------
# Expression Matching
-------------------------------------------------
The script contains two functions "followEdges" and "match". Followedges function "returns the set  of states that can be reached from state following edge arrows".
New set is produced with state then a for loop reviews if state has an arrow. Checks if there is edge1 and edg2 arrows and follows them. The states set is returned.

The match function matches a string to Infix expression. Infix and a string enter the function as parameters, shunt function called and changes infix to postfix. The postfix is
passed to compile function to produce finite automata. Current states and next set of states are created and are merged. For loop goes through the string. If any characters
are present, another for loop is used. This for loop loops through each state in current state set. If labels match any current states and current character of the string, followEdges function adds state to next state set.

-------------------------------------------------
References
-------------------------------------------------
1) Learnonline lecture notes
2) Web.microsoft streams
3) Stackoverflow











