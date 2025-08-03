try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
except ValueError:
    print("Invalid input. Please enter numeric values.")
    exit()
operation = input("Enter operation (+, -, *, /): ")
if operation == '+':
    result = (num1) + (num2)
elif operation == '-':
    result = (num1) - (num2)        
elif operation == '*':
    result = (num1) * (num2)                    
elif operation == '/':
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
        exit()
    result = (num1) / (num2)
else:
    print("Invalid operation. Please enter one of +, -, *, /.")
    exit()
print(f"The result of {num1} {operation} {num2} is: {result}")
