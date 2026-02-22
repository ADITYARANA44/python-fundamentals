#Data Structures in python:-

#Data structures are used to store,organize,and manipulate data efficiently.
#In python we have 4 types of in-build data structures.
#(i)   List
#(ii)  Tuple
#(iii) Set
#(iv)  Dictionary


#List:-

#1 Mutable;
# l = [12,13,14,15,16]            #Before

# l = [120,13,14,15,16]           #After

#2 Duplicates;
# l = [12,13,14,15,12,12,12,16]

#3 Heterogenous;
# l = [12,12.1,True,print(),15,len()]

#4 Ordered;
#In lists we can access elements of list using inedex values.

#List indexing and Slicing:
# l = [12,13,14,15,16,34.5,True,print()]

#print(l[0])                      #Indexing
# print(l[0:5:1])                 #Slicing

#List traversing and Methods:

#List Traversing(running loops on list)
# l = [12,13,14,15,16,34.5]

# for i in range(len(l)):
#     print(l[i])

#2nd way directly on values
# l = [12,13,14,15,16,34.5]  

# for i in l:
#     print(i)

#List Methods
#print(dir(list))
#help(list)

#Use of append() method
# l = [1,2,3,4,5]

# l.append(6)
# l.append(7)
# print(l)

#Use of insert() method
# l = [1,3,4,5]

# l.insert(1,2)
# print(l)

#Use of remove() method
#Remove method will always remove the first occurence.
# l = [1,2,3,4,5,6]

# l.remove(4)
# print(l)

#Mutablility
# l = [1,2,3,4,5,6]
# l[0] = 10
# print(l)

#Question1
# l = [-45,67,12,-68,-69,34]
# print("Positive elements are")
# for i in l:
#     if i >= 0:
#         print(i)

# print("Negative elements are")
# for i in l:
#     if i < 0:
#         print(i)        

#Question2
# l = [12,435,67,89,23,25,69]
# sum = 0
# for i in l:
#     sum = sum + i

# print(f"Mean is {sum / len(l)}")    

#Question3
# l = [12,567,43,235,347,568,45,7]
# greatest = l[0]
# index = 0

# for i in range(len(l)):
#     if l[i] > greatest:
#         greatest = l[i]
#         index = i

# print(f"Your greatest number is {greatest} at index {index}.")

#Question4
# l = [12,567,43,235,347,568,45,7]
# greatest = l[0]
# sec_greatest = l[0]

# for i in l:
#     if i > greatest:
#         sec_greatest = greatest
#         greatest = i

#     elif i > sec_greatest:
#         sec_greatest = i

# print(sec_greatest,greatest)     

#Question5
# l = [12,13,14,15,16,17]

# for i in range(len(l)-1):
#     if l[i] < l[i+1]:
#         continue

#     else:
#         print("Your list is not sorted.")
#         break

# else:
#     print("Your list is sorted.")


#Tuple:-

# a = (1,2,3,4,5)
# print(type(a))

#1 Immutable;
# a = (1,2,3,4,5)
# a[0] = 12
# print(a)

#2 Duplicates;
# a = (1,2,3,4,5,1,2,2)

#3 Ordered;
#In tuples we can access values using inedex values.

#4 Heterogenous;
# a = (1,2,3,4,5,print(),1.3,float())

#Tuple treversing:
# a = (1,2,3,4,5,5.5)

# for i in a:
#     print(i)

#2nd way
# a = (1,2,3,4,5,6.89)

# for i in range(len(a)):
#     print(a[i])

#Tuple methods:

#Use of index() method
# a = (1,2,3,4,5,6.89)
# index = a.index(5)
# print(index)

#Use of count() method
# a = (1,2,3,4,5,6,7,8,1,2,3,3,2,1,4,5)
# count = a.count(1)
# print(count)

#Tuple un-packing:
# a,b,c,d = (1,2,3,4)
# print(a)
# print(b)
# print(c)
# print(d)

# a = (1)
# print(type(a))                #Here tuple got-unpacked

