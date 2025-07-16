# Simple calculator
print('''1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exponential
**************************''')
#To perform Addition
print("Please Enter two numbers to add")
#prompt a user for a numbers and store it
first_number=input("First Number:")
#prompt a user for a second number
second_number=input("Second Number:")
addition=float(first_number) + float(second_number)
print(f"The sum of {first_number} and {second_number} = {addition} \n")

#To perform Subtraction
print("Please Enter two numbers to subtract")
#prompt a user for a numbers and store it
first_number=input("First Number:")
#prompt a user for a second number
second_number=input("Second Number:")
subtraction=float(first_number) - float(second_number)
print(f"The sum of {first_number} and {second_number} = {subtraction} \n")

#To perform multiplication
print("Please Enter two numbers to multiply")
#prompt a user for a numbers and store it
first_number=input("First Number:")
#prompt a user for a second number
second_number=input("Second Number:")
multiplication=float(first_number) * float(second_number)
print(f"The sum of {first_number} and {second_number} = {multiplication} \n")

#To perform division
print("Please Enter two numbers to divide")
#prompt a user for a numbers and store it
first_number=input("First Number:")
#prompt a user for a second number
second_number=input("Second Number:")
division=float(first_number) / float(second_number)
print(f"The sum of {first_number} and {second_number} = {division} \n")

#To perform exponential
print("Please Enter two numbers to perform exponential operation")
#prompt a user for a numbers and store it
first_number=input("First Number:")
#prompt a user for a second number
second_number=input("Second Number:")
exp=float(first_number) ** float(second_number)
print(f"The sum of {first_number} and {second_number} = {exp} \n")


