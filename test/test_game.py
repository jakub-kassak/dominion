from typing import List
from unittest import TestCase
from unittest.mock import Mock

from simpledominion.EndGameStrategy import EndGameStrategy
from simpledominion.Game import Game
from simpledominion.Player import Player


class TestGame(TestCase):
    def setUp(self) -> None:
        self.player: Mock = Mock(Player)
        self.buy_decks: List[Mock] = [Mock()]
        self.strategy: Mock = Mock(EndGameStrategy)
        self.factory: Mock = Mock()
        self.turn: Mock = Mock()
        self.factory.new.return_value = self.turn
        self.game: Game = self.create_game()

    def create_game(self) -> Game:
        return Game(self.player, self.buy_decks, self.factory, self.strategy, 0)

    def assert_play_card(self, result: bool = False, return_value: bool = False, n: int = 0,
                         call_check: bool = False) -> None:
        self.turn.play_card.return_value = return_value
        self.assertEqual(result, self.game.play_card(n))
        if call_check:
            self.turn.play_card.assert_called_with(n)

    def test_play_card_and_end_play_card_phase(self) -> None:
        self.game = self.create_game()
        self.assert_play_card(result=False, return_value=False, n=1, call_check=True)
        self.assert_play_card(result=True, return_value=True, n=2, call_check=True)
        self.assertTrue(self.game.end_play_card_phase())
        self.assert_play_card(result=False, return_value=True, n=1)

    def assert_buy_card(self, result: bool = False, return_value: bool = False, n: int = 0) -> None:
        self.turn.buy_card.return_value = return_value
        self.assertEqual(result, self.game.buy_card(n))

    def test_buy_card(self) -> None:
        self.game = self.create_game()
        self.assert_buy_card(result=False, return_value=True)
        self.assertTrue(self.game.end_play_card_phase())
        self.assert_buy_card(result=True, return_value=True)

    def assert_end_turn(self, result=False, is_game_over=False) -> None:
        no: int = self.game.turn_number
        self.strategy.is_game_over.return_value = is_game_over
        self.turn.end_turn.return_value = 0
        self.assertEqual(result, self.game.end_turn())
        if is_game_over:
            self.assertEqual(no, self.game.turn_number)
        else:
            self.assertEqual(no + 1, self.game.turn_number)

    def test_end_turn(self) -> None:
        self.game = self.create_game()
        self.assert_end_turn(result=True, is_game_over=False)
        self.assert_end_turn(result=True, is_game_over=True)
        self.assert_end_turn(result=False, is_game_over=True)
