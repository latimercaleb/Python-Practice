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