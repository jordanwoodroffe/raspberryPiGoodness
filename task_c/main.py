from classes.electronicDie import Player
import datetime
import sys
import csv

def main():
    Player1 = Player("Player1", 0, 1)
    Player2 = Player("Player2", 0, 2)

    while True:
        Player1.roll_dice() 
        print ("Player 1's total score is:", Player1.getScore())
        if(Player1.getScore() > 10):
            Player1.hasWon()
            print ("Player 1 has won with of total score of:", Player1.getScore())
            now = datetime.datetime.now()
            with open('winners.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([now.strftime("%Y-%m-%d %H:%M:%S")])
                writer.writerow(["Player 1 has won with of total score of:"])
                writer.writerow([Player1.getScore()])    
            sys.exit(0)
        Player2.roll_dice()
        print ("Player 2's total score is:", Player2.getScore())
        if(Player2.getScore() > 10):
            print ("Player 2 has won with of total score of:", Player2.getScore())
            Player2.hasWon()
            now = datetime.datetime.now()
            with open('winners.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([now.strftime("%Y-%m-%d %H:%M:%S")])
                writer.writerow(["Player 2 has won with of total score of:"])
                writer.writerow([Player2.getScore()])     
            sys.exit(0)

     

        
       
            

if __name__ == "__main__": main()