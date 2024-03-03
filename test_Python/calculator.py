def addition(num1,num2):
    # Convert input strings to floating-point numbers
    try:
        num1 = float(num1)
        num2 = float(num2)
        return num1+num2 
    except ValueError:
        print("Invalid input. Please enter valid numeric values.")
        exit()
    
def substraction(num1,num2):
    # Convert input strings to floating-point numbers
    try:
        num1 = float(num1)
        num2 = float(num2)
        return num1-num2 
    except ValueError:
        print("Invalid input. Please enter valid numeric values.")
        exit()

# Get input from the user
num1 = input('Enter the first number: ')
num2 = input('Enter the second number: ')
sum = addition(num1,num2)
difference = substraction(num1,num2)

# Display the result
print(f"The sum of {num1} and {num2} is {sum:.2f}")
print(f"The difference of {num1} and {num2} is {difference:.2f}")
