year = input("Insert a leap year immediatly ")
year = int(year)

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year!")
        else:
            print("not leap year!")
    else:
        print("Leap year!")
else:
    print("Not leap year")
    