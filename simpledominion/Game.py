from typing import List, Optional

from simpledominion.BuyDeck import BuyDeckInterface
from simpledominion.CardInterface import CardInterface
from simpledominion.EndGameStrategy import EndGameStrategy
from simpledominion.Player import Player
from simpledominion.Turn import Turn, TurnInterface
from simpledominion.TurnStatus import TurnStatus
from enum import IntEnum


class Phase(IntEnum):
    ACTION = 1
    BUY = 2


class GameInterface:
    def play_card(self, idx: int) -> bool:
        raise NotImplementedError

    def end_play_card_phase(self) -> bool:
        raise NotImplementedError

    def buy_card(self, idx: int) -> bool:
        raise NotImplementedError

    def end_turn(self) -> bool:
        raise NotImplementedError

    def evaluate_points(self) -> Optional[int]:
        raise NotImplementedError

    @property
    def turn_number(self) -> int:
        raise NotImplementedError


class Game(GameInterface):
    def __init__(self, player: Player, buy_decks: List[BuyDeckInterface], end_strategy: EndGameStrategy) -> None:
        self._player: Player = player
        self._turn: TurnInterface = Turn(TurnStatus(1, 1, 5, 0), player)
        self._buy_decks: List[BuyDeckInterface] = buy_decks
        self._end_strategy: EndGameStrategy = end_strategy
        self._turn_number: int = 1
        self._is_game_over: bool = False
        self._phase: Phase = Phase.ACTION

    @property
    def turn_number(self) -> int:
        return self._turn_number

    def evaluate_points(self) -> Optional[int]:
        if self._is_game_over:
            self._player.hand.draw(999999999)
            cards: List[CardInterface] = self._player.hand.get_all()
            points: int = 0
            for card in cards:
                points += card.cardType.points
            return points
        return None

    def play_card(self, idx: int) -> bool:
        if not self._is_game_over and self._phase == Phase.ACTION:
            return self._turn.play_card(idx)
        return False

    def end_play_card_phase(self) -> bool:
        if self._phase <= Phase.BUY:
            self._phase = Phase.BUY
            return True
        return False

    def buy_card(self, idx: int) -> bool:
        if self._phase == Phase.BUY:
            return self._turn.buy_card(self._buy_decks[idx])
        return False

    def end_turn(self) -> bool:
        if self._is_game_over:
            return False
        self._phase = Phase.ACTION
        self._turn.end_turn()
        self._turn = Turn(TurnStatus(1, 1, 5, 0), self._player)
        self._is_game_over = self._end_strategy.is_game_over()
        self._turn_number += int(not self._is_game_over)
        return True
