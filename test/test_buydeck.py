from typing import Optional
from unittest import TestCase
from simpledominion.BuyDeck import BuyDeck, BuyDeckInterface
from simpledominion.CardInterface import CardInterface
from simpledominion.GameCardType import GAME_CARD_TYPE_COPPER, GAME_CARD_TYPE_FESTIVAL, GameCardType


class TestBuyDeck(TestCase):

    def setUp(self) -> None:
        self.buy_deck1: BuyDeckInterface = BuyDeck(GAME_CARD_TYPE_COPPER)
        self.deck2_size: int = 5
        self.buy_deck2: BuyDeckInterface = BuyDeck(GAME_CARD_TYPE_FESTIVAL, self.deck2_size)

    def test_buy_is_empty(self) -> None:
        self.assertEqual(GAME_CARD_TYPE_COPPER, self.buy_deck1.card_type)
        for i in range(9):
            self.assertEqual(10 - i, self.buy_deck1.size)
            self.assertIsInstance(self.buy_deck1.buy(), CardInterface)
        self.assertFalse(self.buy_deck1.is_empty())
        self.buy_deck1.buy()
        self.assertTrue(self.buy_deck1.is_empty())
        for i in range(self.deck2_size):
            card: Optional[CardInterface] = self.buy_deck2.buy()
            self.assertIsNotNone(card)
            if card:
                c_type: GameCardType = card.cardType
                self.assertEqual(GAME_CARD_TYPE_FESTIVAL, c_type)
        self.assertIsNone(self.buy_deck1.buy())
        self.assertIsNone(self.buy_deck2.buy())
