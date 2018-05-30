#printing to the terminal
print (2+5)

# vars in python
foo = 12
print ("This is my variable ")
print(foo)

#import modules to use them
import math
print(math.ceil(2.89))

#strings in python get  single or double quotes
'hello'
"world"

# Booleans & Conditionals
True != False 
4 > 3
3 < 4
3 ==  3
3 <= 4
4>=3

if  4<3:
    print(True)
elif 4==4:
        print("Elif ran")
else:
    print(False)

num1 = 15
num2 = 13
if num1 < num2 or num2 < num1:
    print ("Processed")
else:
    print ("Unprocessed")

        
# Lists, Dictionaries, Tuples

#Lists are zero indexed and only use [] and are mutable collections
#Can print from last index first using -1 first index using 0
emptyList =[]
print("This is an empty list: {0} Of type: {1}".format(emptyList,type(emptyList)))
numList = [1,2,34,5]
print ("The first index is: {0}".format(numList[0]))
print ("The last index is: {0}".format(numList[3]))
print ("The last index is: {0}".format(numList[-1]))

# Can have heterogenous data types
otherList = ["name", True, 12]
print (otherList)
otherList.append("AnotherName")
print (otherList)

# Can get more than one element at a time
print(otherList[1:4])

# Can list a list in a list
nestedList = [1,2,["Apple", "Pie"],3]
print(nestedList[2])
print(nestedList[2][1])
print(nestedList[2][0])

#Using the "for-in"  &  sort
print("Start of for-in loop")
for i in nestedList:
    print(i)
even = [2,4,6,8]
odd = [1,3,5,7]
total = even + odd
print("Concatenated total: {0}".format(total))
total.sort()
print("Sorted total: {0}".format(total))

#Tuple,  similar to list of immutable collection, similar to string, Lists can cast to tuple
firstTuple = 1,2,True,"tacos"
print(firstTuple)
print(firstTuple[1:4:])
# Tuples can multi-assign
One,Two,Three = firstTuple[0:3:]
print(One)
print(Two)
print(Three)

#Dictionary: Most prominent type, key-value pairs like json using {}, use [] to pick the name and return the key
names = {"liz": 2512, "cal": 4095, "rush" : 2032}
print (names)
names["weforgotone"] = 12
print (names)

# Functions for dictionary, .keys() and .values() returns a list that is iterable but not indexable if you want a specific key turn it into a list
keys = names.keys()
print (keys)
del names["weforgotone"]
print (names)
A = list(keys)
vals = names.values()
print(vals)
B = list(vals)

# Loops



#Functions



#OOP


