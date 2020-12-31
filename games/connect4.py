class ConnectFour:
    sims = 4000  # factor for num of simulations

    def __init__(self, w, h):
        self.board = [[0] * h for _ in range(w)]
        self.last = 0
        self.lastc = [0, 0]
        self.w = w
        self.h = h

    def availableMoves(self):
        return [i for i in range(self.w) if self.board[i][self.h - 1] == 0]

    def checkWin(self, player):
        def checker(up, down, x, y):
            def check(x, y):
                if x < 0 or y < 0 or x >= self.w or y >= self.h:
                    return 0
                elif self.board[x][y] != player.p:
                    return 0
                else:
                    return 1 + check(x + up, y + down)

            return check(x, y)

        checks = [
            checker(1, 1, self.lastc[0], self.lastc[1])
            + checker(-1, -1, self.lastc[0], self.lastc[1])
            - 1,  # diag1
            checker(-1, 1, self.lastc[0], self.lastc[1])
            + checker(1, -1, self.lastc[0], self.lastc[1])
            - 1,  # diag2
            checker(1, 0, self.lastc[0], self.lastc[1])
            + checker(-1, 0, self.lastc[0], self.lastc[1])
            - 1,  # up down
            checker(0, 1, self.lastc[0], self.lastc[1])
            + checker(0, -1, self.lastc[0], self.lastc[1])
            - 1,  # left right
        ]
        if max(checks) < 4:
            return False
        return True

    def makeMove(self, move, player):
        place = self.board[move].index(0)
        self.last, self.lastc = move, [move, place]
        self.board[move][place] = player.p

    def clone(self):
        copy = ConnectFour(self.w, self.h)
        copy.board, copy.last, copy.lastc = (
            [x[:] for x in self.board],
            self.last,
            self.lastc[:],
        )
        return copy

    def display(self):
        for i in reversed(range(self.h)):
            print([self.board[j][i] for j in range(self.w)])
