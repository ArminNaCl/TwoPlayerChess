from Enums import *

class Square:
    def __init__(self,position,piece=PieceName.NONE):
        self.__position=position
        self.__piece=piece
        self.__color=self.calcColor()

    @property
    def piece(self):
        return self.__piece

    @property
    def position(self):
        return self.__position
    
    def piece_setter(self,value):
        self.__piece=value

    def calcColor(self):
        if sum(self.__position)%2==0:
            return Color.BLACK
        else:
            return Color.WHITE

    def showPosition(self):
        x = chr(self.__position[0]+49)
        y = chr(self.__position[1]+97)
        position=x+y
        return position

    def __str__(self):
        return "squre {} is {} and {}".format(self.showPosition(),self.__color,self.__piece)



