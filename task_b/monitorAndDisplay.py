
from sense_hat import SenseHat
from time import sleep
from time import asctime
import json

class Reader():
     
    def __init__(self):
        pass         
    #Display The Temprature on senseHat
    def displayTemp(self):
        import time
        sense = SenseHat()
        with open("config.json","r") as f:
            temp_dict = json.load(f)
         
        while True:
            temp = round(sense.get_temperature())
            #If the level of temperature is cold, display temperature with bluecolour.
            if (temp <=temp_dict["cold_max"]):
                message = '%d' %(temp)
                sense.show_message(message, scroll_speed=(0.1),text_colour=[0,0,255], back_colour= [0,0,0])
                time.sleep(10)            
                sense.clear() 

            #f the level of temperature is comfortable, display temperature with greencolour.
            if (temp > temp_dict["comfortable_min"] and temp <= temp_dict["comfortable_max"]):
                message = '%d' %(temp)
                sense.show_message(message, scroll_speed=(0.1),text_colour=[0,255,0], back_colour= [0,0,0])
                time.sleep(10)            
                sense.clear() 

            #If the level of temperature is hot, display temperature with redcolour.
            if (temp > temp_dict["hot_min"]):
                message = '%d' %(temp)
                sense.show_message(message, scroll_speed=(0.1),text_colour=[255,0,0], back_colour= [0,0,0])
                time.sleep(10)            
                sense.clear()  

def main():
    Reader1 = Reader()
    Reader1.displayTemp()        	

if __name__ == "__main__": main()
