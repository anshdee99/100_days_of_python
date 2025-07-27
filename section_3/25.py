print ("Welcome to the Roller Coaster")
height = int(input("What is your height in cm? "))
bill = int(0)

if height >= 120: 
    print ("You can ride the Roller Coaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print ("Your age is 12 or less, price is $5")
        bill = 5
    elif age <= 18:
        print ("Your age is 18 or less, price is $7")
        bill = 7
    else: 
        print ("Your age is above 18, price is $12")
        bill = 12
    picture = input("Do you want a picture ? Y for Yes, N for No ")
    if picture == "Y": #Price of a picture is $3
        print (f"Your total is {bill + 3}")
else: 
    print ("You can not ride the Roller Coaster")
