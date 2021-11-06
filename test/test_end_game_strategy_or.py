from unittest import TestCase
from unittest.mock import Mock
from simpledominion.EndGameStrategy import EndGameStrategy, EndGameStrategyOr


class TestNEmptyDecks(TestCase):
    def setUp(self) -> None:
        self.s1: Mock = Mock()
        self.s2: Mock = Mock()
        self.strategy_or: EndGameStrategy = EndGameStrategyOr(self.s1, self.s2)

    def set_mocks(self, over1: bool, over2: bool) -> None:
        self.s1.is_game_over.return_value = over1
        self.s2.is_game_over.return_value = over2

    def test_is_game_over(self) -> None:
        self.set_mocks(False, False)
        self.assertFalse(self.strategy_or.is_game_over())
        self.set_mocks(True, False)
        self.assertTrue(self.strategy_or.is_game_over())
        self.set_mocks(False, True)
        self.assertTrue(self.strategy_or.is_game_over())
        self.set_mocks(True, True)
        self.assertTrue(self.strategy_or.is_game_over())
