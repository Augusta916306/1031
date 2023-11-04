#function to add two numbers
def add(first_input, second_input):
    return first_input + second_input

#function to subtract two numbers
def subtract (first_input, second_input):
    return first_input - second_input

#function to multiply two numbers
def multiply (first_input, second_input):
    return first_input * second_input

#function to divide two numbers
def divide (first_input, second_input):
    return first_input / second_input

    # Simple Calculator
print("Welcome to simple calculator.")
print("I will add/subtract/multiply/divide any two numbers you provide.")
first_input = input("Enter in first number: ")
second_input = input("Enter in second number: ")
operation = input("Would you like to add/subtract/multiply/divide: ")

# explicitly convert string type to float type
first_number = float(first_input)
second_number = float(second_input)

if operation == "add":
    result = first_number + second_number
    print(f"Result: {result}")
elif operation == "subtract":
    result = first_number - second_number
    print(f"Result: {result}")
elif operation == "multiply":
    result = first_number * second_number
    print(f"Result: {result}")
elif operation == "divide":
    result = first_number / second_number
    print(f"Result: {result}") 
else:
    print("Sorry, I do not understand your request.")