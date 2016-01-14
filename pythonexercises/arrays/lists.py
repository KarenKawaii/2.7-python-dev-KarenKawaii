# coding: utf-8

'''
    Lists
    Is a type of ordered collection.
    Known as array or vectors in other languages.
    
    To create a list is so simple as indicate
    between brackets and separated by commas the
    values to include them in the list. 
'''

# List
# Example 1

print "## Example for a list ##"
print "L = [22, True, 'one list', [1,2]]"
L = [22, True, 'one list', [1, 2]]
print L

# You can access to every single element of the list
# Writing the list name and indicating the index for
# the element between brackets.
# Note: The index for the first element of the list is 0, not 1.

# Example 2

print "## Example to access an element in the list. ##"
print "L2 = [11, False]"
L2 = [11, False]
print L2
print "ELEMENT_LIST = L2[0]"
ELEMENT_LIST = L2[0]
print ELEMENT_LIST
print "The element list value is 11."

# To access an element from the list included in other list.
# We have to use two times this operator. First, to indicate
# what position from the external list we want to access,
# the second to select the element from the internal list.

print "## Example to access an element from a list into another list. ##"
INTERNAL_LIST = ["one list", [1, 2]]
print INTERNAL_LIST
print "ELEM_INTERNAL_LIST = INTERNAL_LIST[1][0]"
ELEM_INTERNAL_LIST = INTERNAL_LIST[1][0]
print ELEM_INTERNAL_LIST

# Yo can update an element in the list with the previous method.

print "## Update an element in the list. ##"
print "L3 = [22, True]"
L3 = [22, True]
print L3
print "L[0] = 99"
L3[0] = 99
print "## The element is updated.##"
print L3
