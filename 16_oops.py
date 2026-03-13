#Object oriented programming:-

# Benefit's of using oop's:
#1 It makes's our code re-usable
#2 Provide's security
#3 Good for management system

# Classes in oop's:

# Syntax-
# class Factory:
#     a = 12              #attribute

#     def hello(self):    #method
#         print("How are you ?") 

#     print("Hello how are you i am getting initialized.")

# print(Factory().a)
# Factory().hello()

# Objects in python:

# class Factory:
#     a = 12              #attribute

#     def hello(self):    #method
#         print("How are you ?") 

#     print("Hello how are you ? , i am getting initialized")

# obj = Factory()
# print(obj.a)
# obj.hello()

# creating multiple objects

# eg:
# obj2 = Factory()
# obj3 = Factory() 

# Use of 'self':
#=> 'Self' targets object location.

# Constructor:

# class Factory:
#     def __init__(self,material,zips,pockets):
#         self.material = material
#         self.zips = zips
#         self.pockets = pockets

#     def show(self):
#         print(f"Your object details are {self.material} , {self.pockets} , {self.zips}")
           
# reebok = Factory("Leather",2,2)    
# adidas = Factory("Polyster",1,2)

# print(reebok.pockets)

# Use of 'show()' function-
# reebok.show()

# Attributes and Methods:
#=> Attributes are the variables defined inside a class.

# class Animal():
    
#     name = "Lion"                                #Class attribute

#     def __init__(self,age):                      #Instance attribute
#         self.age = age 

#     def show(self):                              #Instance method
#         print("how are you ?")    

#     @classmethod                                 #Class method
#     def hello(cls):
#         print("How are you brother ?")    

#     @staticmethod                                #Static method
#     def static():
#         print("How are you ?")    


# obj = Animal(12)
# obj.show()
# obj.hello()
# obj.static()


# Four pillar or oop's:-

#1 Inheritance
#2 Polymorphism
#3 Encapsulation
#4 Abstraction


# Inheritance:-

# Syntax-                                         #Parent class / Super-class
# class Factorymumbai:
#     a = "Hello i am an attribute mentioned inside Factory."

#     def hello(self):
#         print("Hello i am a method mentioned inside Factory.")


# class Factorypune(Factorymumbai):                 #Child class / Sub-class
#     pass


# obj = Factorymumbai()
# print(obj.a)

# obj2 = Factorypune()
# obj2.hello()

# Constructor in inheritance:

# class Animal:
    
#     def __init__(self,name):
#         self.name = name

#     def show(self):   
#         print(f"hello your name is {self.name} and age is {self.age}.")

# class Human(Animal):
#     def __init__(self, name,age):
#         super().__init__(name)
#         self.age = age
       
#     def show(self):
#         print(f"Your name is {self.name} and age is {self.age}.")   
    

# animal1 = Animal("lion")
# animal1.show()                   #This will give us error though     

# person1 = Human("aditya",12)      
# person1.show()      

# Types of inheritance:

#1 Single inheritance
#=> In single inheritance we have only one parent class and one child class.

# eg:
# class Animal:
    
#     def __init__(self,name):
#         self.name = name

#     def show(self):   
#         print(f"hello your name is {self.name} .")

# class Human(Animal):
#     def __init__(self, name,age):
#         super().__init__(name)
#         self.age = age

#     def show(self):   
#         print(f"Hello your name is {self.name} and age is {self.age}.")

# animal1 = Animal("lion")
# animal1.show()            

# person1 = Human("aditya",22)      
# person1.show()     

#2 Multiple inheritance
#=> multiple inheritance means there will two parent class and one child class.

# eg:
# class Animal:
#     name1 = "lion"

# class Human: 
#     name2 = "Hrash"

# class Robots(Animal,Human): 
#     name3 = "amrinder123"

# obj = Robots()    
# print(obj.name1)      

# eg2:
# class Animal:
#     def __init__(self,name):
#         self.name

# class Human: 
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# class Robots(Human,Animal): 
#     name3 = "amrinder123"

# obj = Robots("aditya",22)

#3 Multi-level inheritance
#=> GrandParent class --> Parent class --> Child class

# class Factory:
#     def __init__(self,materials,zips):
#         self.materials = materials
  
# class BhopalFactory(Factory):
#     def __init__(self, materials, zips,color):
#         super().__init__(materials, zips)
#         self.color = color
  
# class PuneFactory(BhopalFactory):
#     def __init__(self, materials, zips, color,pockets):
#         super().__init__(materials, zips, color)
#         self .pockets = pockets

# obj = PuneFactory()


# Polymorphism:-
#=> There are two ways to achieve polymorphism in python.

#1 Method overriding:
# eg:
# class Animal:
    
#     def show(self):
#         print("Hello i am aditya singh rana.")

# class Human(Animal):     

#     def show(self):
#         print("How are you ?")   

# obj = Human()
# obj.show()

#2 Method overloading:
#=> method overloading doesn't exist in python.

# Duck Typing:

# eg:
# class Animal:
    
#     def show(self):
#         print("Hello i am aditya singh rana.")

# class Human:     

#     def show(self):
#         print("How are you ?")   

# obj = Human()
# obj.show()
 
# obj2 = Animal 
# obj2.show()


# Encapsulation:-

# eg:
# class Factory:
    
#     __a = "pune"

#     def __show(self):
#         print("Hello i am a pune factory.")

# obj = Factory()
# print(obj.a)


# Abstraction:-
#=> abstraction doesnot exist in python but we can achieve it usinga library.

# eg:
# from abc import ABC, abstractmethod

# class abstract(ABC)
#     @abstractmethod
#     def perimeter(self):
#         pass
    
#     @abstractmethod
#     def area(self):
#         pass

# class Square(abstract):
    
#     def __init__(self,side):
#         self.side = side

#     def area(self):
#         print("I have careated this.")        
    

# class Circle(abstract):

#     def __init__(self,radius):
#         self.radius = radius
        
#     def perimeter(self):
#         print("I have created.")

#     def area(self):
#         print("I have careated this.")        


# obj = Circle(7)


# Dunder Methods:-

# eg:
# class Animal:
    
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"Hello how are you and your name is {self.name}."

#     def __add__(self, other):
#         return f"Your sum of ages are {self.age + other.age}."   

# obj1 = Animal("Lion",4)
# obj2 = Animal("Dolphin",5)

# print(obj1 + obj2)










