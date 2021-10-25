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
        count = 0
        for deck in self._decks:
            count += deck.is_empty()
        return count >= self._n

