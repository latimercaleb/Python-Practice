# Remember logical operations
a = "foo"
b = "bar"
print (a == b) 
print (a == b and b == 1)
print (a == b or b == "bar") 

# Control flow
if a==1:
    print("If block")
else:
    print("Else block")

# Looper
the_list = ["A", "B", "C"]
for itm in the_list:
    print(itm)

for index,itm in enumerate(the_list):
    print(f"{itm} is at position {index}")

c = len(the_list)
while c > 0:
    print(the_list[c-1])
    c = c-1

for x in range(0,5):
    print(x)

# Functions
def test_function():
    print("Function called")

test_function()

def test_function1(name="me"):
    print(f"Calling {name}")

test_function1()
test_function1("you")

# Closures
alpha = "Foo String"
def wrapper():
    alpha = "Bar String" # If this is commented it reffs line 43 instead, can use global keyword to refference it directly though its not recommended
    def inner(): 
        print(alpha)
    inner()
wrapper()

# OOP
class FirstClass:
    def __init__(self, foo, bar):
        self.foo = foo
        self.bar = bar
    def testMethod(self):
        print("{}, {}".format(self.foo, self.bar))

first = FirstClass('test', 'phrase')
first.testMethod()

class Book: 
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __repr__(self): # Special method gives print representation for object
        return f"Title: {self.title}, Author: {self.author}"
    
    def __len__(self): 
        return self.pages

firstBook = Book('Flask Starting Soon', 'Caleb', 220)
print(firstBook)
print(len(firstBook))

# Decorators
def greet():
    print('Greetings')
    def goodbye(): 
        return "Farewell!"

def hold(func): # Function passing as arg
        func()
        return "Hold Please!"

print(hold(greet))

def decorator_new(proc): # Decorator concept
    def wrapper():
        print("Execution context before function...")
        proc()
        print("Execution context post-function....")
    return wrapper

def use_decorator():
    print("No decorator?")

use_decorator()
use_decorator = decorator_new(use_decorator) # Reassign function with decorator logic
use_decorator()

@decorator_new
def use_decorator_notation(): # Reassignment via decorator notation
    print("No decorator?")

use_decorator_notation()