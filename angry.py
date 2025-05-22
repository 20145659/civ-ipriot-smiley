from smiley import Smiley

class Angry(Smiley):
    def __init__(self):
        super().__init__(complexion=self.RED)
        self.draw_mouth()
        self.draw_eyes()

    def draw_mouth(self):
        mouth = [49, 50, 51, 52, 53, 54]  # Flat or angry shape
        for pixel in mouth:
            self.pixels[pixel] = self.BLANK

    def draw_eyes(self):
        # Eyebrows (slanted inward)
        eyebrows = [1, 6, 9, 14]  # Outer brow line
        for pixel in eyebrows:
            self.pixels[pixel] = self.BLANK

        # Eyes (underneath the brows)
        eyes = [18, 21]
        for pixel in eyes:
            self.pixels[pixel] = self.BLANK