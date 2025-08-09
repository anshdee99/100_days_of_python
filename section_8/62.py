#Function that allows for input. 
def greet_again(name, location):
    print (f"Hello {name}")
    print (f"What is it like in {location}?")

greet_again("Ansh","Nowhere") #Argumets can be defined like this. 
greet_again (location = "Ding", name = "Ansh") #You can define the arguments like this as well. 
greet_again (name = "Ansh", location = "Ding") #The position does not matter if they are defined like this. 
#Both examples returned the same output. Line 7,8. 
