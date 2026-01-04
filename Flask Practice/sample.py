# Quick recap of basic python concepts
print("hello world")
print(2+1)

a = 5
print(a)

# String practice
b = "i'm a practice string"
print(b)
print(len(b))
print(b[2])


c = b.capitalize()
print(c)

# Start position included, exit position excluded
d = c[6:14]
print(d)
# Can use format or f-string literals
print("hello {} world".format(d))

# List practice
free_list=[1,2,3]
print(free_list)
print(len(free_list))

mixed_list = [True, 1, 'test']
print(mixed_list)

mixed_list.append('zero')
mixed_list.insert(2,'X')
print(mixed_list)

# Dictionaries
ex = {'k1': 'value 1', 'k2': 'value 2'}
print(ex)
print(ex['k1'])
ex['k3'] = 150
print(ex)


#####################################
#### PART 6: EXERCISE REVIEW  #######
#####################################

# Time to review all the basic data types we learned! This should be a
# relatively straight-forward and quick assignment.

###############
## Problem 1 ##
###############

# Given the string:
s = 'flask'

# Use indexing to print out the following:
# 'f'

# 's'

# 'ask'

# 'las'

# 'k'

# Bonus: Use indexing to reverse the string


###############
## Problem 2 ##
###############

# Given this nested list:
mylist = [3,7,[1,4,'hello']]
# Reassign "hello" to be "goodbye"


###############
## Problem 3 ##
###############

# Using keys and indexing, grab the 'hello' from the following dictionaries:

d1 = {'simple_key':'hello'}

d2 = {'k1':{'k2':'hello'}}

d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}


###############
## Problem 4 ##
###############

# Use a set to find the unique values of the list below:
mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]


###############
## Problem 5 ##
###############

# You are given two variables:
age = 4
name = "Sammy"

# Use print formatting to print the following string:
"Hello my dog's name is Sammy and he is 4 years old"
