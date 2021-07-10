from pygame import image


class Inventory:


    def __init__(self):
        self.contents = []
        self.graphic = image.load("inventory.png")