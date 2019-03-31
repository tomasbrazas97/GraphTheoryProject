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








