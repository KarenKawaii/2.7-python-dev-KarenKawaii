# coding: utf-8
'''
    Strings
    The strings are text between '' or ""
    Inside of that characters could be anothers
    like n or t escaped with \
'''

# Example for unicode codification.
# Example to raw string.

print "## Unicode string example. ##"
UNICODE = u"äóè"
print "Unicode string should have an u before the string \
with special characters."
print UNICODE

print "## Raw string example. ##"
RAW = r"\n"
print "The escaped characters with \ are not \
replaced by their counterparts."
print RAW

print "## Triple quotes to multiple lines example. ##"
TRIPLEQUOTES = """This text is written in
multiple lines. Isn't necessary to use the back slash for a
jump line."""
print TRIPLEQUOTES

# You can use operators to concatenate strings.
print "## Use operators to concatenate strings example. ##"
NUM_ONE = "uno"
NUM_TWO = "dos"
ADDITION = NUM_ONE + NUM_TWO
print "ADDITION = NUM_ONE + NUM_TWO"
print ADDITION

print "MULTIPLY = NUM_ONE * 3"
MULTIPLY = NUM_ONE * 3
print MULTIPLY
