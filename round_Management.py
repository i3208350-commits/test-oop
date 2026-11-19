from printi import Printi
# from game import Card
wordes_player=[["H",7],["H",3]]
wordes_computer=[["C",4],["C","Q"]]
victory_player=26
victory_computer=26
draw_player=0
draw_computer=0
j=11
q=12
k=13
As=14



class RoundManagement:
    def __init__(self):
        # self.victory_player=victory_player
        # self.victory_computer=victory_computer
        self.player=0
        self.computer=0
        print("examination")
        
       
    def drawing_cards(self,wordes_player,wordes_computer):
       
        self.player=wordes_player[0]
        wordes_player.pop(0)
        
        self.computer=wordes_computer[0]
        wordes_computer.pop(0)
        print(f"The player's card is:___{self.player}")
        print(f"The computer's card is:___{self.computer}")
    def shape_Conversion(self):
        if self.player[1]=="J":
            self.player[1]=11
        if self.player[1]=="Q":
            self.player[1]=12
        if self.player[1]=="K":
            self.player[1]=13
        if self.player[1]=="A":
             self.player[1]=14
        if self.computer[1]=="J":
                    self.computer[1]=11
        if self.computer[1]=="Q":
                    self.computer[1]=12
        if self.computer[1]=="K":
                    self.computer[1]=13
        if self.computer[1]=="A":
                     self.computer[1]=14
        
    # def conversion_returned(self):
    #             if self.player[1]==11:
    #                 self.player[1]=="J"
    #             if self.player[1]==12:
    #                 self.player[1]=="Q"
    #             if self.player[1]==13:
    #                 self.player[1]=="K"
    #             if self.player[1]==14:
    #                  self.player[1]=="A"
    #             if self.computer[1]==11:
    #                         self.computer[1]="J"
    #             if self.computer[1]==12:
    #                         self.computer[1]=="Q"
    #             if self.computer[1]==13:
    #                         self.computer[1]=="K"
    #             if self.computer[1]==14:
    #                          self.computer[1]=="A"
    def victory_check(self,victory_player,victory_computer,draw_player,draw_computer,wordes_player,wordes_computer):
        
        
        if self.player[1]>self.computer[1]:
            victory_player+=1
            victory_computer-=1
            # self.conversion_returned()
            wordes_player.append(self.computer)
            wordes_player.append(self.player)
            Printi.Victory_Print(self,victory_player,victory_computer)
        if self.computer[1]>self.player[1]:
           victory_computer+=1
           victory_player-=1
        #    self.conversion_returned()
           wordes_computer.append(self.player)
           wordes_computer.append(self.computer)
           
           Printi.loss_Print(self,victory_player,victory_computer)
           

        if self.computer==self.player:
            draw_player+=1
            draw_computer+=1
            self.conversion_returned()
            Printi.draw(victory_player,victory_computer)
       

   



#   בוצעה בדיקה על המחלקה עצמאית ועובדת כדרוש
# d=Card
# r=RoundManagement()
# r.drawing_cards(wordes_player,wordes_computer)
# r.shape_Conversion()
# r.victory_check(victory_player,victory_computer,draw_player,draw_computer,wordes_player,wordes_computer)
