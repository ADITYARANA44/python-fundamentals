# Exception handling:-

# Eroors:
# print("hello world"               #Syntax error
# a = 12                            #Indentation error
# if a == 12
# print("Hello")

# Exceptions:
# a = int(input("Please tell your number = "))

# print(10 / a)                       #Try dividing 10 with zero you'll get ZeroDivisionError
# print("ok i have done the division.")

# Use of try , rxcept , else, finally:
# a = int(input("Please tell your number = "))

# try:
#     print(10 / a)         

# except Exception as err: 
#     print(f"sorry there is an error as {err}.")   

# else:
#     print("good there is no exception.") 

# finally:
#     print("I will run no matter what.")                

# print("ok i have done the division.")

# Use of (raise raising an error by yourself) 
# age = int(input("tell your age = "))

# if age < 10 or age > 18:
#     raise ValueError("your age must be between 10 and 18.")

# else:
#     print("welcome to club.")