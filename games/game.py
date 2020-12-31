# general class definition of game
class Game:
    sims = 0  # factor for num of simulations

    def availableMoves(self):
        # returns list of available moves
        pass

    def checkWin(self, player):
        # return true or false (checks win based off of self.last move)
        pass

    def makeMove(self, move, player):
        # makes move on self.board
        pass

    def clone(self):
        # creates copy of game
        pass

    def display(self):
        # shows self.board
        pass
