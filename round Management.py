

wordes_player=[["H",7],["H",3]]
wordes_computer=[["D",2],["D",9]]
victory_player=0
victory_computer=0
draw_player=0
draw_computer=0




class RoundManagement:
    def __init__(self):
        self.player=0
        self.computer=0
        print("examination")
        
       
    def drawing_cards(self,wordes_player,wordes_computer):
        print("examination")
        self.player=wordes_player[0]
        self.computer=wordes_computer[0]
    def victory_check(self,victory_player,victory_computer,draw_player,draw_computer,wordes_player,wordes_computer):
        if self.player[1]>self.computer[1]:
            victory_player+=1
            wordes_player.append(self.computer)
            


        if self.computer[1]>self.player[1]:
           victory_computer+=1
           wordes_computer.append(self.player)

        if self.computer==self.player:
            draw_player+=1
            draw_computer+=1
        print(victory_player)
        print(victory_computer)



# בוצעה בדיקה על המחלקה עצמאית ועובדת כדרוש
# r=RoundManagement()
# r.drawing_cards(wordes_player,wordes_computer)
# r.victory_check(victory_player,victory_computer,draw_player,draw_computer,wordes_player,wordes_computer)
