import random

width = 10
height = 10
 

snake = [(0, 0)]
 

food = (random.randint(0, width - 1), random.randint(0, height - 1))
 
direction = (1, 0)
 
while True:
    for i in range(height):
        for j in range(width):
            if (i, j) in snake:
                print("X", end=" ")
            elif (i, j) == food:
                print("F", end=" ")
            else:
                print(".", end=" ")
        print()
 

    