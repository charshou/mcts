import math
from random import choice


class Player:
    def __init__(self, p):
        assert p == 1 or p == 2
        self.p = p

    def play(self, state):
        avail = state.availableMoves()
        print(avail)
        m = int(input("Choose: "))
        while m < 0 or m >= len(avail):
            m = int(input("Choose: "))
        state.makeMove(avail[m], self)

    def __str__(self):
        return "Player " + str(self.p)


class MCTS(Player):
    def __init__(self, p, c):
        self.c = c
        self.opp = Player(3 - p)
        Player.__init__(self, p)

    def get_move(self, state):
        root = Node(None, state, self.opp)
        for _ in range(50):  # TODO set range param
            # selection
            while len(root.unexplored) == 0 and root.children:
                root = max(
                    root.children,
                    key=lambda x: x.wins / x.visits
                    + self.c
                    * (math.log(root.visits) / x.visits)
                    ** 0.5,  # selects child node using UCT
                )

            # expansion
            if root.unexplored and root.state.checkWin(root.player):
                root = root.addChild(
                    choice(root.unexplored),
                    self if root.player is self.opp else self.opp,
                )

            # simulation
            for _ in range(100):
                # TODO fill in simulation
                pass

            # backpropagation
            while root.parent != None:
                # TODO fill in backp
                pass

    def play(self, state):
        pass


class Node:
    def __init__(self, parent, state, player):
        self.children = []
        self.state = state
        self.wins = 0
        self.visits = 0
        self.playermoved = player
        self.unexplored = state.availableMoves()

    def addChild(self, move, state, player):
        statec = state.clone()
        statec.makeMove(move, player)
        child = Node(self, statec, player)
        self.children.append(child)
        self.unexplored.remove(move)
        return child

    def update(self, result):  # result is 1, 2, or 0
        if result == self.playermoved.p:
            self.wins += 1
        self.visits += 1