#Functions:-
#print(),int(),len()          #These are in-built functions

#print("Hello how are you")   #In this i am calling the print() function

#Making our own functions:
# def hello():
#     print("This is a hello function so i am doing hello.")

# hello()                       #Calling the hello() function    

#Parameters and arguments:
#1 parameters = "parameters are the variables listed inside the functions."
#2 arguments  = "The things you provide to the parameters."
#eg:
# def sum(a,b):
#     print(f"The sum of your numbers is {a + b}.")

# sum(5443,3242)    
# sum(12,45)

#Type's of arguments:
#1 Positional arguments
#eg:
# def sum(a,b):
#     print(f"The sum of your numbers is {a + b}.")

# sum(5443,3242)    
# sum(12,45)

#2 Key-word arguments
# def hello(name,age):
#     print(f"Your name is {name} and age is {age}.")

# hello(age = 22,name = "aditya")  

#3 Default arguments
# def sum(a , b = 45):
#     print(f"The sum is {a + b}")

# sum(12)   
# sum(12,12)                      #In this case the value of b is re-assigned from 45 to 12

#Question1:
# def pallindrome(st):
#     rev = ""
#     for i in range(len(st)-1,-1,-1):
#         rev = rev + st[i]

#     if rev == st:
#         print("Plallindrome")

#     else:
#         print("Not a pallindrome")            

# pallindrome("naman")
# pallindrome("Arun kumar")

#Return in functions:
# def hello():
#     return "Hello how are you"

# hello()
# print(hello())