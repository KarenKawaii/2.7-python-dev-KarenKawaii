# coding: utf-8

'''
    Booleans
    For these variables, their values are True or False.
    There are important for conditional expressions and loops.

    The bool type is a subclass from int type.

    The different kind of operators to work with boolean values
    are called:

    - logical operators or conditionals.
'''

# Operators
# Description and examples.

# And operator.
print "## AND operator example ##"
print "Is fullfilled a and b?"
A = True
print "A = ", A
B = False
print "B = ", B
RES = A and B
print "RES = A and B"
print "RES = ", RES 

# Or operator.
print "## OR operator example ##"
print "Is fullfilled a or b?"
A = True
print "A = ", A
B = False
print "B = ", B
RES = A or B
print "RES = A or B"
print "RES = ", RES 

# Not operator.
print "## Not operator example ##"
print "Not a"
A = True
print "A = ", A
RES = not A
print "RES = not A"
print "RES = ", RES

# The boolean values also are the result
# of expressions that use relational operators
# Comparations between values.

# == operator
print "## == operator example ##"
print "Are a and b equals?"
A = 5
print "A = ", A
B = 3 
print "B = ", B
RES = A == B
print "RES = A == B"
print "RES = ", RES 

# != operator
print "## != operator example ##"
print "Are a and b different?"
A = 5
print "A = ", A
B = 3 
print "B = ", B
RES = A != B
print "RES = A != B"
print "RES = ", RES 

# < operator
print "## < operator example ##"
print "Is a minor than b?"
A = 5
print "A = ", A
B = 3 
print "B = ", B
RES = A < B
print "RES = A < B"
print "RES = ", RES

# > operator
print "## > operator example ##"
print "Is a higher than b?"
A = 5
print "A = ", A
B = 3 
print "B = ", B
RES = A > B
print "RES = A > B"
print "RES = ", RES 

# <= operator
print "## <= operator example ##"
print "Is a minor or equal than b?"
A = 5
print "A = ", A
B = 3 
print "B = ", B
RES = A <= B
print "RES = A <= B"
print "RES = ", RES 

# >= operator
print "## >= operator example ##"
print "Is a higher or equal than b?"
A = 5
print "A = ", A
B = 3 
print "B = ", B
RES = A >= B
print "RES = A >= B"
print "RES = ", RES 
