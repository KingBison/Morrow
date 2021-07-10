from Sword import Sword
from Pickaxe import Pickaxe
import Inventory
from pygame import image
front = image.load("player_front.png")
back = image.load("player_back.png")
left = image.load("player_left.png")
right = image.load("player_right.png")

class Player:
    
    def __init__(self,init_x,init_y):
        self.item_in_hand = Sword()
        self.inventory = Inventory.Inventory()
        self.graphic = front
        self.x=init_x
        self.y=init_y

    def moveUp(self):
        self.graphic = back
        self.y-=1
    def moveDown(self):
        self.graphic = front
        self.y+=1
    def moveLeft(self):
        self.graphic = left
        self.x-=1
    def moveRight(self):
        self.graphic = right
        self.x+=1

