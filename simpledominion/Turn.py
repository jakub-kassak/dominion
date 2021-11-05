from simpledominion.Player import Player
from simpledominion.BuyDeck import BuyDeckInterface
from simpledominion.CardInterface import CardInterface
from simpledominion.TurnStatus import TurnStatus
from typing import Optional


class TurnFactory:
    @staticmethod
    def new(status: TurnStatus, player: Player):
        return Turn(status, player)


class TurnInterface:
    def play_card(self, idx: int) -> bool:
        raise NotImplementedError

    def buy_card(self, buy_deck: BuyDeckInterface) -> bool:
        raise NotImplementedError

    def end_turn(self) -> None:
        raise NotImplementedError


class Turn(TurnInterface):
    def __init__(self, status: TurnStatus, player: Player) -> None:
        self._status = status
        self._player = player
        self._player.hand.draw(status.cards)
        self._points: int = 0
        status.cards = 0

    def end_turn(self) -> int:
        self._player.discard_pile.put_into(self._player.play_pile.get_all() + self._player.hand.get_all())
        return self._points

    def play_card(self, idx: int) -> bool:
        if self._status.actions > 0 and self._player.hand.is_action_card(idx) \
                or self._player.hand.is_treasure_card(idx):
            card: Optional[CardInterface] = self._player.hand.play(idx)
            if card:
                if card.cardType.isAction:
                    self._status.actions -= 1
                card.evaluate(self._status)
                self._player.play_pile.put_into([card])
                self._player.hand.draw(self._status.cards)
                return True
        return False

    def buy_card(self, buy_deck: BuyDeckInterface) -> bool:
        if self._status.coins >= buy_deck.card_type.cost and self._status.buys > 0:
            card: Optional[CardInterface] = buy_deck.buy()
            if card:
                self._status.buys -= 1
                self._status.coins -= buy_deck.card_type.cost
                self._points += card.cardType.points
                self._player.discard_pile.put_into([card])
                return True
        return False
