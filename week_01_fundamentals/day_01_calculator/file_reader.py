filename = input("Enter the filename: ")
try:
    with open(filename, 'r') as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")