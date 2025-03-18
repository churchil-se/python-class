#Ask user to input two numbers and an operator
num1 = float(input("Think of a number between 1-10: "))
num2 = float(input("Now, think of a number between 11-20: "))
operation = input("Choose an operation (+, -, *, /): ").strip()


#Perform the selected operation
if operation  == '+':
    result = num1 + num2
elif operation =='-':
    result = num1 - num2
elif operation =='*':
    result = num1 * num2
elif operation =='/':
    if num2 != 0:
        result = num1 / num2
    else:
        print("Error: Division by zero is not allowed")
else:
    print("Invalid operation. Kindly choose +, -, *, or /.")

#Display the result
print(f"The result of {num1} {operation} {num2} is: {result}")