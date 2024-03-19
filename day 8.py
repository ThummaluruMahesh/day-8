# 1.) Write a Python script to generate and print a dictionary that 
# contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 2.)Find the uncommon words from 2 strings

# # s1 = "Hello how are you"
# s2 = "Hello how is"

# 3.)Wrire a code print the 8th fibanochi number



# ! Eg:3
'''
def profile(name,age,place):
    txt ="my name is {}. iam {} years old. Iam from {}."
    print(txt.format(name,age,place))
profile("mahesh",22,"cbe")
    
my name is mahesh. iam 22 years old. Iam from cbe.
'''


# ! Eg:4
# ? function with return statement

# return
#1.) A variable declared inside the function can be accesed outside
#using return
#2.) return does not print anything
#3.) we can write any code below return statement

    
'''
def f1():
    z = 8
f1()
print(z) # error ---> cannot use outside the function
'''

'''
def f1(a,b):
    c = a*b
    return c
#print(f1(6,8))
obj = f1(6,8)
obj1 = f1(4,6)



def gracemark(object):
    print(object+4)
gracemark(obj)
gracemark(obj1)

52
28

'''


# 123
'''
def palindrome(n):
    string = str(n)
    rev = str(n)[::-1]
    if string==rev:
        print(n, "palindrome")
    else:
        print("Not palindrome")
a = int(input("Enter the value:"))
palindrome(a)

Enter the value:45
Not palindrome
'''

# ? based on the declaration of parameter and args
# ? function are divided into 6 catagories

# posiytion args
# keyword args
# default args
# variable length args
# keyword variable length args

# * positional args
# ? The position of parameter have to be same as position as arguments
# Eg:1
'''
def profile(name,phone,mark):
    txt = "my name is {}. my phone number is {}. I got {} marks."
    print(txt.format(phone,name,mark))

profile(8266727889,"mahesh",98)

my name is mahesh. my phone number is 8266727889. I got 98 marks.

'''

# * keyword args
# ! Eg:1
# To overcome the disadvantages of position args, we use keyword args
# ? It is the process of initialising the parameter with the args while calling the
# ? function
'''
def profile(name,phone,mark):
    txt = "my name is {}. my phone number is {}. I got {} marks."
    print(txt.format(phone,name,mark))

profile(name = "mahesh", mark= 98, phone=9876543210)

my name is 9876543210. my phone number is mahesh. I got 98 marks.

'''
# todo ---> Exception of keyword args function
'''

def profile(name,phone,mark):
    txt = "my name is {}. my phone number is {}. I got {} marks."
    print(txt.format(name,phone,mark))

#profile(name = "mahesh",9876543210,mark =98) # error --> positionargs follow keywordargs
#profile(9876543210,name="mahesh",mark=98) # error --> name has multiple values
profile("mahesh",mark=98,phone=9876543210)

my name is mahesh. my phone number is 9876543210. I got 98 marks.

'''

# * default args
# the method of assigning the argument to the parameter while declaring thefunction
# ! Eg:1
'''
def profile(name,phone,place="kadapa"):
    txt = "my name is {}. my phone number is {}. I am from {}."
    print(txt.format(name,phone,place))

profile("mahesh",9876543210,"kadapa")

my name is mahesh. my phone number is 9876543210. I am from kadapa
'''

# ! Eg:2
'''
def profile(name,phone,place="kadapa"):
    if place != "kadapa" or place=="KADAPA" or place=="kadapa":
        txt = "my name is {}. my phone number is {}. I am  {}."
        print(txt.format(name,phone,place))
    else:
        print("you are not eligible to signup")
profile("mahesh",9876543210)
'''
Exception
'''
def profile(name,place="kadapa",phone): # error --> coz default args should
    if place == "kadapa" or place=="KADAPA" or place=="kadapa":
        txt = "my name is {}. my phone number is {}. I am  {}."
        print(txt.format(name,phone,place))
    else:
        print("you are not eligible to signup")
profile("mahesh",9876543210)
'''

