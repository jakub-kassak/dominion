from unittest import TestCase
from unittest.mock import Mock
from typing import List

from simpledominion.CardInterface import CardInterface
from simpledominion.Hand import Hand


class TestHand(TestCase):
    cards_len: int = 10

    def setUp(self) -> None:
        self.deck = Mock()
        self.hand: Hand = Hand(self.deck)
        self.cards: List[Mock] = []
        for i in range(TestHand.cards_len):
            self.cards.append(Mock())

    def assert_draw_return_value(self, ret_val: List[CardInterface], count: int):
        self.assertEqual(count, len(ret_val))
        for m in self.cards[:count]:
            self.assertEqual(True, m in ret_val)

    def draw(self, start: int = 0, stop: int = cards_len):
        self.deck.draw.return_value = self.cards[start:stop]
        self.hand.draw(start - stop - 1)
        self.deck.draw.called_times = 0

    def test_draw(self):
        self.assertEqual([], self.hand.get_all())
        self.draw(0, 6)
        self.deck.draw.assert_called_once()
        self.assert_draw_return_value(self.hand.cards, 6)
        hand_cards: List[CardInterface] = self.hand.cards
        discarded_cards: List[CardInterface] = self.hand.get_all()
        self.assertEqual(hand_cards, discarded_cards)
        hand_cards.pop()
        self.assertNotEqual(hand_cards, discarded_cards)

    def test_discard(self):
        self.draw(0, 3)
        self.assert_draw_return_value(self.hand.get_all(), 3)
        self.draw(0, 2)
        self.draw(2, 6)
        self.assert_draw_return_value(self.hand.get_all(), 6)

    def test_is_treasure_card(self):
        self.draw()
        self.cards[3].cardType.isTreasure = True
        self.assertEqual(True, self.hand.is_treasure_card(3))
        self.assertEqual(False, self.hand.is_treasure_card(-1))
        self.assertEqual(False, self.hand.is_treasure_card(10))
        self.cards[3].cardType.isTreasure = False
        self.assertEqual(False, self.hand.is_treasure_card(3))

    def test_is_action_card(self):
        self.draw(0, 7)
        self.cards[3].cardType.isAction = True
        self.assertEqual(True, self.hand.is_action_card(3))
        self.cards[3].cardType.isAction = False
        self.assertEqual(False, self.hand.is_action_card(3))

    def test_play(self):
        self.draw()
        self.assertEqual(self.cards[3], self.hand.play(3))
        self.assertNotEqual(self.cards[3], self.hand.play(3))
        self.assertEqual(False, self.cards[3] in self.hand.cards)
        self.assertEqual(None, self.hand.play(-1))
        self.assertEqual(None, self.hand.play(10))
