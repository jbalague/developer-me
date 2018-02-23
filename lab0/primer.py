# Python primer
#
# For better understanding refer to the official documentation
#  The Python Tutorial
#  https://docs.python.org/3/tutorial/index.html

# Everything after a hash, #, is a comment and extends to the end of the line

# Hello world!
print('Hello world!')

# Name declaration, assignment and reference
name = 'mundo'

print('Hola ' + name)

# Names (variables) are references to values
# Values can be of several types (number, string, list, dict..)
seventeen = 17
pi = 3.14159265359
greeting = 'Good morning!'
weekDays = ['Monday', 'Tuesday', 'Wednesday', 'Thusrday', 'Friday']
minion = { 
  'name': 'Stuart',
  'eyes': 1,
  'likes': ['banana', 'banana smothie', 'banana ice cream']
}

print(seventeen)
print(greeting)
print (weekDays[1])
print(minion['name'])

# Names can be re-assigned to any other value, i.e. no static typing
seventeen = 'XVII'
weekDays = 'boring'

print(seventeen)
print (weekDays[1])

# Apropos string formating and printing
sentence = minion['name'] + ' has ' + str(minion['eyes']) + ' eye(s) and likes ' + str(minion['likes']) + '...'
print(sentence)
print('{} has {} eye(s) and likes {}...'.format(minion['name'], minion['eyes'], minion['likes']))

# Consistent notation is helpful 
# Some common naming notations 
NumberOfDaysInAYear = 365       # CamelCase
numberOfDaysInAYear = 365       # mixedCase
number_of_days_in_a_year = 365  # lowercase with underscores
# Chose one and stick to it
#
# Use a fixed number of spaces, not tab(s), to indent (check editor)



# Reserved identifiers a.k.a. Keywords
#
#   False      class      finally    is         return
#   None       continue   for        lambda     try
#   True       def        from       nonlocal   while
#   and        del        global     not        with
#   as         elif       if         or         yield
#   assert     else       import     pass
#   break      except     in         raise



# Control Flow statements
# 
fruit = 'banana'
if fruit == 'banana':           # Don't forget the semicolon!
  print('Yummy!')               # Some indentation required
  print('I like bananas!')      # Same indentation required
else:
  print ('I don\'t like that!') # Note the escape character, \,  

weekDays = ['Monday', 'Tuesday', 'Wednesday', 'Thusrday', 'Friday']
for day in weekDays:
  print(day + ' is boring...')

while weekDays:                         # While weekDays not empty
  print(weekDays.pop(0) + ' is boring') # extract and print first of the list 

# Procedures and functions
def sayHello():       # Doesn't expect any argument
  print('Hi')         # Doesn't return any value (well, technically returns None)

def say(something):   # Expects one positional argument
  print(something)    # Doesn't return any value (well, technically returns None)

def sum(num1, num2):  # Expects two positional argument
  return(num1 + num2) # Returns some value 

sayHello()
say('Nice to meet you.')
print(sum(21, 21))

# Optional keyword arguments can have default values
def f1(a='a', b='b'): 
  print(a, b)

def f2(**d):          # Will receive a dictionary with all keyword arguments  
  print(d)            

f1()
f1(a='A')
f2(d='aha', d1=1, d2=2)

# Modules are just files containing some python code
#
# Supose we have moved code below to a file named week.py 

week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def tomorrow(day):
  tomorrow = day
  if day in week:
    n = week.index(day)
    n = n + 1
    if n == len(week):
      n = 0
      tomorrow = week[n]
  return(tomorrow)

def yesterday(day):
  yesterday = day
  if day in week:
    n = week.index(day)
    n = n - 1
    if n < 0:
      n = len(week) - 1 
      yesterday = week[n]
  return(yesterday)


# We can now import it in our program
import week  # Loads and executes week.py content

# All names in week.py are available under the namespace week
print(week.week)
today = 'Wednesday'
print(week.tomorrow(today))
print(week.yesterday('Monday'))
              

# Python comes with many handy built-in modules
# Environment variables
import os
print(os.environ['USER'])

# Execution arguments
import sys
print(sys.argv)

# You'll find many more good surprises looking for
# The Python Standard Library in the documentation
#  https://docs.python.org/3/library/index.html

# Exception handling
#
# Errors detected during execution are called exceptions and
# can be easily and elegantly handled by the program itself
filename = 'thisfiledoesnotexist.txt'
try:
  file = open(filename)
  print('Cool! File found and opened')
except FileNotFoundError:
  print('Uh! Something went wrong. File not found')
finally:
  print('No matter what happens, finally section is always executed')

# Raising exceptions to leverage exception handling
#
# raise Exception()


# Classes bundle data and functionality together
class Space:
  
  spaces = []                   # Class variable, shared by all instances

  def __init__(self, name):     # Constructor, called on instantiation
    self.name = name            # Instance variable, unique per instance
    self.members = []           # Instance variable, unique per instance
    self.spaces.append(self)

  def names():                  # Class method
    names = []
    for space in Space.spaces:
      names.append(space.getName())
    return(names)

  def getName(self):
    return(self.name)

  def updateName(self, name):
    self.name = name

  def addMember(self, name):
    self.members.append(name)
  
  def removeMember(self, name):
    self.members

  def getMembers(self):
    return(self.members)

  def info(self):
    print('Space {} has {} members.'.format(self.name, len(self.members)))
    print(self.getMembers())


# Using classes
room1 = Space('room1')            # New instance
room2 = Space('room2')            # New instance

print('Room list:')
print(Space.names())              # Calling class method

room1.addMember('Mel')            # Calling instance method
print(room1.getMembers())
room1.addMember('Stuart')
room1.addMember('Bob')
print(room1.getMembers())
room1.info()

print('There are {} spaces:'.format(len(Space.spaces)))
for space in Space.spaces:
  space.info()

