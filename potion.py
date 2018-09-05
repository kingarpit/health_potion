import random

health=50

difficulty=int(raw_input("Enter your choice between 1 to 3 : "))
print(difficulty)

potion_health=random.randint(25,50)/difficulty

health=health+potion_health

print (health)



