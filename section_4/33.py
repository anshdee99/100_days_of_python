import random
list = ["Ansh", "Nidhi", "Duanshi", "Parveen", "Vipul", "Vel"]

# Option 1
print(random.choice(list))

# Option 2
random_index = random.randint(0,5)
print(list[random_index])
