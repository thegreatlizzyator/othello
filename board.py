import numpy as np
from cell import Cell

class Board:

    def __init__(self):
        # self.allpawns = listofpawns # TODO: idiotproof check that list contains objects of class pawn 
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

    def coord_color(self, color):
        li_coord = []
        if(color == 'white' or color == 'black'):
            for x in range(0,8):
                for y in range(0,8):
                    if self.cells[x][y].status == color:
                        li_coord.append((x,y))
        else:
            raise NameError('Color can only be white or black !')
        return li_coord
    
    def 


    def is_sandwich(self):
        #TODO: @Aline propose de faire une fonction qui detecte les sandwich
        pass


    def place(self, pawn):
        pass
        # self.allpawns.append(pawn)

    
    def translate2A1(self):
        pass #TODO translate A1 --> x,y 

    def translate2XY(self):
        pass #TODO translate x,y --> A1 ...  

    
    def __str__(self):
        pass #TODO: print the ascii board with the is_sandwinch/check as ? 