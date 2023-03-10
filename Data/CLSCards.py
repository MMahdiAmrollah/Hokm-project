import random


class Cards:
    def __init__(self):
        self.Spade = {'Spade02': 2, 'Spade03': 3, 'Spade04': 4, 'Spade05': 5, 'Spade06': 6, 'Spade07': 7,
                      'Spade08': 8, 'Spade09': 9, 'Spade10': 10, 'Spade11': 11, 'Spade12': 12, 'Spade13': 13, 'Spade14': 14}
        self.Club = {'Club02': 2, 'Club03': 3, 'Club04': 4, 'Club05': 5, 'Club06': 6, 'Club07': 7,
                     'Club08': 8, 'Club09': 9, 'Club10': 10, 'Club11': 11, 'Club12': 12, 'Club13': 13, 'Club14': 14}
        self.Diamond = {'Diamond02': 2, 'Diamond03': 3, 'Diamond04': 4, 'Diamond05': 5, 'Diamond06': 6, 'Diamond07': 7,
                        'Diamond08': 8, 'Diamond09': 9, 'Diamond10': 10, 'Diamond11': 11, 'Diamond12': 12, 'Diamond13': 13, 'Diamond14': 14}
        self.Heart = {'Heart02': 2, 'Heart03': 3, 'Heart04': 4, 'Heart05': 5, 'Heart06': 6, 'Heart07': 7,
                      'Heart08': 8, 'Heart09': 9, 'Heart10': 10, 'Heart11': 11, 'Heart12': 12, 'Heart13': 13, 'Heart14': 14}
        self.DeckOfCards = {'Spade02': 2, 'Spade03': 3, 'Spade04': 4, 'Spade05': 5, 'Spade06': 6, 'Spade07': 7,
                            'Spade08': 8, 'Spade09': 9, 'Spade10': 10, 'Spade11': 11, 'Spade12': 12, 'Spade13': 13, 'Spade14': 14, 'Club02': 2, 'Club03': 3, 'Club04': 4, 'Club05': 5, 'Club06': 6, 'Club07': 7,
                            'Club08': 8, 'Club09': 9, 'Club10': 10, 'Club11': 11, 'Club12': 12, 'Club13': 13, 'Club14': 14,
                            'Diamond02': 2, 'Diamond03': 3, 'Diamond04': 4, 'Diamond05': 5, 'Diamond06': 6, 'Diamond07': 7,
                            'Diamond08': 8, 'Diamond09': 9, 'Diamond10': 10, 'Diamond11': 11, 'Diamond12': 12, 'Diamond13': 13, 'Diamond14': 14,
                            'Heart02': 2, 'Heart03': 3, 'Heart04': 4, 'Heart05': 5, 'Heart06': 6, 'Heart07': 7,
                            'Heart08': 8, 'Heart09': 9, 'Heart10': 10, 'Heart11': 11, 'Heart12': 12, 'Heart13': 13, 'Heart14': 14}
        self.PlayGroundCards = {}

    def PrimitiveDistributer(self):
        for i in range(1, 5):
            DeckKeysList = list(self.DeckOfCards.keys())
            RandedCard = random.choices(DeckKeysList)[0]
            self.PlayGroundCards[RandedCard] = self.DeckOfCards[RandedCard]
        print(self.PlayGroundCards)

    def SetDistributer(self):
        pass
