from simpledominion.CardInterface import CardInterface
from simpledominion.Deck import DeckInterface
from typing import List, Optional


class HandInterface:
    def is_treasure_card(self, idx: int) -> bool:
        raise NotImplementedError

    def is_action_card(self, idx: int) -> bool:
        raise NotImplementedError

    def play(self, idx: int) -> Optional[CardInterface]:
        raise NotImplementedError

    def draw(self, count: int):
        raise NotImplementedError

    def get_all(self) -> List[CardInterface]:
        raise NotImplementedError

    @property
    def cards(self) -> List[CardInterface]:
        raise NotImplementedError


class Hand(HandInterface):
    def __init__(self, deck: DeckInterface):
        self._deck = deck
        self._cards: List[CardInterface] = []

    @property
    def cards(self) -> List[CardInterface]:
        return self._cards[:]

    def draw(self, count: int):
        self._cards += self._deck.draw(count)

    def _correct_index(self, idx: int) -> bool:
        if idx < 0 or idx > len(self._cards) - 1:
            return False
        return True

    def is_treasure_card(self, idx: int) -> bool:
        return self._correct_index(idx) and self._cards[idx].cardType.isTreasure

    def is_action_card(self, idx: int) -> bool:
        return self._correct_index(idx) and self._cards[idx].cardType.isAction

    def play(self, idx: int) -> Optional[CardInterface]:
        if self._correct_index(idx):
            return self._cards.pop(idx)
        return None

    def get_all(self) -> List[CardInterface]:
        cards: List[CardInterface] = self._cards
        self._cards = []
        return cards
