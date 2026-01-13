import random
 
amount = int(input("How many random numbers would you like to generate? "))
 
numbers = [random.randint(1, 10) for _ in range(amount)]
 
print("Generated numbers:")
print(", ".join(str(num) for num in numbers))