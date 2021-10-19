from simpledominion.GameCardType import GameCardType
from simpledominion.CardInterface import CardInterface


class GameCard(CardInterface):

    def __init__(self, cardType: GameCardType):
        self._cardType = cardType

    @property
    def cardType(self):
        return self._cardType

    def evaluate(self, TurnStatus) -> None:
        TurnStatus.coins += self._cardType.plusCoins
        TurnStatus.buys += self._cardType.plusBuys
        TurnStatus.cards += self._cardType.plusCards
        TurnStatus.actions += self._cardType.plusActions
