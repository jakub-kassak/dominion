from typing import List
from simpledominion.BuyDeck import BuyDeckInterface


class EndGameStrategy:
    def is_game_over(self) -> bool:
        raise NotImplementedError
