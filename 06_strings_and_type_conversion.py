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