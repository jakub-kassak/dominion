from unittest import TestCase
from simpledominion.DiscardPile import DiscardPile
from simpledominion.GameCardType import GameCardType, GAME_CARD_TYPE_ESTATE, GAME_CARD_TYPE_COPPER
from simpledominion.CardInterface import CardInterface

class FakeCard(CardInterface):
    def __init__(self, cardType: GameCardType):
        self._cardType = cardType
    @property
    def cardType(self):
    	return self._cardType


class TestDiscardPile(TestCase):
    def assertTopIs(self, pile, string):
        self.assertEqual(pile.getTopCard().cardType.name, string)
        
    def assertTopIsNone(self, pile):
        self.assertIsNone(pile.getTopCard())

    def setUp(self):
        self.pile1 = DiscardPile([FakeCard(GAME_CARD_TYPE_ESTATE), FakeCard(GAME_CARD_TYPE_COPPER)])
        self.pile2 = DiscardPile([])
        
    def test_get_top_card(self):
        self.assertTopIs(self.pile1, "Copper")
        self.assertTopIsNone(self.pile2)
        
    def test_add_cards_and_get_size(self):
        self.assertEqual(self.pile2.getSize(), 0)
        self.pile2.addCards([FakeCard(GAME_CARD_TYPE_ESTATE)])
        self.assertEqual(self.pile2.getSize(), 1)
        self.assertTopIs(self.pile2, "Estate")
        self.pile2.addCards([FakeCard(GAME_CARD_TYPE_COPPER)])
        self.assertEqual(self.pile2.getSize(), 2)
        self.assertTopIs(self.pile2, "Copper")
        
        
