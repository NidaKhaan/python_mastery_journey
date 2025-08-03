raw_input = input("Enter number seperated by spaces:")
numbers = raw_input.split()
file_numbers = []
for number in numbers:
    converted_number = int(number)
    file_numbers.append(converted_number)
print("The numbers you entered are:")
for number in file_numbers:
    square = number ** 2
    cube = number ** 3
    if number % 2 == 0:
        print(f"The number {number} is even.")
    else:
        print(f"The number {number} is odd.")
    print(f"The cube of {number} is: {cube}")
    print(f"The square of {number} is: {square}")
    print(" ")