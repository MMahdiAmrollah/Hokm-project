from Data import CLSCards
import os

INSCards = CLSCards.Cards()
import random


class GameManager:
    def __init__(self):
        self.GamersNameAndOrder = {}
        self.PlayGroundCards = {}
        self.TrumpCallerName = ''
        self.Trump = {}
        self.TurnNumber = 0
        self.SetNumber = 0

###########################################

    def Partner (player_list:list):
        TeamA =[]
        TeamB = []
        random.shuffle(player_list)
        TeamA = [player_list[0],player_list[2]]
        TeamB = [player_list[1],player_list[3]]
        return TeamA,TeamB

############################################
    def GamersNameAndOrderReciever(self):
        for i in range(1, 5):
            self.GamersNameAndOrder[input(
                f'Please enter Gamer 0{i} name :')] = i
        os.system('cls')
        print(f'Gamers with their order are :\n{self.GamersNameAndOrder}')

    def GamerCaller(self):
        pass

    def TrumpCallerDeterminator(self):
        Status = True
        while Status:
            INSCards.PrimitiveDistributer()
            for k, v in INSCards.PlayGroundCards.items():
                if v == 14:
                    PlGrCrdsVals = list(INSCards.PlayGroundCards.values())
                    x = PlGrCrdsVals.index(14)
                    self.TrumpCallerName = list(
                        self.GamersNameAndOrder.keys())[x]
                    Status = False
                    print(f'Trump Caller is : {self.TrumpCallerName}')
                    break
            INSCards.PlayGroundCards = {}

    def PartnerDeterminator(self):
        pass

    def TurnCounter(self):
        pass

    def SetCounter(self):
        pass

    def TurnWinnerDeterminator(self):
        pass
