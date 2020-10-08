import random
health=50
difficulty=3
health_potion=random.randint(25,50)/difficulty
health=health+health_potion
print(health)