

class Printi:
    def __init__(self):
          pass
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

