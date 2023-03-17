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
                self.cells[x,y] = Cell(x,y,'empty')
    
    def check(self, Playercolor):
        if Playercolor == "white":
            pass
        else:
            pass
        # return list of coordinates where one can place a pawn  

    def coord_color(self, color):
        '''
        Returns a list of the coordinates of the cells of a certain color (black or white)
        '''
        li_coord = []
        if(color == 'white' or color == 'black'):
            for x in range(0,8):
                for y in range(0,8):
                    if self.cells[x,y].status == color:
                        li_coord.append((x,y))
        else:
            raise NameError('Color can only be white or black !')
        return li_coord
    
    def coord_adjacent(self, color):
        '''
        Returns a list of the coordinates of the cells adjacent to the ones of a certain color (black or white)
        '''
        li_coord = []
        li_color = self.coord_color(color)
        for c in li_color:
            x = c[0]
            y = c[1]
            adjacents = [(x,y-1), (x-1,y), (x,y+1), (x+1,y)]
            for a in adjacents:
                xa = a[0]
                ya = a[1]
                if self.cells[xa,ya].is_empty():
                    li_coord.append(a)

        return li_coord

    def is_sandwich(self):
        #TODO: @Aline propose de faire une fonction qui detecte les sandwich
        pass


    def place(self, pawn):
        pass
        # self.allpawns.append(pawn)

    
    def translate2A1(self,y,x): # translate A1 --> x,y 
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

    def translate2XY(self,y,x): #translate x,y --> A1 ...  
        if y in range (0,len(self.liste_pos_Y)) :
            new_y = self.liste_pos_Y[y]
        else:
            raise ValueError("La position indiquée n'existe pas sur le plateau")
        if x in range (0,len(self.liste_pos_x)):
            new_x = self.liste_pos_x[x]
        else:
            raise ValueError("La position indiquée n'existe pas sur le plateau")
        return (new_y,new_x)
    
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