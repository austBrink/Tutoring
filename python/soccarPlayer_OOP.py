# Write a class named SoccerPlayer that contains data on player’s name (a string), jersey number (an integer), and goals scored (an integer). Add the getter and setter methods. Create 2 soccer player objects and display the name, jersey number and goals scored.

class SoccerPlayer:
    # every class has a constructor. 
    # this builds the class
    def __init__(self, playerName, jerseyNumber, goalsScored):
        self.playerName = playerName
        self.jerseyNumber = jerseyNumber
        self.goalsScored = goalsScored

    def getPlayerName(self):
        return self.playerName
    
    def getJerseyNumber(self):
        return self.jerseyNumber

    def getGoalsScored(self):
        return self.goalsScored

    def setPlayerName(self, newName):
        self.playerName = newName

    def setJerseyNumber(self, newNumber):
        self.jerseyNumber = newNumber
    
    def setGoalsScored(self, newGoals):
        self.goalsScored = newGoals


sp1 = SoccerPlayer("Andre",10,2)

print(sp1.getPlayerName())
sp1.setPlayerName("Alexi")
print(sp1.getPlayerName())
print(sp1.getJerseyNumber())
print(sp1.getGoalsScored())

sp2 = SoccerPlayer("Alex", 12, 3)
print(sp2.getPlayerName())
print(sp2.getJerseyNumber())
print(sp2.getGoalsScored())

    

