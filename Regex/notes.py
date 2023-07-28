#regular expression(Regex) : it is defined as a seq of characters which are used to search for a pattern in string.
#module "re" is used for regular expression in python.
#some built-in fns used in regular expression :
#  1)fullmatch() : it returns true if match is found.
#  2)search() : it returns match object.
#  3)findall() : it returns list that contains all match.
#  4)split() : it returns a string has been split.
#  5)sub() : it is used to replace the matches.

#a regular expression is created using mix of characters, spcl seq,and sets.

#characters :
# [] : represents a set of characters
# \ : represents spcl seq
# ^ : represents patterns present at the beginning of a string
# . : represents any character present at some specific place
# * : represents 0 or more occurrence
# + : represents 1 or more occurrence
# {} : specified number of occurrence of pattern
# | (or) : represents this or that character is present

#rules of regex:
# x ='[abc]' : either a,b or c
# x ='[^abc]' : except abc
# x ='[a-z]' : lower case a to z
# x ='[A-Z]' : upper case A to Z
# x ='[a-zA-Z]' : both upper and lower case
# x ='[0-9]' : it checks the digit
# x ='[a-zA-Z0-9]' : lower cases, upper cases or digit

#spcl seq :
# x = '\s' : check space
# x = '\d' : check digit
# x = '\D' : it returns string except number
# x = '\w' : it returns string containing a word

#quantifiers :
#  x = '[a]+' : it includes more number of a
#  x = '[a]*' : count including zero number of a
#  x = '[a]?' : a included or not included(if used only 1 time)
#  x = '[a]{n}' : n = number
#  x = '[a]{n,k}' : n = minimum number, k = maximum number

#ctrl+f = search bar pops in any app















