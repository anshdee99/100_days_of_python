print ("Welcome to the Roller Coaster")
height = int(input("What is your height in cm? "))

if height >= 120: 
    print ("You can ride the Roller Coaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print ("Please pay $5, your age is 12 or less")
    elif age <= 18:
        print ("Please pay $7, your age is 18 or less")
    else: 
        print ("Please pay $12, your age is above 18")
else: 
    print ("You can not ride the Roller Coaster")
