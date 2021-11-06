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


def parse_attributes(command: List[str]) -> List[int]:
    try:
        att: List[int] = [int(s) for s in command[1:]]
        att.sort(reverse=True)
        return att
    except ValueError:
        pass


def handle_state(state: GameState, new_state: Optional[GameState], command: str, attribute: Optional[int] = None):
    if new_state:
        return new_state
    else:
        if attribute is None:
            print("incorrect move: {}".format(command))
        else:
            print("incorrect move: {} {}".format(command, attribute))
        return state


def main():
    domionion: SimpleDominionInterface = SimpleDominion()
    state = domionion.create_game_state()
    while True:
        command = input(">>> ").split()
        if command[0] == "play":
            for val in parse_attributes(command):
                state = handle_state(state, domionion.playCard(val), command[0], val)
        elif command[0] == "buy":
            for val in parse_attributes(command):
                state = handle_state(state, domionion.buyCard(val), command[0], val)
        elif command[0] == "end-play":
            state = handle_state(state, domionion.endPlayCardPhase(), command[0])
        elif command[0] == "end-turn":
            state = handle_state(state, domionion.endTurn(), command[0])
        elif command[0] == "print":
            print_gam_state(state)
        elif command[0] == "quit":
            if input("confirm (yes): ") == "yes":
                break
        else:
            print("incorrect command")


if __name__ == '__main__':
    main()
