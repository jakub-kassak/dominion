from typing import List, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Card:
    name: str
    description: str
    cost: int

@dataclass
class GameState:
    handCards: List[Card]
    buyCards: List[Tuple[int, Card]]
    deckSize: int
    discardPileSize: int
    discardPileTop: Optional[Card]
    points: int
    turn: int

class SimpleDominionInterface:
    def playCard(self, handIdx: int) -> Optional[GameState]:
        pass    
    def endPlayCardPhase(self) -> Optional[GameState]:
        pass
    def buyCard(self, buyCardIdx: int) -> Optional[GameState]:
        pass
    def endTurn(self) -> Optional[GameState]:
        pass
