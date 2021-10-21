from simpledominion.Player import Player
from simpledominion.BuyDeck import BuyDeckInterface
from simpledominion.CardInterface import CardInterface
from simpledominion.TurnStatus import TurnStatus
from typing import Optional
from enum import IntEnum


class Phase(IntEnum):
    ACTION = 1
    BUY_TREASURE = 2
    BUY = 3
    CLEAN_UP = 4


class Turn:
    def __init__(self):
        self._status: Optional[TurnStatus] = None
        self._player: Optional[Player] = None
        self._phase: Phase = Phase.CLEAN_UP

    def end_play_card_phase(self) -> bool:
        if self._phase > Phase.BUY:
            return False
        self._phase = Phase.BUY
        return True

    def end_turn(self) -> bool:
        if self._phase == Phase.CLEAN_UP:
            return False
        self._phase = Phase.CLEAN_UP
        self._player.discard_pile.put_into(self._player.play_pile.get_all())
        self._player.discard_pile.put_into(self._player.hand.get_all())
        return True

    def new_turn(self, status: TurnStatus, player: Player) -> bool:
        if self._phase == Phase.CLEAN_UP:
            self._status = status
            self._player = player
            self._phase = Phase.ACTION
            self._player.hand.draw(status.cards)
            status.cards = 0
            return True
        return False

    def play_card(self, idx: int) -> bool:
        if self._phase == Phase.ACTION and self._status.actions > 0 and self._player.hand.is_action_card(idx) \
                or self._phase <= Phase.BUY_TREASURE and self._player.hand.is_treasure_card(idx):
            if self._player.hand.is_treasure_card(idx):
                self._phase = Phase.BUY_TREASURE
            if self._phase == Phase.ACTION:
                self._status.actions -= 1
            card: CardInterface = self._player.hand.play(idx)
            card.evaluate(self._status)
            self._player.play_pile.put_into([card])
            self._player.hand.draw(self._status.cards)
            return True
        return False

    def buy_card(self, buy_deck: BuyDeckInterface) -> bool:
        if self._phase == Phase.BUY \
                and self._status.coins >= buy_deck.card_type.cost \
                and self._status.buys > 0:
            card: CardInterface = buy_deck.buy()
            if card:
                self._status.buys -= 1
                self._status.coins -= buy_deck.card_type.cost
                self._player.discard_pile.put_into([card])
                return True
        return False
