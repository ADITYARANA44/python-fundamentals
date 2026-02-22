#Loops:-
#loops in python allows us to execute a block of code multiple times without re-writing it.

#Types:
#1 For-loop
#2 While-loop

#break and continue:
#Use of break
# a = 20

# for i in range(1,20,1):
#     if i == 15:
#         break 
#     print(i)

#Use of continue
# a = 20

# for i in range(1,21,1):
#     if i == 15:
#         continue
#     print(i)
        
#Questions on For-loops:
#Question1
# n = int(input("Plase tell your number = "))

# for i in range(n):
#     print("Hello World")

#Question2
# n = int(input("Please tell your number = "))

# for i in range(1,n+1,1):
#     print(i)

#Question3
# n = int(input("Please tell your number = "))

# for i in range(n,0,-1):
#     print(i)

#Question4
# n = int(input("Please tell which table you want to print = "))

# for i in range(1,11,1):
#     print(f"{n} * {i} = {n * i}")

#Question5
# n = int(input("Please tell your number = "))
# sum = 0

# for i in range(1,n+1,1):
#     sum = sum + i

# print(sum)    

#Question6
# n = int(input("Please tell your number = "))
# fact = 1

# for i in range(1,n+1,1):
#     fact = fact * i

# print(fact)   

#Question7
# n = int(input("Please tell your number = "))
# even = 0
# odd = 0

# for i in range(1,n+1,1):
#     if i % 2 == 0:
#         even = even + i

#     else:
#         odd = odd + i

# print(f"Sum of even and odd numbers are {even} , {odd}")        

#Question8
# n = int(input("Please tell your number = "))

# for i in range(1,n+1,1):
#     if n % i == 0:
#         print(i)

#Question9
# n = int(input("Please tell your number = "))
# sum = 0

# for i in range(1,n,1):
#     if n % i == 0:
#         sum = sum + i

# if sum == n:
#     print(f"{n} is a perfect number")

# else:
#     print(f"{n} is not a perfect number")        

#Question10
# num = int(input("Please tell which number you want to check = "))
# count = 0

# for i in range(1,num+1,1):
#     if num % i == 0:
#         count = count + 1

# if count == 2:
#     print(f"{num} is a prime number")

# else:
#     print(f"{num} is not a prime number")

#Question11
# st = "I love to play free-fire in free time."
# b = ""

# for i in range(len(st)-1,-1,-1):
#     b = b + st[i]

# print(b)    

#Question12
# st = str(input("Please tell your string = "))
# b  = ""

# for i in range(len(st)-1,-1,-1):
#     b = b + st[i]

# if b ==  st:
#     print(f"{st} is pallindrome")
   
# else:
#     print(f"{st} is not pallindrome")

#Questions13
# a = "irbg846785@#2ueuvui!#@g4yubvlk"
# dig = 0
# char = 0
# spchar = 0

# for i in a:
#     if i.isdigit():
#         dig = dig + 1

#     elif i.isalpha():
#         char = char + 1

#     else:
#         spchar = spchar + 1

# print(f"Total number of digits are {dig} , total number of characters are {char} and total number of spchar are {spchar}")    

#Questions on while-loops:
#Question1
# n = int(input("Please tell your number = "))

# while n > 0:
#     print(n % 10)
#     n = n // 10

#Question2
# n = int(input("Please tell your number = "))
# rev = 0

# while n > 0:
#     rev = rev * 10 + n % 10
#     n = n // 10

# print(f"Reverse is {rev}.")    

#Question3
# n = int(input("Please tell your number = "))
# copy = n
# rev = 0

# while n > 0:
#     rev = rev * 10 + n % 10
#     n = n // 10

# if rev == copy:
#     print(f"{copy} is a pallindromic number.")

# else:
#     print(f"{copy} is not a pallindromic number.")  

