#Importing Emojie from faces.emoji
from faces.emoji import Emoji
import time
import sys

def main():
        emoji = Emoji()
       
        emoji.face1()
        time.sleep(3)
        emoji.face2()
        time.sleep(3)
        emoji.face3()
        time.sleep(5)
        sys.exit(0)

if __name__ == "__main__": main()
