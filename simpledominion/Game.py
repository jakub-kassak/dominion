from typing import List, Optional

from simpledominion.BuyDeck import BuyDeckInterface
from simpledominion.CardInterface import CardInterface
from simpledominion.EndGameStrategy import EndGameStrategy
from simpledominion.Player import Player
from simpledominion.Turn import TurnInterface, TurnFactory
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

    @property
    def points(self) -> int:
        raise NotImplementedError

    @property
    def turn_number(self) -> int:
        raise NotImplementedError

    @property
    def buy_decks(self) -> List[BuyDeckInterface]:
        raise NotImplementedError

    @property
    def turn_status(self) -> TurnStatus:
        raise NotImplementedError


class Game(GameInterface):
    def __init__(self, player: Player, buy_decks: List[BuyDeckInterface], turn_factory: TurnFactory,
                 end_strategy: EndGameStrategy, points: int) -> None:
        self._player: Player = player
        self._factory: TurnFactory = turn_factory
        self._turn_status: TurnStatus = TurnStatus(1, 1, 5, 0)
        self._turn: TurnInterface = self._factory.new(self._turn_status, self._player)
        self._buy_decks: List[BuyDeckInterface] = buy_decks
        self._end_strategy: EndGameStrategy = end_strategy
        self._turn_number: int = 1
        self._is_game_over: bool = False
        self._phase: Phase = Phase.ACTION
        self._points: int = points

    @property
    def points(self) -> int:
        return self._points

    @property
    def turn_number(self) -> int:
        return self._turn_number

    @property
    def buy_decks(self) -> List[BuyDeckInterface]:
        return self._buy_decks[:]

    @property
    def turn_status(self) -> TurnStatus:
        return self._turn_status

    def play_card(self, idx: int) -> bool:
        if not self._is_game_over and self._phase == Phase.ACTION:
            return self._turn.play_card(idx)
        return False

    def end_play_card_phase(self) -> bool:
        self._phase = Phase.BUY
        return True

    def buy_card(self, idx: int) -> bool:
        if self._phase == Phase.BUY and 0 <= idx < len(self._buy_decks) and not self._is_game_over:
            return self._turn.buy_card(self._buy_decks[idx])
        return False

    def end_turn(self) -> bool:
        if self._is_game_over:
            return False
        self._phase = Phase.ACTION
        self._points += self._turn.end_turn()
        self._turn_status = TurnStatus(1, 1, 5, 0)
        self._turn = self._factory.new(self._turn_status, self._player)
        self._is_game_over = self._end_strategy.is_game_over()
        self._turn_number += int(not self._is_game_over)
        return True
