from typing import List, Optional, Tuple, Dict

from simpledominion.BuyDeck import BuyDeck, BuyDeckInterface
from simpledominion.Deck import Deck, DeckInterface
from simpledominion.EndGameStrategy import EndGameStrategy, EndGameStrategyOr, NEmptyDecks
from simpledominion.Game import GameInterface, Game
from simpledominion.GameCard import GameCard
from simpledominion.GameCardType import *
from simpledominion.Hand import Hand, HandInterface
from simpledominion.Pile import PlayPile, DiscardPile, PileInterface
from simpledominion.Player import Player
from simpledominion.SimpleDominionInterface import SimpleDominionInterface, GameState, Card
from simpledominion.Turn import TurnFactory
from simpledominion.TurnStatus import TurnStatus


class SimpleDominion(SimpleDominionInterface):
    def create_player(self) -> Player:
        self._discard_pile.put_into([GameCard(GAME_CARD_TYPE_COPPER) for _ in range(7)])
        self._discard_pile.put_into([GameCard(GAME_CARD_TYPE_ESTATE) for _ in range(3)])
        return Player(self._play_pile, self._discard_pile, self._hand)

    @staticmethod
    def create_buy_decks() -> List[BuyDeckInterface]:
        buy_decks: List[BuyDeckInterface] = []
        decks: Dict[GameCardType, int] = {
            GAME_CARD_TYPE_PROVINCE: 8,
            GAME_CARD_TYPE_ESTATE: 8,
            GAME_CARD_TYPE_DUCHY: 8,
            GAME_CARD_TYPE_COPPER: 20,
            GAME_CARD_TYPE_SILVER: 20,
            GAME_CARD_TYPE_GOLD: 20,
            GAME_CARD_TYPE_SMITHY: 20,
            GAME_CARD_TYPE_VILLAGE: 20,
            GAME_CARD_TYPE_FESTIVAL: 20,
            GAME_CARD_TYPE_LABORATORY: 20,
            GAME_CARD_TYPE_MARKET: 20
        }
        for c_type, amount in decks.items():
            buy_decks.append(BuyDeck(c_type, amount))
        return buy_decks

    def __init__(self) -> None:
        self._play_pile: PileInterface = PlayPile()
        self._discard_pile: PileInterface = DiscardPile()
        self._deck: DeckInterface = Deck(self._discard_pile)
        self._hand: HandInterface = Hand(self._deck)
        self._player: Player = self.create_player()
        self.buy_decks: List[BuyDeckInterface] = self.create_buy_decks()
        end_strategy: EndGameStrategy = EndGameStrategyOr(
            NEmptyDecks(self.buy_decks[0:1], 1),
            NEmptyDecks(self.buy_decks[6:], 3)
        )
        self._game: GameInterface = Game(self._player, self.buy_decks, TurnFactory(), end_strategy, 3)

    def create_game_state(self) -> GameState:
        handCards: List[Card] = []
        for c_type in [c.cardType for c in self._hand.cards]:
            handCards.append(Card(c_type.name, c_type.description, c_type.cost))
        buyCards: List[Tuple[int, Card]] = []
        for size, c_type in [(deck.size, deck.card_type) for deck in self.buy_decks]:
            buyCards.append((size, Card(c_type.name, c_type.description, c_type.cost)))
        deckSize: int = self._deck.size
        discardPileSize: int = self._discard_pile.size
        c: Optional[GameCard] = self._discard_pile.top_card
        if c:
            discardPileTop: Optional[Card] = Card(c.cardType.name, c.cardType.description, c.cardType.cost)
        else:
            discardPileTop = None
        points: int = self._game.points
        turn: int = self._game.turn_number
        status: TurnStatus = self._game.turn_status
        return GameState(handCards, buyCards, deckSize, discardPileSize, discardPileTop, points, status, turn)

    def playCard(self, handIdx: int) -> Optional[GameState]:
        if self._game.play_card(handIdx):
            return self.create_game_state()
        return None

    def endPlayCardPhase(self) -> Optional[GameState]:
        if self._game.end_play_card_phase():
            return self.create_game_state()
        return None

    def buyCard(self, buyCardIdx: int) -> Optional[GameState]:
        if self._game.buy_card(buyCardIdx):
            return self.create_game_state()
        return None

    def endTurn(self) -> Optional[GameState]:
        if self._game.end_turn():
            return self.create_game_state()
        return None
