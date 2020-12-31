class TicTacToe:
    sims = 4000

    def __init__(self, s):
        self.board = [[0] * s for _ in range(s)]
        self.last = [0, 0]
        self.s = s

    def availableMoves(self):
        moves = []
        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                if self.board[x][y] == 0:
                    moves.append([x, y])
        return moves

    def checkWin(self, player):
        def checker(up, down, x, y):
            def check(x, y):
                if x < 0 or y < 0 or x >= self.s or y >= self.s:
                    return 0
                elif self.board[x][y] != player.p:
                    return 0
                else:
                    return 1 + check(x + up, y + down)

            return check(x, y)

        checks = [
            checker(1, 1, self.last[0], self.last[1])
            + checker(-1, -1, self.last[0], self.last[1])
            - 1,  # diag1
            checker(-1, 1, self.last[0], self.last[1])
            + checker(1, -1, self.last[0], self.last[1])
            - 1,  # diag2
            checker(1, 0, self.last[0], self.last[1])
            + checker(-1, 0, self.last[0], self.last[1])
            - 1,  # up down
            checker(0, 1, self.last[0], self.last[1])
            + checker(0, -1, self.last[0], self.last[1])
            - 1,  # left right
        ]
        if max(checks) != self.s:
            return False
        return True

    def makeMove(self, move, player):
        x, y = move
        self.last = move
        self.board[x][y] = player.p

    def clone(self):
        copy = TicTacToe(self.s)
        copy.board, copy.last = [x[:] for x in self.board], self.last[:]
        return copy

    def display(self):
        for i in reversed(range(self.s)):
            print([self.board[j][i] for j in range(self.s)])
