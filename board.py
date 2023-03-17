from tkinter import Y
import numpy as np
from cell import Cell

class Board:



    def __init__(self):
        # self.allpawns = listofpawns # TODO: idiotproof check that list contains objects of class pawn
        self.liste_pos_y = ['a','b','c','d','e','f','g','h']
        self.liste_pos_Y = ['A','B','C','D','E','F','G','H']
        self.liste_pos_x = [1,2,3,4,5,6,7,8] 
        self.cells = np.empty((8,8), dtype=object)
        for x in range(0,8):
            for y in range(0,8):
                self.cells[x][y] = Cell(x,y,'empty')
    
    def check(self, Playercolor):
        if Playercolor == "white":
            pass
        else:
            pass
        # return list of coordinates where one can place a pawn  

    def is_sandwich(self):
        #TODO: @Aline propose de faire une fonction qui detecte les sandwich
        pass


    def place(self, pawn):
        self.allpawns.append(pawn)

    
    def translate2A1(self,y,x):
        if y in self.liste_pos_y:
            new_y = self.liste_pos_y.index(y)
        elif y in self.liste_pos_Y:
            new_y = self.liste_pos_Y.index(y)
        else:
            raise ValueError("La position indiquée n'existe pas sur le plateau")
        if x in self.liste_pos_x:
            new_x = self.liste_pos_x.index(x)
        else:
            raise ValueError("La position indiquée n'existe pas sur le plateau")
        return (new_y,new_x)
        pass #TODO translate A1 --> x,y 

    def translate2XY(self):
        pass #TODO translate x,y --> A1 ...  

    
    def __str__(self):
        pass #TODO: print the ascii board with the is_sandwinch/check as ? 