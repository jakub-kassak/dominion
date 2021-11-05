from typing import Optional
from simpledominion.CardInterface import CardInterface
from simpledominion.GameCardType import GameCardType
from simpledominion.GameCard import GameCard


class BuyDeckInterface:
    def buy(self) -> Optional[CardInterface]:
        raise NotImplementedError

    def is_empty(self) -> bool:
        raise NotImplementedError

    @property
    def card_type(self) -> GameCardType:
        raise NotImplementedError

    @property
    def size(self):
        raise NotImplementedError


class BuyDeck(BuyDeckInterface):

    def __init__(self, card_type: GameCardType, card_count: int = 10):
        self._card_type: GameCardType = card_type
        self._card_count: int = card_count

    @property
    def card_type(self) -> GameCardType:
        return self._card_type

    @property
    def size(self):
        return self._card_count

    def is_empty(self) -> bool:
        return self._card_count == 0

    def buy(self) -> Optional[CardInterface]:
        if self._card_count > 0:
            self._card_count -= 1
            return GameCard(self._card_type)
        return None
