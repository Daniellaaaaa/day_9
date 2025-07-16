# Simple calculator
print('''1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exponential
6. Floor Division
**************************''')
#To perform Addition
print("Please Enter two numbers to add")
#prompt a user for a numbers and store it
first_number=input("First Number:")
#prompt a user for a second number
second_number=input("Second Number:")
addition=float(first_number) + float(second_number)
print(f"The sum of {first_number} and {second_number} = {addition:.2f} \n")

#To perform Subtraction
print("Please Enter two numbers to subtract")
#prompt a user for a numbers and store it
first_number=input("First Number:")
#prompt a user for a second number
second_number=input("Second Number:")
subtraction=float(first_number) - float(second_number)
print(f"The subtraction of {first_number} and {second_number} = {subtraction:.2f} \n")

#To perform multiplication
print("Please Enter two numbers to multiply")
#prompt a user for a numbers and store it
first_number=input("First Number:")
#prompt a user for a second number
second_number=input("Second Number:")
multiplication=float(first_number) * float(second_number)
print(f"The multiplication of {first_number} and {second_number} = {multiplication:.2f} \n")

#To perform division
print("Please Enter two numbers to divide")
#prompt a user for a numbers and store it
first_number=input("First Number:")
#prompt a user for a second number
second_number=input("Second Number:")
division=float(first_number) / float(second_number)
print(f"The division of {first_number} and {second_number} = {division:.2f} \n")

#to perform exponential
print("please enter two numbers to perform exponential operation")
#prompt a user for a numbers and store it
first_number=input("first number:")
#prompt a user for a second number
second_number=input("second number:")
exp=float(first_number) ** float(second_number)
print(f"the exponential of {first_number} and {second_number} = {exp:.2f} \n")

#to perform Floor division
print("please enter two numbers to perform floor division")
#prompt a user for a numbers and store it
first_number=input("first number:")
#prompt a user for a second number
second_number=input("second number:")
floor_division=float(first_number) // float(second_number)
print(f"the floor division of {first_number} and {second_number} = {floor_division:.2f} \n")


