from games import *


def main():
    p1, p2 = Player(1), Player(2)
    curr = p1
    game = TicTacToe(3)
    while True:
        game.display()
        curr.play(game)
        if game.checkWin(curr):
            print(curr, "has won.")
            break
        curr = p1 if curr is p2 else p2


if __name__ == "__main__":
    main()