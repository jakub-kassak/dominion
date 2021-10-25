class GameInterface:
    def play_card(self, idx: int) -> bool:
        raise NotImplementedError

    def end_play_card_phase(self) -> bool:
        raise NotImplementedError

    def buy_card(self, idx: int) -> bool:
        raise NotImplementedError

    def end_turn(self) -> bool:
        raise NotImplementedError

    def evaluate_points(self) -> int:
        raise NotImplementedError

    @property
    def turn_number(self):
        raise NotImplementedError
