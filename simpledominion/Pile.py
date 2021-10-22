from random import shuffle

from simpledominion.CardInterface import CardInterface
from typing import List


class PileInterface:
    def put_into(self, cards: List[CardInterface]):
        raise NotImplementedError

    def get_all(self) -> List[CardInterface]:
        raise NotImplementedError


class PlayPile(PileInterface):
    def __init__(self):
        self._cards: List[CardInterface] = []

    def put_into(self, cards: List[CardInterface]) -> None:
        self._cards.extend(cards)

    def get_all(self) -> List[CardInterface]:
        cards: List[CardInterface] = self._cards
        self._cards = []
        return cards



