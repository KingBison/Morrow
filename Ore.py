from pygame import image

class Ore:

    def __init__(self,locx,locy):
        self.graphic=image.load("ore.png")
        self.walkable = False
        self.fishable = False
        self.removable = True
        self.searchable = True
        self.durability = 5
        self.locx=locx
        self.locy=locy

    