# * variable length params
# ! Eg:1
# To pass more then 1 arg to a parameter means we use variable length args
# To convert normall parameter to variable length param, add * to their prewfix of param

'''
def profile(*name):
    print(" my name is",name)
profile("mahesh,| 'name2', 'name3')

('mahesh', 'name1', 'name2')
'''

'''
name = "mahesh","name1","name2"
def profile(*name):
    for val in name:
        print("my name is", val)
profile("mahesh",'name2','name3')

my name is mahesh
my name is name2
my name is name3
'''

# ! Eg:2
'''
def profile(*name,age):
    for val in name:
        print("my name is", val, "my age is", age)
profile("mahesh",'name2','name3',22)# error --> age has no args
'''

'''
def profile(age,*name):
    for val in name:
        print("my name is", val, "my age is", age)
profile(22,"mahesh",'name2','name3',)

my name is mahesh my age is 22
my name is name2 my age is 22
my name is name3 my age is 22

'''

# * keyword variable length args
# kwargs ---> which is ysed to provide the args in the form of key value pair.
# ! Eg:1
'''
def price(**price_list):
    print(price_list)

price(shirt=1000, iphone=80000)

{'shirt': 1000, 'iphone': 80000}
'''

#n = 5
#{1:1, 2:4, 3:9, 4:16, 5:25}
'''
n = int(input("Enter the number"))
d1 = {}
for val in range(1, n+1):
    d1[val] = val**2
    print(d1)
    
Enter the number5
{1: 1}
{1: 1, 2: 4}
{1: 1, 2: 4, 3: 9}
{1: 1, 2: 4, 3: 9, 4: 16}
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

'''
'''
def dict1(n):
    d1 = {}
    for val in range(1, n+1):
        d1[val]=val**2
    print(d1)
dict1(5)

{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
'''

# ! -----> object oriented programming
# The paradigms of objects oriented programming are


# class
# objects
# inheritance
# polymorphism
# abstraction
# encapsulation

# ! class is blue print of an object

l1 = [1,2,3,4,5,6]

# ? Eg:1
'''
class c1:
    name1 = "mahi"
    print(name1)
mahi
'''
    
# ? Eg:2
'''
class person:
    name = "mahi"
    
c = person() # c as object
The process of creation of an object is called as Instantiation
print(c.name)

'''

# ? Eg:3
# create of a method
#when the function is create with a class is called as method
'''

class person:
    def display(): # It is a method
        print("Hello welcome to classes")
p = person()
p.display()
'''

# ? Eg:4
# ! method with parameter
'''
class person:
    def display(person,name,age):
        print(name,age)
p = person()
p.display("mahi",22)

mahi 22
'''

# ! Eg:5
'''
class person1:
    fname = "mahi" #attribute or static variable
    lname = "T"

    
    def first_name(self):
        print(self.fname)


    def full_name(self):
        print(self.fname+" "+self.lname)
        
p = person1()
p.first_name()
p.full_name()

mahi
mahi T
'''


# ? Eg:6
# constructor --> _init_()
# This is a special method which has the ability to axecute iotself without
# calling it manually theorugh the process of instantiation
'''

class profile:
    def d1(self): # constructor method 
        print("hey")

p = profile() # execute of constructor through this process
'''


'''
d1 = {"a":100,"b":200,"c":300}
d1 = dict(a=100, b=200, c=300)
print(d1)


{'a': 100, 'b': 200, 'c': 300}
'''



#Problem Statement – Given a string S(input consisting) of ‘*’ and ‘#’. 
#The length of the string is variable. The task is to find the minimum number of ‘*’ 
#or ‘#’ to make it a valid string. The string is considered valid if the number of ‘*’ 
#and ‘#’ are equal. The ‘*’ and ‘#’ can be at any position in the string.
#Note : The output will be a positive or negative integer based on number of ‘*’ 
#and ‘#’ in the input string.
'''
(*>#): positive integer
(#>*): negative integer
(#=*): 0
'''
'''   
Example 1:
Input 1:

###***   -> Value of S
Output :

0   → number of * and # are equal
'''





























