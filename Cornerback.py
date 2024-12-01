from Player import Player
import random

class Cornerback(Player): 
    meanSpeed = 85
    stdDevSpeed = 3

    meanCoverage = 85
    stdDevCoverage = 3

    meanBallSkills = 80
    stdDevBallSkills = 5

    def __init__(self, name): 
        super().__init__(name)
        self.generateSpeed()
        self.generateCoverage()
        self.generateBallSkills()
        print("")

    def generateSpeed(self): 
        self.speed = random.gauss(self.meanSpeed, self.stdDevSpeed)
        self.speed = max(70, min(99, round(self.speed)))
        print(f"{self.name}'s Speed is: {self.speed}")

    def generateCoverage(self): 
        self.coverage = random.gauss(self.meanCoverage, self.stdDevCoverage)
        self.coverage = max(70, min(99, round(self.coverage)))
        print(f"{self.name}'s Coverage is: {self.coverage}")

    def generateBallSkills(self): 
        self.ballSkills = random.gauss(self.meanBallSkills, self.stdDevBallSkills)
        self.ballSkills = max(70, min(99, round(self.ballSkills)))
        print(f"{self.name}'s Ball Skills is: {self.ballSkills}")

    def coverRoute(self): 
        coverageRoll = random.randint(1, self.coverage)
        print(f"{self.name}'s Coverage Roll is: {coverageRoll} vs {self.coverage}")

        if coverageRoll <= self.coverage:
            success = True
            print(f"{self.name} is successful at covering the opposing receiver's route.")
            print("")
        else:
            success = False
            print(f"{self.name} is unsuccessful at covering the opposing receiver's route.")
            print("")

        #Calculate the difference between the player's roll and their stat to determine how successful they are at the task. 