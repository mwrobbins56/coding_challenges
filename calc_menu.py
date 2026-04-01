# Create menu-driven calculator
# Function for each operation, add - substract - multiply - divide
def sum(x, y):
    return x + y
def subt(x, y): 
    return x - y
def mult(x, y): 
    return x * y
def divide(x, y):
    if y == 0:
        return "You cannot divide by zero!"
    return x / y

while True:
    # Prompt the user to select an operation and input numbers
    print("Enter 1 to Add, 2 to Subtract, 3 to Multiply, 4 to Divide, 5 to Exit")
    choice = input("Enter your choice (1-5): ")
    num1=float(input("Enter 1st number: "))
    num2=float(input("Enter 2nd number: "))

    # Display the results
    if choice == '5': break
    elif choice == '1':
        print("Result: ",sum(num1,num2))
    elif choice == '2':
        print("Result: ",subt(num1,num2))
    elif choice == '3':
        print("Result: ",mult(num1,num2))
    elif choice == '4':
        print("Result: ",divide(num1,num2))
    else:
        print("Invalid choice!")
 