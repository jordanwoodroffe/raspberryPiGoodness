#Displays 3 Emoji faces in the LED matrix on Sense HAT.
#Emojis will be displayed one by one with 3 seconds interval.

from sense_hat import SenseHat
import random


class Emoji():

    sense = SenseHat()
    sense.clear()
    sense.show_message("Emojis")

    def __init__(self):
        pass
#Face 1 colour and display
    def face1(self):
        sense = SenseHat()
        sense.clear()
        b = [0, 0, 255]
        g = [0, 255, 0]
        r = [255, 0, 0]
        one = [
        b,b,b,b,b,b,b,b,
        b,r,r,b,b,r,r,b,
        b,r,r,b,b,r,r,b,
        b,b,b,g,g,b,b,b,
        b,b,b,g,g,b,b,b,
        b,g,g,b,b,g,g,b,
        b,g,g,g,g,g,g,b,
        b,g,g,g,g,g,g,b,
        ]
        sense.set_pixels(one)
#Face 2 colour and display
    def face2(self):
        sense = SenseHat()
        sense.clear()
        b = [0, 0, 255]
        g = [0, 255, 0]
        r = [255, 0, 0]
        two = [
        b,b,b,b,b,b,b,b,
        b,r,r,b,b,r,r,b,
        b,r,r,b,b,r,r,b,
        b,b,b,g,g,b,b,b,
        b,b,b,g,g,b,b,b,
        b,r,r,r,r,r,r,b,
        b,r,r,r,r,r,r,b,
        b,r,r,b,b,r,r,b,
        ]
        sense.set_pixels(two)
#Face 3 colour and display
    def face3(self):
        sense = SenseHat()
        sense.clear()
        b = [0, 0, 255]
        g = [0, 255, 0]
        r = [255, 0, 0]
        three = [
        b,b,b,b,b,b,b,b,
        b,r,r,b,b,r,r,b,
        b,r,r,b,b,r,r,b,
        b,b,b,g,g,b,b,b,
        b,b,b,g,g,b,b,b,
        b,r,r,r,r,r,r,b,
        b,r,b,b,b,b,r,b,
        b,r,r,r,r,r,r,b,
        ]
        sense.set_pixels(three)
