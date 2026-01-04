# Function Practice
# ## Task 1
#
#  Create a function that takes in two integers and returns
## a Boolean True if their sum is 10, False if their sum is something else.

def check_ten(n1,n2):
    sum = n1+n2
    return sum == 10

print('Part 1')
print(check_ten(5,5))
print(check_ten(5,3))
# ## Task 2
#
# Create a function that takes in two integers and returns True if their
# sum is 10, otherwise, return the actual sum value.

def check_ten_sum(n1,n2):
    sum = n1+n2
    return True if sum == 10 else sum

print('Part 2')
print(check_ten_sum(5,5))
print(check_ten_sum(5,3))

# ## Task 3
#
# Create a function that takes in a string and returns back the
# first character of that string in upper case.



def first_upper(mystring):
    firstCharacter = mystring[0].upper()
    return firstCharacter
    # Code Here
print('Part 3')
print(first_upper('how'))
print(first_upper('ward'))


# ## Task 4
#
# Create a function that takes in a string and returns the last two characters.
# If there are less than two chracters, return the string:  "Error".
# Use this link if you need help/hint.
# (https://stackoverflow.com/questions/7983820/get-the-last-4-characters-of-a-string)



def last_two(mystring):
    length = len(mystring)
    if length < 2:
        return "Error"
    else:
        return f"{mystring[length-1]}{mystring[length-2]}"
print('Part 4')
print(last_two('how'))
print(last_two('ward'))
print(last_two('w'))


# ## Task 5
# (Test this vs the old one)
# Given a list of integers, return True if the sequence [1,2,3] is somewhere
# in the list. Hint: Use slicing and a for loop.


def seq_check(nums):
    for i in range(len(nums)-2):
        if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3 :
            return True
    return False    

print('Part 5')
print(seq_check([8,9,10,52,34,1,4,1,2,3,10]))
print(seq_check([8,9,10,52,34,1,4,1,26,3,10]))
print(seq_check([8,9,10,52,1,2,3,34,1,4,1,23,3,10]))
# ## Task 6
#
# Given a 2 strings, create a function that returns the difference in length
# between them. This difference in length should always be a positive number
# (or just 0). Hint: Absolute Value.**



def compare_len(s1,s2):
    absoluteDifference = abs(len(s1) - len(s2))
    return absoluteDifference

print('Part 6')
print(compare_len('how', 'far'))
print(compare_len('ward', 'red'))
print(compare_len('L', 'Apple'))

# ## Task 7
#
# Given a list of integers, if the length of the list is an even number,
# return the sum of the list. If the length of the list is odd, return the max
## value in that list.



def sum_or_max(mylist):
    choice = len(mylist) % 2
    if(choice == 0):
        return sum(mylist)
    else: 
        return max(mylist)
    
print('Part 7')
print(sum_or_max([1,2,3]))
print(sum_or_max([22,44]))
print(sum_or_max([99,81,54,108, 1]))
