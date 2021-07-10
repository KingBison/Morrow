from Rod import Rod
from Sword import Sword
from Axe import Axe
from Pickaxe import Pickaxe
from pygame.constants import K_SPACE, K_a, K_d, K_s, K_w
import Player
import Ore
import Tree
import Lake
import Grass
import random
import pygame
from pygame import key
from pygame import display
from pygame import event
from pygame import image
from pygame import mixer
from time import sleep


direction_facing="down"

inventory_locations = []

for i in range(5):
    x = 52
    y = 45
    for k in range(3):
        inventory_locations.append((52+k*88,45+i*80))


mixer.init()
mixer.music.load("Morrow_Song.mp3")
mixer.music.play(-1)


pygame.init()
window_width = 1000
window_height = 600
screen = display.set_mode((window_width,window_height))
display.set_caption("Morrow")

p = Player.Player(0,0)
p.inventory.contents.append(Pickaxe())
p.inventory.contents.append(Axe())
p.inventory.contents.append(Sword())






world = []






for i in range(int(window_width/50)):
    for k in range(int(window_height/50)):
        rand = random.randint(0,99)
        if(rand <2):
            new_block = Ore.Ore(i,k)
        elif(rand<70):
            new_block = Grass.Grass(i,k)
        elif(rand<98):
            new_block = Tree.Tree(i,k)
        else:
            new_block = Lake.Lake(i,k)
        
        world.append(new_block)

        screen.blit(new_block.graphic,(new_block.locx,new_block.locy))




open = True

while open:
    for hit in event.get():
        if hit.type == pygame.QUIT:
            open = False
        if hit.type == pygame.KEYDOWN:

            old_loc = [p.x,p.y]

            if hit.key == pygame.K_a:
                direction_facing = "left"
                p.moveLeft()
            if hit.key == pygame.K_d:
                direction_facing = "right"
                p.moveRight()
            if hit.key == pygame.K_w:
                direction_facing = "up"
                p.moveUp()
            if hit.key == pygame.K_s:
                direction_facing = "down"
                p.moveDown()
            if hit.key == pygame.K_RIGHT:
                p.item_in_hand=Pickaxe()
            if hit.key == pygame.K_LEFT:
                p.item_in_hand=Axe()
            if hit.key == pygame.K_UP:
                p.item_in_hand=Sword()
            if hit.key == pygame.K_DOWN:
                p.item_in_hand=Rod()

            if hit.key == pygame.K_SPACE:
                if type(p.item_in_hand) != type(Rod()):
                    if direction_facing == "right":
                        x = p.x
                        y=p.y
                        temp_graphic = p.item_in_hand.graphic
                        for i in range(24):
                            temp_graphic = pygame.transform.rotate(temp_graphic,-15)
                            temp_graphic = pygame.transform.scale(temp_graphic,(50,50))
                            screen.blit(temp_graphic,(x*50+10,x*50-12))
                            sleep(.1)
                            display.update()
                            
                    elif direction_facing == "left":
                        temp_graphic = p.item_in_hand.graphic
                        screen.blit(pygame.transform.flip(p.item_in_hand.graphic,True,False),(p.x*50-10,p.y*50-12))
                    elif direction_facing == "up":
                        temp_graphic = p.item_in_hand.vert_graphic
                        if type(p.item_in_hand) == type(Rod()):
                            screen.blit(p.item_in_hand.up_graphic,(p.x*50+10,p.y*50-12))
                        else :
                            screen.blit(p.item_in_hand.vert_graphic,(p.x*50+10,p.y*50-12))
                        screen.blit(p.graphic,(p.x*50,p.y*50))
                    elif direction_facing == "down":
                        temp_graphic = p.item_in_hand.vert_graphic

                        screen.blit(p.item_in_hand.down_graphic,(p.x*50-10,p.y*50-12))


            

            if hit.key == pygame.K_f:
                open_inv = True
                while open_inv:


                    for hit in event.get():
                        if hit.type == pygame.QUIT:
                            open_inv = False
                            open = False
                        if hit.type == pygame.KEYDOWN:
                            if hit.key == pygame.K_f:
                                open_inv = False

                    screen.blit(p.inventory.graphic,(250,150))


                    for i in range(len(p.inventory.contents)):
                        pygame.draw.circle(screen, (230,230,230), (inventory_locations[i][0]+275,inventory_locations[i][1]+175),30)
                        screen.blit(p.inventory.contents[i].graphic,(inventory_locations[i][0]+250,inventory_locations[i][1]+150))

                            
                    
                    display.update()




            for block in world:
                if block.locx == p.x and block.locy == p.y:
                    if block.walkable == False:
                        p.x=old_loc[0]
                        p.y=old_loc[1]






    for block in world:
        screen.blit(block.graphic,(block.locx*50,block.locy*50))

    screen.blit(p.graphic,(p.x*50,p.y*50))

    if direction_facing == "right":
        screen.blit(p.item_in_hand.graphic,(p.x*50+10,p.y*50-12))
    elif direction_facing == "left":
        screen.blit(pygame.transform.flip(p.item_in_hand.graphic,True,False),(p.x*50-10,p.y*50-12))
    elif direction_facing == "up":
        if type(p.item_in_hand) == type(Rod()):
            screen.blit(p.item_in_hand.up_graphic,(p.x*50+10,p.y*50-12))
        else :
            screen.blit(p.item_in_hand.vert_graphic,(p.x*50+10,p.y*50-12))
        screen.blit(p.graphic,(p.x*50,p.y*50))
    elif direction_facing == "down":
        if type(p.item_in_hand) == type(Rod()):
            screen.blit(p.item_in_hand.down_graphic,(p.x*50-10,p.y*50-12))
        else:
            screen.blit(p.item_in_hand.vert_graphic,(p.x*50-10,p.y*50-12))
    
    display.update()







pygame.quit()