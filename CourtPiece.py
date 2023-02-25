from Data import CLSGameManager
from Data import CLSGamer
from Data import CLSCards
from Data import CLSScores

INSGameManager = CLSGameManager.GameManager()
INSGamer = CLSGamer.Gamer()
INSCards = CLSCards.Cards()
INSScores = CLSScores.Scores()

INSGameManager.GamersNameAndOrderReciever()
INSGameManager.TrumpCallerDeterminator()
