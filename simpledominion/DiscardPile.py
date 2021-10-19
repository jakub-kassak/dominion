from simpledominion.CardInterface import CardInterface
from typing import Optional, List
from random import shuffle

class DiscardPile:
    _cards: List[CardInterface]

    def __init__(self, cards: List[CardInterface]):
        self._cards = cards
        
    def getTopCard(self) -> Optional[CardInterface]: 
        return self._cards[-1] if self._cards else None
        
    def addCards(self, cards: List[CardInterface]) -> None:
        self._cards.extend(cards)
        
    def getSize(self) -> int:
        return len(self._cards)
        
    def shuffle(self) -> List[CardInterface]:
        cards: List[CardInterface] = self._cards
        self._cards = []
        shuffle(cards)
        return cards
        
        
