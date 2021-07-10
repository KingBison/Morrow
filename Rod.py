from pygame import image

class Rod:

    def __init__(self):
        self.graphic = image.load("rod.png")
        self.down_graphic = image.load("rod_down.png")
        self.up_graphic = image.load("rod_up.png")