from simpledominion.TurnStatus import TurnStatus
from simpledominion.GameCardType import GameCardType

class CardInterface:
    def evaluate(self, TurnStatus) -> None:
    	pass
    @property
    def cardType(self) -> GameCardType:
    	pass


