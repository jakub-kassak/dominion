from dataclasses import dataclass
from simpledominion.Pile import PileInterface
from simpledominion.Hand import HandInterface


@dataclass
class Player:
    play_pile: PileInterface
    discard_pile: PileInterface
    hand: HandInterface
