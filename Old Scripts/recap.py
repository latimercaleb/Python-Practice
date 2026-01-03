# importing from python standard lib
import random
import requests


print("Hello world")
# Sales tax calc
amount = 10
tax = 0.06
total = amount + (amount * tax )
print(total)

amount = int(11.2)
test = "Text isn't it"
print(amount)
print (test)

# Age calc
# age = int(input('How old are you?\n'))
# decades = age//10
# years = age % 10
# result = f"'You are {decades} decades & {years} years old'"
# print (result) 

# Conditional practice
t = 12
if t < 15: 
    print('In')
elif t > 13: 
    print('Out')
else: 
    print("Default")

# Rock paper scissors
# choice = random.choice(['rock', 'paper', 'scissors'])
# input = input('rock, paper, scissors')
# if choice == input:
#     print('Tie')
# elif input == 'paper':
#     print('You lose')
# elif input == 'scissors':
#     print('You win')
# else:
#     print('Fail state')
    
# roll = random.randint(1,12)
# print (roll)
    
# Lists & Loops
l = ['list', 1,2,3, 'of stuff']
print(l)
if 2 in l:
    print('Item in list')
del l[3]
print(l)

report = [10.50, 12, 14, 5,3]
sumTotal = 0
for exp in report: 
    sumTotal += exp

sameSum = sum(report)

print( f"The total is: $ {sumTotal} & this is the same $ {sameSum}")

y = {
    'a': 12,
    'b': 13,
    'c': False
}

print(y)
print(y['b'])
print(y.get('d'))

# http calls
response = requests.get('http://api.open-notify.org/astros.json')
json = response.json()
print (json.get('people'))

response = requests.get('http://api.open-notify.org/astros.json')
json = response.json()
print (json.get('people'))

# dice roll
def roll(player):
    rollResult =  random.randint(1, 6) + random.randint(1, 6)
    print(f"Player {player} rolled {rollResult}")
    return rollResult

rollfirst = roll(1)
rollsecond = roll(2) 

if rollfirst > rollsecond: 
    print('Player 1 win')
elif rollfirst < rollsecond: 
    print ('Player 2 win')
else: 
    print ('Tie')


# class practice

class Emp:
    def __init__(self, n, a, s) -> None:
        self.age = a
        self.n = n
        self.salary = s

    def calc_pay(self):
        return self.salary/52

emp = Emp('Ex', '33', 10000)
print (emp.calc_pay())

# file IO
with open('Python.txt') as file:
    print(file)