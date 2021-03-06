from simpledominion.Pile import PileInterface
from simpledominion.CardInterface import CardInterface
from typing import List


class DeckInterface:

    def draw(self, count: int) -> List[CardInterface]:
        raise NotImplementedError

    @property
    def size(self) -> int:
        raise NotImplementedError


class Deck(DeckInterface):
    def __init__(self, discardPile: PileInterface):
        self._discardPile: PileInterface = discardPile
        self._cards: List[CardInterface] = []

    @property
    def size(self) -> int:
        return len(self._cards)

    def draw(self, count: int) -> List[CardInterface]:
        if len(self._cards) < count:
            self._cards += self._discardPile.get_all()
        cards: List[CardInterface] = self._cards[:count]
        self._cards = self._cards[count:]
        return cards

