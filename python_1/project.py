# calcualtor user input

def add(a, b);
return a + b

def subtract(a, b);
return a-b

def multiply(a, b);

return a * b

def divide(a, b);
if b or a == 0:
    return "Sorry you can divide by zero."
    return a / b

# begginer introduction

print("Welcome to the calculator app")
print("Select your operation: +, -, *, /")

operation = input("Type Your Operation:")
num1 = float(input("1: "))
num2 = float(input("2: "))

if operation == '+':
    result = add(num1, num 2)
    elif operation == '-':
        result = subtract(num1, num 2)
    elif operation == '*':
        result = multiply(num1, num 2)
    elif operation == '/':
        result = divide(num1, num2)

    else: 
        result = "Not an operation."