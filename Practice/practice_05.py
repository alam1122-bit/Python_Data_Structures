
# Using 'in' as a Logical Operator

fruit = 'banana'

'n' in fruit

'm' in fruit

'ba' in fruit

if 'a' in fruit:
	print('Found it!')

# String Library

greer = 'Hello World'

zap = greet.lower()

print(zap)

# Searching String

fruit = 'apple'
pos = fruit.find('pl')
print(pos)
ab = fruit.find('z')
print(ab) # -1 is mean not found


# Search and Replace

greet = 'hello ab'
x = greet.replace('ab','cd')
y = greet.replace('l','A')
print(x)
print(y)


# Stripping Whitespace

greet = ' Hello abcd '
a = greet.lstrip()
print(a)
b = greet.rstrip()
print(b)
c = greet.strip()
print(c)


# Prefix

line = 'Please have a good day'
line.startswith('Pl') # True


# Parsing and Extracting

data = 'From abcds.dsff@ubt.ac.ll Mon Feb 2 08:21:12 2026'

atpos = data.find('@')
print(atpos)

sppos = data.find(' ', atpos)
print(sppos)

host = data[atpos + 1 : sppos]
print(host)
