import random

class Card:
    def __init__(self,wordes):
        self.wordes=wordes
        self.wordes_player=[]
        self.wordes_computer=[]
        
    def draw_cardes(self):
        c1=random.choice(self.wordes)
        self.wordes.remove(c1)
        self.wordes_player.insert(0,c1)

        c2=random.choice(self.wordes)
        self.wordes.remove(c2)
        self.wordes_player.insert(0,c2)

        return self.wordes_player,self.wordes_computer



