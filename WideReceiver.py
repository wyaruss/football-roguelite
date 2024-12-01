from Player import Player
import random

class WideReceiver(Player): 
    meanSpeed = 85
    stdDevSpeed = 3

    meanCatch = 85
    stdDevCatch = 3

    meanRouteRunning = 80
    stdDevRouteRunning = 5

    def __init__(self, name):
        super().__init__(name)
        self.generateSpeed()
        self.generateCatch()
        self.generateRouteRunning()
        print("")

    def generateSpeed(self): 
        self.speed = random.gauss(self.meanSpeed, self.stdDevSpeed)
        self.speed = max(70, min(99, round(self.speed)))
        print(f"{self.name}'s Speed is: {self.speed}")

    def generateCatch(self): 
        self.catch = random.gauss(self.meanCatch, self.stdDevCatch)
        self.catch = max(70, min(99, round(self.catch)))
        print(f"{self.name}'s Catch is: {self.catch}")

    def generateRouteRunning(self): 
        self.routeRunning = random.gauss(self.meanRouteRunning, self.stdDevRouteRunning)
        self.routeRunning = max(70, min(99, round(self.routeRunning)))
        print(f"{self.name}'s Route Running is: {self.routeRunning}")

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