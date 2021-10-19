from typing import List, Optional

from simpledominion.BuyDeck import BuyDeck, BuyDeckInterface
from simpledominion.CardInterface import CardInterface
from simpledominion.Deck import Deck
from simpledominion.EndGameStrategy import EndGameStrategy, EndGameStrategyOr, NEmptyDecks
from simpledominion.GameCard import GameCard
from simpledominion.GameCardType import *
from simpledominion.Hand import Hand
from simpledominion.Pile import PlayPile, DiscardPile
from simpledominion.Player import Player
from simpledominion.Turn import Turn, TurnInterface
from simpledominion.TurnStatus import TurnStatus


class GameInterface:
    def play_card(self, idx: int) -> bool:
        raise NotImplementedError

    def end_play_card_phase(self) -> bool:
        raise NotImplementedError

    def buy_card(self, idx: int) -> bool:
        raise NotImplementedError

    def end_turn(self) -> bool:
        raise NotImplementedError

    def evaluate_points(self) -> Optional[int]:
        raise NotImplementedError

    @property
    def turn_number(self):
        raise NotImplementedError


class Game(GameInterface):
    def evaluate_points(self) -> Optional[int]:
        if self._is_game_over:
            self._player.hand.draw(999999999)
            cards: List[CardInterface] = self._player.hand.get_all()
            points: int = 0
            for card in cards:
                points += card.cardType.points
            return points
        return None

    @property
    def turn_number(self):
        return self._turn_number

    @staticmethod
    def create_player() -> Player:
        play_pile = PlayPile()
        discard_pile = DiscardPile()
        discard_pile.put_into([GameCard(GAME_CARD_TYPE_COPPER) for _ in range(7)])
        discard_pile.put_into([GameCard(GAME_CARD_TYPE_ESTATE) for _ in range(3)])
        deck = Deck(discard_pile)
        hand = Hand(deck)
        return Player(play_pile, discard_pile, hand)

    @staticmethod
    def create_decks() -> List[BuyDeck]:
        return [BuyDeck(x, 8) for x in [GAME_CARD_TYPE_PROVINCE, GAME_CARD_TYPE_ESTATE, GAME_CARD_TYPE_DUCHY]] \
               + [BuyDeck(x, 20) for x in [GAME_CARD_TYPE_COPPER, GAME_CARD_TYPE_SILVER, GAME_CARD_TYPE_GOLD]] \
               + [BuyDeck(x, 10) for x in [GAME_CARD_TYPE_SMITHY, GAME_CARD_TYPE_VILLAGE, GAME_CARD_TYPE_FESTIVAL,
                                           GAME_CARD_TYPE_LABORATORY, GAME_CARD_TYPE_MARKET]]

    def __init__(self):
        self._turn: TurnInterface = Turn()
        self._player: Player = self.create_player()
        self._buy_decks: List[BuyDeckInterface] = self.create_decks()
        self._end_strategy: EndGameStrategy = EndGameStrategyOr(
            NEmptyDecks(self._buy_decks[0:1], 1),
            NEmptyDecks(self._buy_decks[6:], 3)
        )
        self._turn.new_turn(TurnStatus(1, 1, 0, 5), self._player)
        self._turn_number: int = 1
        self._is_game_over: bool = False

    def play_card(self, idx: int) -> bool:
        if self._is_game_over:
            return False
        return self._turn.play_card(idx)

    def end_play_card_phase(self) -> bool:
        if self._is_game_over:
            return False
        return self._turn.end_play_card_phase()

    def buy_card(self, idx: int) -> bool:
        if self._is_game_over:
            return False
        return self._turn.buy_card(self._buy_decks[idx])

    def end_turn(self) -> bool:
        if self._is_game_over:
            return False
        self._turn.end_turn()
        self._is_game_over = self._end_strategy.is_game_over()
        self._turn.new_turn(TurnStatus(1, 1, 0, 5), self._player)
        self._turn_number += int(not self._is_game_over)
        return True
