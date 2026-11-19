

wordes_player=[["H",7],["H",3]]
wordes_computer=[["C",7],["C","Q"]]
victory_player=26
victory_computer=26
draw_player=0
draw_computer=0




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
        

    def victory_check(self,victory_player,victory_computer,draw_player,draw_computer,wordes_player,wordes_computer):
        
        
        if self.player[1]>self.computer[1]:
            victory_player+=1
            victory_computer-=1
            wordes_player.append(self.computer)
            wordes_player.append(self.player)
            self.Victory_Print(victory_player,victory_computer)
        if self.computer[1]>self.player[1]:
           victory_computer+=1
           victory_player-=1
           wordes_computer.append(self.player)
           wordes_computer.append(self.computer)
           
           self.loss_Print(victory_player,victory_computer)
           

        if self.computer==self.player:
            draw_player+=1
            draw_computer+=1
            self.draw(victory_player,victory_computer)
       

    def Victory_Print(self,victory_player,victory_computer):
        print("========== TURN ==========")
        print(f"Player: {self.player}")
        print(f"Computer: {self.computer}")
        print("Player won the round!")
        print(f"Player cards:{victory_player}")
        print(f"Computer cards: {victory_computer}")

    def loss_Print(self,victory_player,victory_computer):
        print("========== LOSS ==========")
        print(f"Player: {self.player}")
        print(f"Computer: {self.computer}")
        print("Unfortunately, you lost!")
        print(f"Player cards:{victory_player}")
        print(f"Computer cards{victory_computer}")

    def draw(self,victory_player,victory_computer):
        print("========== DRAW ==========")
        print(f"Player: {self.player}")
        print(f"Computer: {self.computer}")
        print("Unfortunately, you lost!")
        print(f"Player cards:{victory_player}")
        print(f"Computer cards{victory_computer}")

   



#   בוצעה בדיקה על המחלקה עצמאית ועובדת כדרוש
r=RoundManagement()
r.drawing_cards(wordes_player,wordes_computer)
r.shape_Conversion()
r.victory_check(victory_player,victory_computer,draw_player,draw_computer,wordes_player,wordes_computer)
