from unittest import TestCase
from unittest.mock import Mock
from simpledominion.GameCard import GameCard
from simpledominion.GameCardType import *


class TestGameCard(TestCase):

    def setUp(self) -> None:
        self.game_card_estate = GameCard(GAME_CARD_TYPE_ESTATE)
        self.game_card_copper = GameCard(GAME_CARD_TYPE_COPPER)
        self.game_card_village = GameCard(GAME_CARD_TYPE_VILLAGE)
        self.game_card_market = GameCard(GAME_CARD_TYPE_MARKET)
        self.turn_status = Mock()
        self.setUp_turn_status()

    def setUp_turn_status(self):
        self.turn_status.actions = 0
        self.turn_status.buys = 0
        self.turn_status.cards = 0
        self.turn_status.coins = 0

    def test_card_type(self):
        self.assertEqual(self.game_card_estate.cardType, GAME_CARD_TYPE_ESTATE)
        self.assertNotEqual(self.game_card_copper.cardType, GAME_CARD_TYPE_ESTATE)

    def assert_turn_status_equal(self, actions: int, buys: int, cards: int, coins: int):
        self.assertEqual(self.turn_status.actions, actions)
        self.assertEqual(self.turn_status.buys, buys)
        self.assertEqual(self.turn_status.cards, cards)
        self.assertEqual(self.turn_status.coins, coins)

    def test_evaluate(self):
        self.assert_turn_status_equal(0, 0, 0, 0)
        self.game_card_estate.evaluate(self.turn_status)
        self.assert_turn_status_equal(0, 0, 0, 0)
        self.game_card_copper.evaluate(self.turn_status)
        self.assert_turn_status_equal(0, 0, 0, 1)
        self.setUp_turn_status()
        self.game_card_village.evaluate(self.turn_status)
        self.assert_turn_status_equal(2, 0, 1, 0)
        self.setUp_turn_status()
        self.game_card_market.evaluate(self.turn_status)
        self.assert_turn_status_equal(1, 1, 1, 1)
