length = int(input("Please enter line length: "))

orientation = input("Do you want a horizontal or vertical line? ").strip().lower()

if orientation == "horizontal":
    print("*" * length)

elif orientation == "vertical":
    for _ in range(length):
        print("*")

else:
    print("Invalid option. Please enter 'horizontal' or 'vertical'.")