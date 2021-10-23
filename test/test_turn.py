from typing import List
from unittest import TestCase

from simpledominion.BuyDeck import BuyDeck, BuyDeckInterface
from simpledominion.CardInterface import CardInterface
from simpledominion.Deck import Deck
from simpledominion.GameCard import GameCard
from simpledominion.GameCardType import GameCardType
from simpledominion.Hand import Hand
from simpledominion.Pile import PlayPile
from simpledominion.Player import Player
from simpledominion.Turn import TurnInterface, Turn
from simpledominion.TurnStatus import TurnStatus


class TestTurn(TestCase):
    def setUp(self) -> None:
        self.status = TurnStatus(actions=1, buys=1, coins=0, cards=5)
        self.turn: TurnInterface = Turn()
        self.set_up_player()

    def set_up_player(self) -> None:
        play_pile = PlayPile()
        discard_pile = PlayPile()
        deck = Deck(discard_pile)
        hand = Hand(deck)
        self.player = Player(play_pile, discard_pile, hand)

    def set_status(self, actions: int = 0, buys: int = 0, cards: int = 0, coins: int = 0):
        self.status.actions = actions
        self.status.buys = buys
        self.status.coins = coins
        self.status.cards = cards

    def assert_status(self, actions: int = 0, buys: int = 0, cards: int = 0, coins: int = 0):
        self.assertEqual(actions, self.status.actions)
        self.assertEqual(buys, self.status.buys)
        self.assertEqual(cards, self.status.cards)
        self.assertEqual(coins, self.status.coins)

    def set_discard_pile(self):
        self.player.discard_pile.get_all()
        cards: List[CardInterface] = []
        for i in range(2):
            cards.append(GameCard(GameCardType(0, 0, 0, 0, 0, 10, True, False, "null", "null")))
        for i in range(3):
            cards.append(GameCard(GameCardType(0, 0, 0, 1, 0, 10, False, True, "null", "null")))
        self.player.discard_pile.put_into(cards)

    def assert_new_turn_true(self, actions: int = 0, buys: int = 0, cards: int = 0, coins: int = 0):
        self.set_status(actions, buys, cards, coins)
        self.set_discard_pile()
        self.assertTrue(self.turn.new_turn(self.status, self.player))
        self.assert_status(actions, buys, 0, coins)

    def test_new_turn(self):
        self.assert_new_turn_true(cards=5)
        self.assertEqual(5, len(self.player.hand.get_all()))
        self.assertFalse(self.turn.new_turn(self.status, self.player))
        self.assertTrue(self.turn.end_play_card_phase())
        self.assertTrue(self.turn.end_turn())
        self.assert_new_turn_true(cards=1)
        self.assertEqual(1, len(self.player.hand.get_all()))

    def assert_play_card(self, idx: int = 0, actions: int = 0, buys: int = 0, cards: int = 0, coins: int = 0,
                         result: bool = False, is_treasure: bool = False, is_action: bool = False):
        self.set_status(actions, buys, cards, coins)
        self.assertEqual(is_action, self.player.hand.is_action_card(idx))
        self.assertEqual(is_treasure, self.player.hand.is_treasure_card(idx))
        self.assertEqual(result, self.turn.play_card(idx))
        if is_action and result:
            self.assert_status(actions - 1, buys, cards, coins)
        elif is_treasure and result:
            self.assert_status(actions, buys, cards, coins + 1)
        else:
            self.assert_status(actions, buys, cards, coins)

    def test_play_card(self):
        self.assert_new_turn_true(cards=5)
        self.assert_play_card(idx=-1)
        self.assert_play_card(idx=5)
        self.assert_play_card(idx=0, actions=1, buys=1, result=True, is_action=True)
        self.assert_play_card(idx=0, actions=0, result=False, is_action=True)
        self.assert_play_card(idx=1, result=True, is_treasure=True)
        self.assert_play_card(idx=0, actions=1, result=False, is_action=True)
        self.assertTrue(self.turn.end_play_card_phase())
        self.assert_play_card(idx=1, result=False, is_treasure=True)

    def assert_buy_card(self, actions: int = 0, buys: int = 0, cards: int = 0, coins: int = 0,
                        b_deck_size: int = 0, result: bool = False):
        self.set_status(actions, buys, cards, coins)
        c_type: GameCardType = GameCardType(0, 0, 0, 0, 0, 2, False, False, "null", "name")
        buy_deck: BuyDeck = BuyDeck(c_type, b_deck_size)
        self.player.discard_pile.get_all()
        self.assertEqual(result, self.turn.buy_card(buy_deck))
        if result:
            self.assert_status(actions, buys - 1, cards, coins - 2)
            self.assertEqual(c_type, self.player.discard_pile.get_all()[0].cardType)
        else:
            self.assert_status(actions, buys, cards, coins)

    def test_buy_card(self):
        self.assert_new_turn_true()
        self.assert_buy_card(buys=1, coins=2, b_deck_size=1, result=False)
        self.assertTrue(self.turn.end_play_card_phase())
        self.assert_buy_card(buys=1, coins=2, b_deck_size=1, result=True)
        self.assert_buy_card(buys=0, coins=2, b_deck_size=1, result=False)
        self.assert_buy_card(buys=1, coins=1, b_deck_size=1, result=False)
        self.assert_buy_card(buys=1, coins=2, b_deck_size=0, result=False)

    def test_end_play_card_phase(self):
        self.assertFalse(self.turn.end_play_card_phase())
        self.assert_new_turn_true(cards=2)
        self.assertTrue(self.turn.end_play_card_phase())
        self.assert_play_card(actions=1, result=False, is_action=True)
        self.assert_buy_card(buys=1, coins=2, b_deck_size=1, result=True)
        self.assertTrue(self.turn.end_play_card_phase())
        self.assertTrue(self.turn.end_turn())
        self.assertFalse(self.turn.end_play_card_phase())

    def test_end_turn(self):
        self.assertFalse(self.turn.end_turn())
        self.assert_new_turn_true()
        self.assertTrue(self.turn.end_turn())
        self.assert_new_turn_true()
        self.assertTrue(self.turn.end_play_card_phase())
        self.assertTrue(self.turn.end_turn())
        self.assert_buy_card(buys=1, coins=2, b_deck_size=1, result=False)
