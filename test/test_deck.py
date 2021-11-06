from unittest import TestCase
from unittest.mock import Mock
from simpledominion.Deck import Deck, DeckInterface
from simpledominion.GameCardType import GameCardType, GAME_CARD_TYPE_COPPER, GAME_CARD_TYPE_ESTATE
from simpledominion.CardInterface import CardInterface
from simpledominion.GameCard import GameCard
from typing import List


class TestDeck(TestCase):
    def setUp(self) -> None:
        self.dp: Mock = Mock()
        self.deck: DeckInterface = Deck(self.dp)

    def assert_calls_type_len(self, ret_val: List[CardInterface], card_type: GameCardType, calls: int, count: int) -> None:
        self.assertEqual(count, len(ret_val))
        self.assertEqual(calls, self.dp.get_all.call_count)
        self.dp.get_all.call_count = 0
        if count > 0:
            self.assertEqual(card_type, ret_val[-1].cardType)

    def test_draw(self) -> None:
        self.dp.get_all.return_value = []
        self.assert_calls_type_len(self.deck.draw(5), GAME_CARD_TYPE_ESTATE, 1, 0)
        self.dp.get_all.return_value = [GameCard(GAME_CARD_TYPE_ESTATE)] * 3 + [GameCard(GAME_CARD_TYPE_COPPER)] * 7
        self.assert_calls_type_len(self.deck.draw(1), GAME_CARD_TYPE_ESTATE, 1, 1)
        self.assert_calls_type_len(self.deck.draw(2), GAME_CARD_TYPE_ESTATE, 0, 2)
        self.assert_calls_type_len(self.deck.draw(1), GAME_CARD_TYPE_COPPER, 0, 1)
        self.assert_calls_type_len(self.deck.draw(6), GAME_CARD_TYPE_COPPER, 0, 6)
        self.assert_calls_type_len(self.deck.draw(5), GAME_CARD_TYPE_COPPER, 1, 5)
