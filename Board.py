from Square import *
import Pieces
class Board:
    def __init__(self):
        self.__playboard = list()
        self.__stack = list()
        self.King = {Color.BLACK:None,Color.WHITE:None}
        for i in range(8):
            self.__playboard.append([])
            for j in range(8):
                self.__playboard[i].append(Square((i,j)))   
        self.readyToPlay()      
        self.__stack.append(self.playboard)


    def readyToPlay(self):
        board = [
            [
                Pieces.Rook(Color.WHITE,self),
                Pieces.Knight(Color.WHITE,self),
                Pieces.Bishop(Color.WHITE,self),
                Pieces.King(Color.WHITE,self),
                Pieces.Queen(Color.WHITE,self),
                Pieces.Bishop(Color.WHITE,self),
                Pieces.Knight(Color.WHITE,self),
                Pieces.Rook(Color.WHITE,self),
            ],
            [
                Pieces.Pawn(Color.WHITE,self) for i in range(8)
            ],
            [
                PieceName.NONE for i in range(8)
            ],
            [
                PieceName.NONE for i in range(8)
            ],
            [
                PieceName.NONE for i in range(8)
            ],
            [
                PieceName.NONE for i in range(8)
            ],
            [
                Pieces.Pawn(Color.BLACK,self) for i in range(8)
            ],
            [
                Pieces.Rook(Color.BLACK,self),
                Pieces.Knight(Color.BLACK,self),
                Pieces.Bishop(Color.BLACK,self),
                Pieces.King(Color.BLACK,self),
                Pieces.Queen(Color.BLACK,self),
                Pieces.Bishop(Color.BLACK,self),
                Pieces.Knight(Color.BLACK,self),
                Pieces.Rook(Color.BLACK,self),
            ],
        ]
        for i in range(8):
            for j in range(8):
                self.__playboard[i][j].piece_setter(board[i][j])
        return
  
    @property
    def playboard(self):
        return self.__playboard

    @property
    def stack(self):
        return self.__stack

    def push (self):
        self.__stack.append(self.__playboard)
    
    def undo(self):
        self.__playboard=self.__stack.pop()

    def show(self):
        for i in range(8):
            for j in range(8):
                print(self.__playboard[i][j])
            print("="*30)   
    
    


if __name__ == "__main__":
    pass