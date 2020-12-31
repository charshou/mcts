from games import *


def main():
    p1, p2 = MCTS(1, 2 ** 0.5), MCTS(2, 2 ** 0.5)
    curr = p1
    game = TicTacToe(3)
    while True:
        if not isinstance(curr, MCTS):
            game.display()
        curr.play(game)
        if game.checkWin(curr):
            print(curr, "has won.")
            break
        elif not game.availableMoves():
            print("Tie")
            break
        curr = p1 if curr is p2 else p2


if __name__ == "__main__":
    while True:
        main()