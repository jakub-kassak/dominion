from random import shuffle

from simpledominion.CardInterface import CardInterface
from typing import List, Optional


class PileInterface:
    def put_into(self, cards: List[CardInterface]):
        raise NotImplementedError

    def get_all(self) -> List[CardInterface]:
        raise NotImplementedError

    @property
    def size(self) -> int:
        raise NotImplementedError

    @property
    def top_card(self):
        raise NotImplementedError


class PlayPile(PileInterface):
    def __init__(self):
        self._cards: List[CardInterface] = []

    @property
    def size(self) -> int:
        return len(self._cards)

    @property
    def top_card(self) -> Optional[CardInterface]:
        if len(self._cards) > 0:
            return self._cards[-1]
        return None

    def put_into(self, cards: List[CardInterface]) -> None:
        self._cards.extend(cards)

    def get_all(self) -> List[CardInterface]:
        cards: List[CardInterface] = self._cards
        self._cards = []
        return cards


class DiscardPile(PlayPile):
    def get_all(self) -> List[CardInterface]:
        cards: List[CardInterface] = self._cards
        self._cards = []
        shuffle(cards)
        return cards
