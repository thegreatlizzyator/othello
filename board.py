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

    def is_sandwich(self):
        #TODO: @Aline propose de faire une fonction qui detecte les sandwich
        pass


    def place(self, pawn):
        self.allpawns.append(pawn)

    
    def translate2A1(self):
        pass #TODO translate A1 --> x,y 

    def translate2XY(self):
        pass #TODO translate x,y --> A1 ...  

    
    def __str__(self):
        pass 
        sep = "   " + "+----" *8 + "+\n" 
        header = "      A    B    C    D    E    F    G    H  \n" + "   " + "+----" *8 + "+\n" 
        rows =""

        for i in range(0,8):
            row = str(i+1)+ "  "
            for j in range(0,8):
                #print(board.cells[i,j].status)
                if self.cells[i,j].status == "empty":        
                    row += "|    "
                elif self.cells[i,j].status == "black":
                    row += "| B  "
                elif self.cells[i,j].status == "white":
                    row += "| W  "
                else:
                    row += "| ?  "

            rows += row + "| \n" + sep

        ascii_board = header + rows

        return ascii_board