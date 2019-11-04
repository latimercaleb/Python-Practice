# Review of python basics, Run files with python3 fileName

# Commenting, done with hash signs or triple quotes

'''
Multi-line comment, also called docstrings often used to define functions
'''

# Vars are case-senstive and must start with letter or underscore
# Run python code from terminal with 

x = 1
y = 3.5
word = 'A test string'
flag = True

print (word)

# Multiple assignment 
x,y,word,flag = (2,3.1,'Simple second phrase', False)
print (x,y,word,flag)

summation = y + x
print (summation)
print(type(summation))

# Casting
y_casted = str(y)
print (y_casted, type(y_casted))

# Concat
phrase1 = 'Hello'
phrase2 = ' World'
phrase3 = phrase1 + phrase2
print (phrase3)
print ('Formatted string example: {w1}, {w2}'.format(w1=phrase1, w2=phrase2))
print(f'Testing F-strings: {phrase1}, the {phrase2}')
print (phrase3.capitalize(), len(phrase3))

# Lists 
numbers = [1,2,3]
stuff = ['Snacks', 'Apex', 'AI', 'Angular']
othernumbers = list((1,2,3))
print (numbers, othernumbers)
print(stuff[1], len(stuff))

#List Operations
stuff.append('Tacos')
print (stuff)
stuff.remove('AI') ; print (stuff)
stuff.insert(2,'More stuff')
print (stuff)

# Tuples & Sets
# Tuples are unchangeable and ordered, allows dupes, if it has one element, requires trailing comma

fruits = ('Apples', 'Oranges', 'Grapes')
veggies = tuple(('Cucumbers', 'Tomatoes', 'Carrots'))
print (fruits, veggies)
print (fruits[2])
# del veggies # To delete 

# Sets are unordered and unindexed, prevents dupes 
tech_set = {'Keyboard', 'Mouse', 'GPU'}
print (tech_set) 
print ('Keyboard' in tech_set)
tech_set.add('CPU')
print (tech_set)
tech_set.remove('Mouse')
print(tech_set)
tech_set.clear()
tech_set.add('Keyboard')
tech_set.add('Keyboard')
print(tech_set)
# Use del to delete sets as well

# Dictionaries are like JSON a collection, unordered, changeable and indexed, no dupes 
human = {
    'name': 'Natsu Drageneel',
    'guild': 'Fairy Tale',
    'magic-type': 'Dragon Slayer'
}
print (human)
print (human['name'])
print (human.get('guild'))

# Adding key/value
human['pact-beast'] = 'Happy The Cat'
print (human)
print (human.keys())
print (human.items())
print (human.values())

subhuman = human.copy()
subhuman['city'] = 'Cyber-City'
print (subhuman)

del (subhuman['pact-beast'])
subhuman.pop('guild')
print (subhuman)

print(len(human)) 

guildMates = [
    {
        'name': 'Gray Fullbuster',
        'magic': 'CryoMancer'
    },
    {
        'name': 'Erza Scarlet',
        'magic': 'Weapon Transmutation'
    }
]

print (guildMates)
print (guildMates[0]['magic'])

# Functions 
def speak(word='Callat'):
    print(f'Yo {word}')

speak('Foo')
speak()

# Functions w/ returns
def addNums(x,y):
    sumation = x + y
    return sumation

print (addNums(1.2,2.1))

# Lambdas 
addNumsLamb = lambda a, b : a + b
print (addNumsLamb(10,3))

# conditionals 
a = 3
b = 3

if a > b:
    if a == 3: 
        print ('A is 3')
    print ('A is larger')
elif a == b and a == 3:
    print ('A is equal to B and is 3')
else:
    print ('B is larger')

membershiptest = [1,2,4,'moob']
print(membershiptest)

if 2 in membershiptest:
    print (2 in membershiptest)

if -2 not in membershiptest:
    print (-2 not in membershiptest)

# Loops 59:16