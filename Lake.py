from pygame import image


class Lake:

    def __init__(self,locx,locy):
        self.graphic=image.load("lake.png")
        self.walkable = False
        self.fishable = True
        self.removable = False
        self.searchable = False
        self.locx=locx
        self.locy=locy

    