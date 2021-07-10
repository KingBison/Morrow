from pygame import image

class Tree:

    def __init__(self,locx,locy):
        self.graphic=image.load("tree.png")
        self.walkable = False
        self.fishable = False
        self.removable = True
        self.searchable = False
        self.durability = 5
        self.locx=locx
        self.locy=locy

    