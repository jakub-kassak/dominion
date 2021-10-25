from typing import List
from unittest import TestCase
from unittest.mock import Mock
from simpledominion.EndGameStrategy import EndGameStrategy, NEmptyDecks


class TestNEmptyDecks(TestCase):
    def setUp(self) -> None:
        self.decks: List[Mock] = [Mock() for _ in range(10)]
        self.strategy1: EndGameStrategy = NEmptyDecks(self.decks, 3)
        self.strategy2: EndGameStrategy = NEmptyDecks(self.decks[:1], 1)
        self.strategy3: EndGameStrategy = NEmptyDecks([], 1)

    def test_is_game_over(self):
        for m in self.decks:
            m.is_empty.return_value = False
        self.assertFalse(self.strategy1.is_game_over())
        self.assertFalse(self.strategy2.is_game_over())

        self.decks[0].is_empty.return_value = True
        self.assertFalse(self.strategy1.is_game_over())
        self.assertTrue(self.strategy2.is_game_over())

        self.decks[1].is_empty.return_value = True
        self.assertFalse(self.strategy1.is_game_over())

        self.decks[2].is_empty.return_value = True
        self.assertTrue(self.strategy1.is_game_over())

        for i in range(10):
            self.decks.pop()
        self.assertTrue(self.strategy1.is_game_over())
        self.assertFalse(self.strategy3.is_game_over())

