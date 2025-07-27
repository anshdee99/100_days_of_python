print ("Welcome to Roller Coaster")
height = int(input ("What is your height in cm's? "))
bill = 0

if height >= 120: 
    print ("You can ride")
    age = int(input ("What is your age? "))
    if age <= 12: 
        bill += 5
        print (f"pay ${bill}")
    elif age <= 18: 
        bill += 7
        print (f"pay ${bill}")
    elif age >= 45 and age <= 55:
        bill = 0
        print (f"pay ${bill}")
        print ("Your ride is on us")
    elif age > 18:
        bill += 12
        print (f"pay ${bill}")
    else: 
        print ("Invalid input")

else: 
    print ("You can't ride")
