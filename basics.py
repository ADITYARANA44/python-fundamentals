#COMMENTS IN PYTHON:-
#Comments are something that are ignored by the python interpreter.
#We have to use '#' for writing a comment in python.
#eg:
#This is a single line comment.

#In python there are no multi-line comments available but we can acheive it by using 'Doc-string'.
#eg:
"""So this is 
a multi line comment.
with this we can comment multiple lines
in one go."""


#Simple python program:-
# print("Hello everyone my name is ADITYA SINGH RANA and i am learning python")


#Variables in python:-
#In python variables are used as storage to store things in python.
#eg:
#"Lets assume i want to store number 10"
#number = 10     #Here number is the the variable


#Naming conventions:-
#In python we have basically three naming conventions.
#1 Pascal case = AdityaSinghRana
#2 Camel case  = anshulSargoach
#3 Snake case  = arun_kumar


#Data-types in python:-
#Data-types are the things we store in variables.

#Diffent types of Data-types are:
#1 Numbers
# a = 12
# b = 55.6
# c = 86j
# print(type(a))
# print(type(b))
# print(type(c))

#2 Strings
# a = "This is a string Data-type and we can store anything in a string"
# print(a)

#3 Bool
#Bool data-types gives us only two values True/False
#eg:
# a = True
# b = False
# print(type(a))
# print(type(b))


#Strings and type conversion:-

#How string works ?
#String takes more space than other Data-types.
# a = "F"                          
# print(ord(a))                  #(Conversion of character to unicode using ord())
# print(chr(70))                 #(Conversion of unicode to character using chr())

#String Indexing:
# s = "Amrinder Singh"
# print(s[4])

#String slicing:
# a = "Python is better than C++ & Java"
# print(a[0:13:1])

#Type-conversion:
# a = 5
# print(type(a))                  #When you will print this you will se the type as integer 
# a = str(a)                       #Here i am changing the type from integer data-type to string data-type 
# print(type(a))                  #and now you will see the type as string data-type 

#Types of conversion:
#So basically there are two types of conversion's in python.

#1 Implicit => In this python automatically converts data from data-type to another.
#eg:
# a = 10
# b = 3
# print(a / b)
# print(type(a / b))

#2 Explicit => In this we as a user use in-bulid functions to convert one data-type to another.
#eg:
# a = "LION is the king of jungle."
# print(type(a))
# a = float()
# print(type(a)) 

#Type conversion concepts:
"""There are truthy values and falsey values , and there
are only 7 falsy values that means only 7 things will be converted
to false rest true. """
# a = 0
# b = 0.0
# c = False
# d = ""
# e = ()
# f = []
# g = {}

# print(bool(a))
# print(bool(b))
# print(bool(c))
# print(bool(d))
# print(bool(e))
# print(bool(f))
# print(bool(g))


#Input and Output:-

#example of output:
# print("So this this the example of output.")

#example of input:
# a = str(input("Please tell your name sir/madam : "))

#Questions:
#Question1
# n = int(input("Please tell your number Sir/Madam : "))

#Question2
# age = int(input("Please enter your age : "))
# print(f"Your age is {age}")


#Operators:-
#Operators are symbols that perform operations on variables.
#Types:

#1 Arithmetic operators
# a = 12
# b = 50

# print(a + b)                    #Addition
# print(a - b)                    #Subtraction
# print(a * b)                    #Multiplication
# print(a / b)                    #Division
# print(a // b)                   #Floor-division
# print(b % a)                    #Modulus
# print(a**b)                     #Exponentiation

#2 Assignment operators
#Assignment operators are used to assign values to variables. 
#'=' is the assignment operator 

#3 Comnpund assignment operators
# a = 10

# a = a + 10
#print(a)
#but there is also another way to write this operation
# a += 10
# print (a)

# +=                                 #Add and assign
# -=                                 #Subract and assign
# *=                                 #Multiply and assign
# /=                                 #divide and assign
# //=                                #Floor division and assign 
# %=                                 #Modulus and assign 
# **=                                #Exponentation and assign

#4 Comparison operators
#Comparision operators are used to compare variables with each other.
#(also comparision operators will always give's answer in bool(True/false))

# a = 20
# b = 15

# print(a < b)                        #less than
# print(a > b)                        #Greater than
# print(a <= b)                       #Less than equal to
# print(a >= b)                       #Greater than equal to
# print(a == b)                       #Equal to
# print(a != b)                       #Not equal to

#5 Logical operators
#There are basically three types of logical operators.
#'and' , 'or' and 'not'
#eg:
# a = 10
# b = 20
# print(a < b and a != b)
# print(a > b or b > a)
# print(not a)
