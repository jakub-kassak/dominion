from typing import Optional
from simpledominion.CardInterface import CardInterface
from simpledominion.GameCardType import GameCardType
from simpledominion.GameCard import GameCard


class BuyDeck:

    def __init__(self, card_type: GameCardType, card_count: int = 10):
        self._card_type = card_type
        self._card_count = card_count

    @property
    def card_type(self) -> GameCardType:
        return self._card_type

    @property
    def card_count(self):
        return self._card_count

    def is_empty(self) -> bool:
        return self._card_count == 0

    def buy(self) -> Optional[CardInterface]:
        if self._card_count > 0:
            self._card_count -= 1
            return GameCard(self._card_type)
