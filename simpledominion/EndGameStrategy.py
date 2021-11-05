from typing import List
from simpledominion.BuyDeck import BuyDeckInterface


class EndGameStrategy:
    def is_game_over(self) -> bool:
        raise NotImplementedError


class NEmptyDecks(EndGameStrategy):
    def __init__(self, decks: List[BuyDeckInterface], n: int):
        self._decks = decks[:]
        self._n = n

    def is_game_over(self) -> bool:
        count: int = 0
        for deck in self._decks:
            count += deck.is_empty()
        return count >= self._n


class EndGameStrategyOr(EndGameStrategy):
    def __init__(self, s1: EndGameStrategy, s2: EndGameStrategy):
        self._s1 = s1
        self._s2 = s2

    def is_game_over(self) -> bool:
        return self._s1.is_game_over() or self._s2.is_game_over()
