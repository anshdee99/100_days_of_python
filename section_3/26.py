print ("Welcome to the Python Pizza Deliveries")
size = input("What siez pizza do you want? S,M,L: ") #S = $15, M = $20, L = $25
peperroni = input("Do you want peperroni on your pizza ? Y or N: ") #S Peperoni = $2, M or L Peperoni = $3
extra_cheese = input("Do you want extra cheese on your pizza ? Y or N: ") #$1 for extra cheese
bill = 0

if size == "S":
    print ("You chose S, it's $15")
    bill = 15
    if peperroni == "Y":
        bill += 2
    if extra_cheese == "Y":
        bill += 1
        print (f"Your total for a Small Pizza is {bill}")
elif size == "M":
    print ("You chose M, price is $20")
    bill = 20
    if peperroni == "Y":
        bill += 3
        print (f"Your total for a Med Pizza is {bill}")
elif size == "L":
    print ("You chose M, price is $25")
    bill = 25
    if peperroni == "Y":
        bill += 3
        print (f"Your total for a Large Pizza is {bill}")
else: 
    print ("Please enter a valid value S, M or L")
