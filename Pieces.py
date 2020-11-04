from Enums import *
from Piece import Piece
    
class Knight(Piece):
    def allMoves(self):
        axis = [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]
        return self.oneMove(axis)

    def __str__(self):
        return "{} {}".format(self.color,PieceName.KNIGHT)


class Queen(Piece):
    def allMoves(self):
        axis = [(1,1),(-1,1),(1,-1),(-1,-1),(1,0),(0,1),(-1,0),(0,-1)]
        return self.axisMove(axis)
    def __str__(self):
        return "{} {}".format(self.color, PieceName.QUEEN)
     
    
class Bishop(Piece):
    def allMoves(self):
        axis =[(1,1),(-1,1),(1,-1),(-1,-1)]
        return self.axisMove(axis)
    def __str__(self):
        return "{} {}".format(self.color,PieceName.BISHOP)


class Rook(Piece):
    def allMoves(self):
        axis= [(1,0),(0,1),(-1,0),(0,-1)]
        return self.axisMove(axis)

    def __str__(self):
        return "{} {}".format(self.color, PieceName.ROCK)


class King(Piece): 
    def __init__(self,color,board):
        super().__init__(color,board)
        board.King[color]=self

    def allMoves(self):
        axis = [(1,0),(1,1),(1,-1),(-1,0),(-1,1),(-1,-1),(0,-1),(0,1)]
        return self.oneMove(axis)

    def __str__(self):
        return "{} {}".format(self.color,PieceName.KING)


class Pawn(Piece):  
    def __init__(self,color,board):
        super().__init__(color,board)
        if color == Color.WHITE:
            self.vec=+1
        else:
            self.vec=-1

    def allMoves(self):
       return self.pawnMove()
       
     
     
     
    
    def __str__(self):
        return "{} {}".format(self.color,PieceName.PWAN)
