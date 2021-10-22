from random import shuffle

from simpledominion.CardInterface import CardInterface
from typing import List


class PileInterface:
    def put_into(self, cards: List[CardInterface]):
        raise NotImplementedError

    def get_all(self) -> List[CardInterface]:
        raise NotImplementedError



