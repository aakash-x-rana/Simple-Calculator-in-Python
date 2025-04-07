#Program to create a simple calculator

# 3 steps to build calculator program
#1. Function for Operations
#2. User input
#3. Print Result


# Step-1: Create function
# Function to add two numbers
def add(num1,num2):
    return num1 + num2 

# Function to Subtract two numbers
def sub(num1,num2):
    return num1 - num2 

# Function to multiply two numbers
def multiply(num1,num2):
    return num1 * num2 

# Function to divide two numbers
def divide(num1,num2):
    return num1 / num2 

# Function to average two numbers
def avg(num1,num2):
    return (num1 + num2)/2 

# Step-2: User input
print("Please slect a operation:\n" \
      "1. Addition\n" \
      "2. Subtraction\n" \
      "3. Multiply\n" \
      "4. Divide\n" \
      "5. Average\n")
select = int(input("select a operation from 1-5:"))
if select > 5:
    print("Invalid Operation! please select again!")

number1 = int(input("Enter first number:"))
number2= int(input("Enter second number:"))


#Step-3: print the result

if select == 1:
    print(number1, "+",number2, "=", add(number1,number2))

elif select == 2:
    print(number1, "-",number2, "=", sub(number1,number2))

elif select == 3:
    print(number1, "*",number2, "=", multiply(number1,number2))

elif select == 4:
    print(number1, "/",number2, "=", divide(number1,number2))

elif select == 5:
    print("(",number1, "+",number2,")","/2 =", avg(number1,number2))

