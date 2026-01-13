str = input("Say something: ")
vary = 0
for char in str: 
    if vary == 0 :
        char = char.upper()
        print(char, end="")
        vary = vary + 1
    elif vary == 1:
        char = char.lower()
        print(char, end="")
        vary = vary - 1