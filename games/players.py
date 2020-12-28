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

    def getMove(self, state):
        rootn = Node(None, state.clone(), self.opp)
        for _ in range(2000):  # TODO set range param
            root = rootn

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
            if root.unexplored and not root.state.checkWin(root.playermoved):
                root = root.addChild(
                    choice(root.unexplored),
                    root.state,
                    self if root.playermoved is self.opp else self.opp,
                )

            # simulation
            copyState, curr = root.state.clone(), root.playermoved
            while (
                not copyState.checkWin(curr)
                and not len(copyState.availableMoves()) == 0
            ):
                move, curr = (
                    choice(copyState.availableMoves()),
                    self if root.playermoved is self.opp else self.opp,
                )
                copyState.makeMove(move, curr)
            result = curr.p if copyState.checkWin(curr) else 0

            # backpropagation
            while root != None:
                root.update(result)
                root = root.parent

        selected = max(rootn.children, key=lambda x: x.wins / x.visits)
        return selected.state.last

    def play(self, state):
        state.makeMove(self.getMove(state), self)


class Node:
    def __init__(self, parent, state, player):
        self.children = []
        self.state = state
        self.wins = 0
        self.visits = 0
        self.parent = parent
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
        elif result == 0:
            self.wins += 0.3
        self.visits += 1