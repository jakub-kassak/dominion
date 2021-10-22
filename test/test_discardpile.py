from typing import List
from unittest import TestCase
from simpledominion.Pile import DiscardPile, PileInterface
from simpledominion.GameCardType import *
from simpledominion.CardInterface import CardInterface


class FakeCard(CardInterface):
    def __init__(self, cardType: GameCardType):
        self._cardType = cardType

    @property
    def cardType(self):
        return self._cardType


class TestDiscardPile(TestCase):

    def setUp(self):
        self.discard_pile: PileInterface = DiscardPile()
        self.discard_pile.put_into([FakeCard(GAME_CARD_TYPE_ESTATE), FakeCard(GAME_CARD_TYPE_COPPER)])

    def test_put_into(self):
        self.discard_pile.put_into([FakeCard(GAME_CARD_TYPE_ESTATE)])
        self.assertEqual(3, len(self.discard_pile.get_all()))
        self.discard_pile.put_into([FakeCard(GAME_CARD_TYPE_ESTATE)])
        self.assertEqual(GAME_CARD_TYPE_ESTATE, self.discard_pile.get_all()[0].cardType)
        cards = [FakeCard(GAME_CARD_TYPE_ESTATE), FakeCard(GAME_CARD_TYPE_COPPER),
                 FakeCard(GAME_CARD_TYPE_FESTIVAL), FakeCard(GAME_CARD_TYPE_MARKET),
                 FakeCard(GAME_CARD_TYPE_SMITHY), FakeCard(GAME_CARD_TYPE_LABORATORY),
                 FakeCard(GAME_CARD_TYPE_VILLAGE), FakeCard(GAME_CARD_TYPE_DUCHY)]
        self.discard_pile.put_into(cards)
        shuffled_cards: List[CardInterface] = self.discard_pile.get_all()
        self.assertEqual(len(cards), len(shuffled_cards))
        self.assertNotEqual(cards, shuffled_cards)
