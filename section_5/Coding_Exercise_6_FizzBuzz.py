# When the number is divisible by 3 then instead of printing the number it should print "Fizz".
# When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

for marks in range (1,101):
#I have taken an LCM of 3 and 5 to calculate this, there are other ways to do it as well. 
    if (marks % 15) == 0: #This statement needs to stay at top because of the if-elif-else behaviour, if I put in in elif statement once the elif condition is met rest are skipped.
        print ("FizzBuzz")
    elif (marks % 3) == 0:
        print ("Fizz")
    elif (marks % 5) == 0:
        print ("Buzz")
    else: 
        print(marks)
