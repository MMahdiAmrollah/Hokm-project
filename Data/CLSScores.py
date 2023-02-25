class Scores:
    def __init__(self):
        self.TeamA = []
        self.TeamB = []
        self.TeamARoundWins = 0
        self.TeamBRoundWins = 0
        self.TeamASetWins = 0
        self.TeamBSetWins = 0
        self.GameWinner = 0

    def RoundWinnerSaver(self):

        if len(self.TeamA) == 7:
            self.TeamARoundWins +=1
            return self.TeamA
        elif len(self.TeamB) == 7:
            self.TeamBRoundWins +=1
            return self.TeamB

    def SetWinnerDiterminator(self):

        if self.TeamARoundWins == 7:
            self.TeamASetWins +=1
            return self.TeamA
        elif self.TeamBRoundWins == 7:
            self.TeamBSetWins +=1
            return self.TeamB


    def GameWinnerDeterminator(self):

        if self.TeamASetWins == 7:
            self.GameWinner = 'TeamA'
            return self.TeamA
        elif self.TeamASetWins == 7:
            self.GameWinner = 'TeamB'
            return self.TeamB

    def SetKotDetector(self):
        pass

    def GameKotDetector(self):
        pass
