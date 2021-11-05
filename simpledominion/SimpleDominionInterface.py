from typing import List, Tuple, Optional
from dataclasses import dataclass

from simpledominion.TurnStatus import TurnStatus


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
    status: TurnStatus
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

    def create_game_state(self) -> GameState:
        pass
