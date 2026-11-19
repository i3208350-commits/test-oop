import random
from round_Management import RoundManagement 





wordes=[["H",2],["H",3],["H",4],["H",5],["H",6],["H",7],["H",8],["H",9],["H",10],["H","J"],["H","Q"],["H","K"],["H","A"]
        ,["D",2],["D",3],["D",4],["D",5],["D",6],["D",7],["D",8],["D",9],["D",10],["D","J"],["D","Q"],["D","K"],["D","A"],
        ["S",2],["S",3],["S",4],["S",5],["S",6],["S",7],["S",8],["S",9],["S",10],["S","J"],["S","Q"],["S","K"],["S","A"],
        ["C",2],["C",3],["C",4],["C",5],["C",6],["C",7],["C",8],["C",9],["C",10],["C","J"],["C","Q"],["C","K"],["C","A"]]

wordes_player=[["H",7],["H",3]]
wordes_computer=[["C","J"],["C","Q"]]
victory_player=26
victory_computer=26
draw_player=0
draw_computer=0
for i in wordes:
           
           
        
             wordes_player.append(i)
        



print(wordes_player)
def mnue():
        while True:
            print("--------Welcome to the card game--------")
            print("• 1. Play turn")
            print("• 2. Exit")
            choice=input("Enter your choice")
            if choice=="1":
                    r=RoundManagement()
                    r.drawing_cards(wordes_player,wordes_computer)
                    r.shape_Conversion()
                    r.victory_check(victory_player,victory_computer,draw_player,draw_computer,wordes_player,wordes_computer)
            if choice=="2":
                print("-----We’re sorry to see you go—goodbye!-----")
                break
                                    
    

if __name__ == '__main__':
    mnue()