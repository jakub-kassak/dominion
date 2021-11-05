from typing import Optional, List

from simpledominion.SimpleDominion import SimpleDominion
from simpledominion.SimpleDominionInterface import SimpleDominionInterface, GameState


def print_gam_state(state: GameState):
    print("handCards:")
    for i in range(len(state.handCards)):
        print("\t[{}]\t{}".format(i, state.handCards[i]))
    print("buyCards:")
    for i in range(len(state.buyCards)):
        print("\t[{}]\t{}".format(i, state.buyCards[i]))
    print("deckSize: {}".format(state.deckSize))
    print("discardPileSize: {}".format(state.discardPileSize))
    print("discardPileTop: {}".format(state.discardPileTop))
    print("turnStatus: {}\npoints: {}\nturn: {}".format(state.status, state.points, state.turn))


def main():
    domionion: SimpleDominionInterface = SimpleDominion()
    state: GameState = domionion.create_game_state()
    new_state: Optional[GameState] = None
    while True:
        command = input(">>").split()
        if command[0] == "play":
            idx: List[int] = [int(command[i]) - i + 1 for i in range(1, len(command))]
            for val in idx:
                new_state = domionion.playCard(val)
        elif command[0] == "buy":
            idx: List[int] = [int(command[i]) - i + 1 for i in range(1, len(command))]
            for val in idx:
                new_state = domionion.buyCard(val)
        elif command[0] == "end-play":
            new_state = domionion.endPlayCardPhase()
        elif command[0] == "end-turn":
            new_state = domionion.endTurn()
        elif command[0] == "print":
            print_gam_state(state)
        else:
            print("incorrect command")

        if new_state:
            state = new_state
        else:
            print("incorrect move")


if __name__ == '__main__':
    main()
