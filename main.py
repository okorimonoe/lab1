import sys

print("Hello, World!")

print(sys.version)

if 5 > 2:
 print("Five is greater than two!")
if 5 > 2:
        print("Five is greater than two!")


x = 5
y = "Hello, World!"

#This is a comment.

if 5 > 2:
 print("Yes")

 # print("Hello, World!")
 print("Cheers, Mate!")

 # This is a comment
 # written in
 # more than just one line
 print("Hello, World!")

 """

 This is a comment
 written in 
 more than just one line
 """


x = 5
y = "John"
print(x)
print(y)

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

x = 5
y = "John"
print(type(x))
print(type(y))


x = "John"
# is the same as
x = 'John'

a = 4
A = "Sally"
#A will not overwrite a

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

MyVariableName = "John"

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = "Python is awesome"
print(x)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

x = 5
y = 10
print(x + y)

x = 5
y = "John"
print(x, y)

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)


def myfunc():
 global x
 x = "fantastic"


myfunc()

print("Python is " + x)

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)


carname = "Volvo"

x = 50

x = 5
y = 10
print(x + y)
z = x+y
print(z)

x, y , z = "Orange", "Banana" , "Cherry"
x = y =z = "Orange"

def myfunc():
  global x
  x = "fantastic"


x = "Hello World"
  str
  x = 20
  int
  x = 20.5
  float
  x = 1j
  complex
  x = ["apple", "banana", "cherry"]
  list
  x = ("apple", "banana", "cherry")
  tuple
  x = range(6)
  range
  x = {"name": "John", "age": 36}
  dict
  x = {"apple", "banana", "cherry"}
  set
  x = frozenset({"apple", "banana", "cherry"})
  frozenset
  x = True
  bool
  x = b"Hello"
  bytes
  x = bytearray(5)
  bytearray
  x = memoryview(bytes(5))
  memoryview
  x = None

  x = 5
  print(type(x))

  x = "Hello World"
  print(type(x))


x = "Hello World"
  str
  x = 20
  int
  x = 20.5
  float
  x = 1j
  complex
  x = ["apple", "banana", "cherry"]
  list
  x = ("apple", "banana", "cherry")
  tuple
  x = range(6)
  range
  x = {"name": "John", "age": 36}
  dict
  x = {"apple", "banana", "cherry"}
  set
  x = frozenset({"apple", "banana", "cherry"})
  frozenset
  x = True
  bool
  x = b"Hello"
  bytes
  x = bytearray(5)
  bytearray
  x = memoryview(bytes(5))
  memoryview
  x = None

  x = 5
  print(type(x))

x = "Hello World"
print(type(x))


x = 20.5
print(type(x))

x = ["apple", "banana", "cherry"]
print(type(x))


x = ("apple", "banana", "cherry")
print(type(x))


x = {"name" : "John", "age" : 36}
print(type(x))


x = True
print(type(x))


x = 1    # int
y = 2.8  # float
z = 1j   # complex
print(type(x))
print(type(y))
print(type(z))



x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))


x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))


x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))



x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))


x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))


import random

print(random.randrange(1, 10))



x = 5
x = float(x)

x = 5.5
x = int(x)

x = 5
x = complex(x)

x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3


x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2


x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'



print("Hello")
print('Hello')

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

a = "Hello"
print(a)

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)


a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

a = "Hello, World!"
print(a[1])

for x in "banana":
  print(x)


a = "Hello, World!"
print(len(a))


txt = "The best things in life are free!"
print("free" in txt)


txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")



txt = "The best things in life are free!"
print("expensive" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

b = "Hello, World!"
print(b[2:5])

b = "Hello, World!"
print(b[:5])


b = "Hello, World!"
print(b[2:])


b = "Hello, World!"
print(b[-5:-2])

a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.lower())

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

a = "Hello, World!"
print(a.replace("H", "J"))

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

a = "Hello"
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b
print(c)

age = 36
txt = f"My name is John, I am {age}"
print(txt)


price = 59
txt = f"The price is {price} dollars"
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt)

txt = "We are the so-called \"Vikings\" from the north."


x = "Hello World"
print(len(x))

txt = "Hello World"
x = txt[0]

txt = "Hello World"
x = txt[2:5]

txt = " Hello World "
x = txt.strip()

txt = "Hello World"
txt = txt.upper()

txt = "Hello World"
txt = txt.lower()

txt = "Hello World"
txt = txt.replace("H", "J")

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))











