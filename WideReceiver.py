from Player import Player
import random

class WideReceiver(Player): 
    @classmethod
    def stat_metadata(cls) -> dict:
        return {
            "speed": {"mean": 85, "sd": 2},
            "strength": {"mean": 70, "sd": 5},
            "quickness": {"mean": 80, "sd": 5},
            "route_running": {"mean": 80, "sd": 5},
            "catch": {"mean": 85, "sd": 5}
        }

    def runRoute(self): 
        routeRoll = random.randint(1, self.routeRunning)
        print(f"{self.name}'s Route Roll is: {routeRoll} vs. {self.routeRunning}")
        
        if routeRoll <= self.routeRunning:
            success = True
            print(f"{self.name} is successful running his route.")
            print("")
        else:
            success = False
            print(f"{self.name} is unsuccessful at running his route.")
            print("")

        #Calculate the difference between the player's roll and their stat to determine how successful they are at the task. 
        difference = self.routeRunning - routeRoll 