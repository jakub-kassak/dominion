from simpledominion.DiscardPile import DiscardPile
from simpledominion.CardInterface import CardInterface
from typing import List


class DeckInterface:

    def draw(self, count: int) -> List[CardInterface]:
        raise NotImplementedError



