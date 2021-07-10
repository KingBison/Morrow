from pygame import image


class Grass:

    def __init__(self,locx,locy):
        self.graphic=image.load("grass.png")
        self.walkable = True
        self.fishable = False
        self.removable = False
        self.searchable = True
        self.locx=locx
        self.locy=locy

    