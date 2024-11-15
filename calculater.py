# Prompt the user for input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter a mathematical operation (addition, subtraction, multiplication, division): ").strip().lower()

# Perform the selected operation
if operation == "addition":
    result = num1 + num2
    print(f"The result of addition is: {result}")
elif operation == "subtraction":
    result = num1 - num2
    print(f"The result of subtraction is: {result}")
elif operation == "multiplication":
    result = num1 * num2
    print(f"The result of multiplication is: {result}")
elif operation == "division":
    if num2 != 0:
        result = num1 / num2
        print(f"The result of division is: {result}")
    else:
        print("Error: mathematical error!!1")
else:
    print("Invalid operation. Please enter addition, subtraction, multiplication, or division.")
