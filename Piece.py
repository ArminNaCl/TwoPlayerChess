from Board import *
import Pieces

class Piece():
    def __init__(self,color,board):
        self.__color=color
        self.__board=board

    @property
    def color(self):
        return self.__color
    
    @property
    def position(self):
        square=self.square
        if square == None :return None
        return square.position
    
    @property
    def square(self):
        for rows in self.__board.playboard:
            for square in rows:
                if square.piece==self:
                    return square
        return None

    def allMoves(self):
        pass

    def availableMoves(self):
        available_move = list()
        all=self.allMoves()
        for move in all:
            self.move(move)
            if self.check() == False:
                available_move.append(move)
            self.undo()
        return available_move

    def showAvailableMoves(self):
        print("{" ,end=" ")
        for piece in self.availableMoves():
            print(piece.showPosition(),end=" ,")
        print("}")

    def showAllMoves(self):
        print("{" ,end=" ")
        for piece in self.allMoves():
            print(piece.showPosition(),end=" , ")
        print("}")    

    def axisMove(self,axis):
        x,y=self.position
        possible_moves = list()
        for xx,yy in axis:
            xtemp,ytemp = x+xx,y+yy
            while self.isInBoard((xtemp,ytemp)):
                if self.simpleMove(self.__board.playboard[xtemp][ytemp]): 
                    possible_moves.append(self.__board.playboard[xtemp][ytemp])
                elif self.attack(self.__board.playboard[xtemp][ytemp]): 
                    possible_moves.append(self.__board.playboard[xtemp][ytemp])
                    break
                else:
                    break
                xtemp,ytemp = xtemp + xx,ytemp + yy
        return possible_moves

    def oneMove(self,axis):
        x,y=self.position
        possible_moves = list()
        for xx,yy in axis:
            xtemp,ytemp = x+xx,y+yy
            if self.isInBoard((xtemp,ytemp)) and (self.simpleMove(self.__board.playboard[xtemp][ytemp]) or self.attack(self.__board.playboard[xtemp][ytemp])) : 
                possible_moves.append(self.__board.playboard[xtemp][ytemp])
        return possible_moves

    def pawnMove(self):
        x,y = self.position
        possible_moves=list()
        if self.isInBoard((x+self.vec,y+1)) and self.attack(self.__board.playboard[x+self.vec][y+1]): possible_moves.append(self.__board.playboard[x+self.vec][y+1]) 
        if self.isInBoard((x+self.vec,y-1)) and self.attack(self.__board.playboard[x+self.vec][y-1]): possible_moves.append(self.__board.playboard[x+self.vec][y-1])
        if self.isInBoard((x+self.vec,y)) and self.simpleMove(self.__board.playboard[x+self.vec][y]): possible_moves.append(self.__board.playboard[x+self.vec][y])
        return possible_moves


    def isInBoard(self,location):
        x,y = location
        if x >= 0 and x < 8 and y >= 0 and y < 8:
            return True
        return False        
    
    def attack(self,square):
        if self.isInBoard(square.position) and square.piece != None and  square.piece.color != self.color :
            return True
        return False

    def simpleMove(self,square):
        if self.isInBoard(square.position) and (square.piece == None):
            return True
        return False

    def check(self):
        enpieces=[self.__board.playboard[i][j].piece for i in range(8) for j in range(8) if self.__board.playboard[i][j].piece != None and self.__board.playboard[i][j].piece.color != self.color]
        for enpiece in enpieces:
            for move in enpiece.allMoves():
                if move == self.__board.King[self.color].square:
                    return True
        return False

    def move(self,square):
        selfx , selfy =self.position
        squarex,squarey=square.position
        self.__board.push()
        if (type(self) is Pieces.Pawn and squarex in [7,0] ):
            self.__board.playboard[squarex][squarey].piece_setter(Queen(self.color,self.__board))
        else:
            self.__board.playboard[squarex][squarey].piece_setter(self.square.piece)
        self.__board.playboard[selfx][selfy].piece_setter(None)


    def undo(self):
        self.__board.undo()

    def __str__():
        pass
