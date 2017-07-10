from Watertank import watertank
import pygame
pygame.init()
tank = watertank(800, 800)
done = False
while not done:

    x = int(input("enter a number between -3 and 3: "))
    if x > 3 or x < -3:
        done = True
    else:
        tank.fill(x)
        print(tank.water_l)
