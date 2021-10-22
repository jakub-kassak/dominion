from unittest import TestCase
from typing import List
from simpledominion.Pile import PlayPile
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
        self.pile1 = PlayPile()

    def test_put_into(self):
        self.pile1.put_into([FakeCard(GAME_CARD_TYPE_ESTATE)])
        self.assertEqual(1, len(self.pile1.get_all()))
        self.pile1.put_into([FakeCard(GAME_CARD_TYPE_ESTATE)])
        self.assertEqual(GAME_CARD_TYPE_ESTATE, self.pile1.get_all()[0].cardType)
        cards = [FakeCard(GAME_CARD_TYPE_ESTATE), FakeCard(GAME_CARD_TYPE_COPPER),
                 FakeCard(GAME_CARD_TYPE_FESTIVAL), FakeCard(GAME_CARD_TYPE_MARKET),
                 FakeCard(GAME_CARD_TYPE_SMITHY), FakeCard(GAME_CARD_TYPE_LABORATORY),
                 FakeCard(GAME_CARD_TYPE_VILLAGE), FakeCard(GAME_CARD_TYPE_DUCHY)]
        self.pile1.put_into(cards)
        shuffled_cards: List[CardInterface] = self.pile1.get_all()
        self.assertEqual(len(cards), len(shuffled_cards))
        for i in range(len(cards)):
            self.assertEqual(True, cards[i] in shuffled_cards)