#We can solve this by 
# a = (1,)
# print(type(a))


#Sets:-

#s = {}                          #Currently this is not a set this is a dictionary

#1 Mutable;
# s = {1,2,3,4,5}                  #Before
# s = {10,2,3,4,5}                 #After

#2 No-duplicates;
# s = {1,2,3,4,5,5}

#3 Un-ordered
#Sets are un-orderd and we cannot access elements using index values.

#Heterogenous
# Set is semi-heterogenous it can store some data types like string, numbers, tuples but not everything.

#Hash function in python:
# print(hash(12))
# print(hash("hello"))
# print(hash((1,2,3,4)))

#Set Traversing:
"""A set cannot be traversed using the index values cause it is 
unordered and has no indexSo many times it will give random values."""

#Set methods:
# a = {1,2,3,4}

#Use of remove() method
# a.remove(2)
# print(a)

#Use of pop() method
# a.pop()
# print(a)

#Use of clear() method
# a.clear()
# print(a)

#Set operations:
# a = {1,2,3,4,5,12}
# b = {6,7,8,9,10,12}

#UNION
# print(a | b)

#INTERSECTION
# print(a & b)

#DIFFERENCE
# print(a - b)

#SYMMETRIC DIFFERNCE
# print(a ^ b)


#Dictionaries:-
#Dictionary is pair of keys and values.

# d = {}
# print(type(d))

# d = {1:"Hello",2:56}                   #Here 1 is the key and "Hello" is the value 
# print(type(d))

#1 Mutable;
"""Dictionaries are mutable , meaning you can change
   , add or remove key-values pairs after creation."""
# eg:
# d = {1:"Hello",2:56} 
# d[2] = 49
# print(d)

#2 Duplicates;
"""Keys must be unique , but you can have duplicated in
   values."""
# eg:
# d = {1:"Hello",2:56,3:56} 
# print(d)

#3 Order;
"""Dictionary follows insertion order.we cannot access values
   using index values but we can access them using keys."""

#4 Heterogenous:
"""A dictionary can store different types of keys and values,
   like integers, strings , lists or even another dictionary. """
# eg:
# d = {1:"Hello",2:56,"hello":"hello"} 
# print(d)

# Syntax Working:
# d = {10:100,20:200,30:300}
# print(d[10])

# Updating the key-values:
# d = {10:100,20:200,30:300}
# d[10] = 1000
# print(d)   

# Creating the key-values:
# d = {10:100,20:200,30:300}
# d[40] = 400
# print(d)

# Traversing in dictionary:
# d = {10:100,20:200,30:300,40:400}
# In first step we are accesing only keys.
# for i in d:
#     print(i)

# In second step we are accesing only values.
# for i in d:
#     print(d[i])   

# Dictionary methods:
# help(dict)

# Use of clear() method
# d = {10:100,20:200,30:300,40:400}
# d.clear()
# print(d)

# Deep copy and Shallow copy

# Deep copy
# eg:
# d = {10:100,20:200,30:300,40:400}
# b = d
# b[0] = 100
# print(d)

# Shallow copy
# d = {10:100,20:200,30:300,40:400}
# b = d.copy()
# b[0] = 100
# print(d)

# Question1
# d1 = {10:100,20:200,30:300}
# d2 = {40:400,50:500,60:600}

# for i in d2:
#     d1[i] = d2[i]

# print(d1)    

# Question2
# d1 = {10:100,20:200,40:300}
# sum = 0
# for i in d1:
#     sum = sum + d1[i]

# print(sum)    

#Question3
# l = [1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,4,4,5,5,6,6,7,7,7,8,9,9,10]
# d = {}

# for i in l:
#     if i in d.keys():
#         d[i] = d[i] + 1

#     else:
#         d[i] = 1

# print(d)

# Question4
# d1 = {10:100,20:200,40:300}
# d2 = {40:400,50:500,60:600}

# for i in d2:
#     if i in d1.keys():
#         d1[i] = d1[i] + d2[i]

#     else:
#         d1[i] = d2[i]

