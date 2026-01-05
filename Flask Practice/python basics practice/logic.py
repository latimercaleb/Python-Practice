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
