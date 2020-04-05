#triggering the roll of the die when shaking the Pi.
#detecting shaking motion by IMU sensor and then display the die in random matter.

class Player():

    def __init__(self, name, score, number):
        self.name = name
        self.score = score
        self.number = number

    def getScore(self):
        return self.score

    def getName(self):
        return self.name
    
    def getNumber(self):
        return self.number
        
    def increaseScore(self, score):
        self.score += score

    def hasWon(self):
        import time
        from sense_hat import SenseHat
        sense = SenseHat() # initialize 
        sense.clear()
       
    # Setup dice display variables
        b = [0, 0, 0]
        g = [0, 255, 0]

        if (self.getNumber() == 1):
            b = [0, 0, 0]
            g = [0, 255, 0]
            
            win1 = [
            b,b,b,g,g,b,b,b,
            b,b,g,g,g,b,b,b,
            b,g,g,g,g,b,b,b,
            b,b,b,g,g,b,b,b,
            b,b,b,g,g,b,b,b,
            b,b,b,g,g,b,b,b,
            b,g,g,g,g,g,g,b,
            b,g,g,g,g,g,g,b,
            ]
            sense.set_pixels(win1)
            time.sleep(3)
        
        if (self.getNumber() == 2):
            b = [0, 0, 0]
            g = [0, 255, 0]
            
            win2 = [
            b,b,b,g,g,b,b,b,
            b,g,g,g,g,g,b,b,
            b,g,g,b,b,g,g,b,
            b,b,b,g,g,g,b,b,
            b,b,b,g,g,b,b,b,
            b,b,g,g,b,b,b,b,
            b,g,g,g,g,g,g,b,
            b,g,g,g,g,g,g,b,
            ]
            sense.set_pixels(win2)
            time.sleep(3)
        


    def roll_dice(self):
        import time
        import random
        from sense_hat import SenseHat
        sense = SenseHat() # initialize 
        sense.clear()

        while True:
            x, y, z = sense.get_accelerometer_raw().values()

            x = abs(x)
            y = abs(y)
            z = abs(z)
        
        
            if x > 1.4 or y > 1.4 or z > 1.4:    

                b = [0, 0, 0]
                g = [0, 255, 0]
                r = [255, 0, 0]

                one = [
                b,b,b,b,b,b,b,b,
                b,b,b,b,b,b,b,b,
                b,b,b,b,b,b,b,b,
                b,b,b,g,g,b,b,b,
                b,b,b,g,g,b,b,b,
                b,b,b,b,b,b,b,b,
                b,b,b,b,b,b,b,b,
                b,b,b,b,b,b,b,b,
                ]

                two = [
                b,b,b,b,b,b,b,b,
                b,g,g,b,b,b,b,b,
                b,g,g,b,b,b,b,b,
                b,b,b,b,b,b,b,b,
                b,b,b,b,b,b,b,b,
                b,b,b,b,g,g,b,b,
                b,b,b,b,g,g,b,b,
                b,b,b,b,b,b,b,b,
                ]

                three = [
                g,g,b,b,b,b,b,b,
                g,g,b,b,b,b,b,b,
                b,b,b,b,b,b,b,b,
                b,b,b,g,g,b,b,b,
                b,b,b,g,g,b,b,b,
                b,b,b,b,b,b,b,b,
                b,b,b,b,b,b,g,g,
                b,b,b,b,b,b,g,g,
                ]

                four = [
                b,b,b,b,b,b,b,b,
                b,g,g,b,b,g,g,b,
                b,g,g,b,b,g,g,b,
                b,b,b,b,b,b,b,b,
                b,b,b,b,b,b,b,b,
                b,g,g,b,b,g,g,b,
                b,g,g,b,b,g,g,b,
                b,b,b,b,b,b,b,b,
                ]

                five = [
                g,g,b,b,b,b,g,g,
                g,g,b,b,b,b,g,g,
                b,b,b,b,b,b,b,b,
                b,b,b,g,g,b,b,b,
                b,b,b,g,g,b,b,b,
                b,b,b,b,b,b,b,b,
                g,g,b,b,b,b,g,g,
                g,g,b,b,b,b,g,g,
                ]

                six = [
                r,r,b,b,b,b,r,r,
                r,r,b,b,b,b,r,r,
                b,b,b,b,b,b,b,b,
                r,r,b,b,b,b,r,r,
                r,r,b,b,b,b,r,r,
                b,b,b,b,b,b,b,b,
                r,r,b,b,b,b,r,r,
                r,r,b,b,b,b,r,r,
                ]

                r = random.randint(1,6)
                
                if r == 1:
                    sense.set_pixels(one)
                    self.increaseScore(1)
                    time.sleep(2)
                    print (self.getName(), "rolls", r)
                    break
                elif r == 2:
                    sense.set_pixels(two)
                    self.increaseScore(2)
                    time.sleep(2)
                    print (self.getName(), "rolls", r)
                    break
                elif r == 3:
                    sense.set_pixels(three)
                    self.increaseScore(3)
                    time.sleep(2)
                    print (self.getName(), "rolls", r)
                    break
                elif r == 4:
                    sense.set_pixels(four)
                    self.increaseScore(4)
                    time.sleep(2)
                    print (self.getName(), "rolls", r)
                    break
                elif r == 5:
                    sense.set_pixels(five)
                    self.increaseScore(5)
                    time.sleep(2)
                    print (self.getName(), "rolls", r)
                    break
                elif r == 6:
                    sense.set_pixels(six)
                    self.increaseScore(6)
                    time.sleep(2)
                    print (self.getName(), "rolls", r)
                    break
          
