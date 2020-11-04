from Board import Board


myBoard = Board()
myBoard.show() 
print(myBoard.playboard[6][3].showPosition())
myBoard.playboard[6][3].piece.showAvailableMoves()