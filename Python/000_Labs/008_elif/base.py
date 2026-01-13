num1 = int(input("Please enter a number: "))
operator = input("Please enter an operation (+, -, *, /): ")
num2 = int(input("Please enter another number: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
 
    if num2 == 0:
        result = "Error (cannot divide by zero)"
    else:
        result = num1 / num2
else:
    result = "Invalid operator"
 
print(f"{num1} {operator} {num2} = {result}")