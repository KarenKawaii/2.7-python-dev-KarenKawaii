# -*- coding: utf-8 -*-
"""
This module is for explain the different kind of operators.
"""

# Arithmetic operators.
# Plus operator
SUM = 3 + 2
print "Plus operator"
print "3 + 2 =", SUM

# Minus operator.
SUBTRACTION = 4 - 7
print "Minus operator"
print "3 + 2 =", SUBTRACTION

# Negative operator.
NEGATIVE = -7
print "Negative operator"
print NEGATIVE

# Multiplication operator.
TIMES = 2 * 6
print "Multiplication operator. 2 times 6"
print "2 * 6 =", TIMES

# Exponent operator.
EXPONENT = 2 ** 6
print "Exponent operator. Two elevated to the sixth power."
print "2 ** 6 =", EXPONENT

# Division operator.
DIVISION = 3.5 / 2
print "Division operator. 3.5 divided by 2"
print "3.5 / 2 =", DIVISION

# Entire division.
ENTIRE = 3.5 // 2
print "Entire division."
print "3.5 // 2 =", ENTIRE

# Modulus operator % mod.
MOD = 7 % 2
print "Mod % get the remainder of the division of those numbers."
print "7 % 2 =", MOD


# Bit operators
# And & operator
AND = 3 & 2
print "Is an operation and bit to bit between the binary numbers 11 and 10."
print "3 & 2 =", AND

# Or | operator
OR = 3 | 2
print "Or | returns 1 if the first or second operando is 1. For the rest is 0."
print "3 | 2 =", OR

# Xor ^ operator
XOR = 3 ^ 2
print "Returns 1 if one of the operandos is 1 and the other is not."
print "3 ^ 2 =", XOR

# Not ~ operator
NOT = ~3
print "If the operando is 0 changes to 1, if is 1 changes to 0."
print "~3 =", NOT

# Displacement operators << and >>
DISPLACELEFT = 3 << 1
print "Displace the bits n positions to the left."
print "3 << 1 =", DISPLACELEFT
DISPLACERIGHT = 3 >> 1
print "Displace the bits n positions to the right side."
print "3 >> 1 =", DISPLACERIGHT
