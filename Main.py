from WideReceiver import WideReceiver
from Cornerback import Cornerback

player1Name = input("WR name: ")
player1 = WideReceiver(player1Name)

for stat in player1.stats:
    print(f"{player1.name}'s {stat}: {player1.stats[stat]}")