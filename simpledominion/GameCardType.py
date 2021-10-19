from dataclasses import dataclass

@dataclass(frozen=True)
class GameCardType:
    plusActions: int
    plusBuys: int
    plusCards: int
    plusCoins: int
    points: int
    cost: int
    isAction: bool
    name: str
    description: str

GAME_CARD_TYPE_ESTATE: GameCardType = GameCardType(0, 0, 0, 0, 1, 2, False, "Estate", "+1 Point")
GAME_CARD_TYPE_COPPER: GameCardType = GameCardType(0, 0, 0, 1, 0, 0, False, "Copper", "+1 Coin")
GAME_CARD_TYPE_SMITHY: GameCardType = GameCardType(0, 0, 3, 0, 0, 4, True, "Smithy", "+3 Cards")
GAME_CARD_TYPE_VILLAGE: GameCardType = GameCardType(2, 0, 1, 0, 0, 3, True, "Village", "+2 Actions; +1 Card")
GAME_CARD_TYPE_FESTIVAL: GameCardType = GameCardType(2, 1, 0, 2, 0, 5, True, "Festival", "+2 Actions; +1 Buy; +2 Coins")
GAME_CARD_TYPE_LABORATORY: GameCardType = GameCardType(1, 0, 2, 0, 0, 5, True, "Laboratory", "+1 Action; +2 Cards")
GAME_CARD_TYPE_MARKET: GameCardType = GameCardType(1, 1, 1, 1, 0, 5, True, "Market", "+1 Action; +1 Buy; +1 Card; +1 Coin")
