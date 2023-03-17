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
            raise ValueError('Color can only be white or black !')
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
                if self.cells[xa,ya].is_empty() and a not in li_coord:
                    li_coord.append(a)

        return li_coord

    def type_sandwich(self, coord1, coord2):
        x1 = coord1[0]
        y1 = coord1[1]
        x2 = coord2[0]
        y2 = coord2[1]
        diffx = np.abs(x2 - x1)
        diffy = np.abs(y2 - y1)
        if(x2 == x1 and diffy > 1):
            # sandwich line
            typesand = 'line'
        elif(y2 == y1 and diffx > 1):
            # sandwich column
            typesand = 'col'
        elif(diffx == diffy and diffx > 1):
            # sandwich diagonal
            typesand = 'diag'
        else:
            typesand = None
        return typesand 

    def is_aligned4sandwich(self, coord1, coord2):    
        typesand = self.type_sandwich(coord1, coord2)
        if(typesand == None):
            align = False
        elif(typesand == 'line' or typesand == 'col' or typesand == 'diag'):
            align = True
        else:
            raise ValueError('Le type de sandwich est line, col ou diag')
        return align
        
    def is_sandwich(self, color, coord1, coord2):
        if color == 'white':
            otherc = 'black'
        elif color == 'black':
            otherc = 'white' 
        else:
            raise ValueError('Color can only be white or black !')

        x1 = coord1[0]
        y1 = coord1[1]
        x2 = coord2[0]
        y2 = coord2[1]
        diffx = np.abs(x2 - x1)
        diffy = np.abs(y2 - y1)
        typesand = self.type_sandwich(coord1, coord2)

        if not self.is_aligned4sandwich(coord1, coord2):
            sandwich = False
        else:
            if(typesand == 'line'):
                if(y1 < y2):
                    ori = y1 
                elif(y1 > y2):
                    ori = y2
                else:
                    raise ValueError('Cannot compare the same pawn !')

                sum = 0
                for j in range(1,diffy):
                    y = ori + j
                    if(otherc == 'white'):
                        sum += self.cells[x1,y].is_white()
                    elif(otherc == 'black'):
                        sum += self.cells[x1,y].is_black()
                
                sandwich = (sum == diffy-1)
            
            elif(typesand == 'col'):
                if(x1 < x2):
                    ori = x1 
                elif(x1 > x2):
                    ori = x2
                else:
                    raise ValueError('Cannot compare the same pawn !')

                sum = 0
                for i in range(1,diffx):
                    x = ori + i
                    if(otherc == 'white'):
                        sum += self.cells[x,y1].is_white()
                    elif(otherc == 'black'):
                        sum += self.cells[x,y1].is_black()
                
                sandwich = (sum == diffx-1)
                
            elif(typesand == 'diag'):
                if(x1 < x2 and y1 < y2):
                    orix = x1 
                    oriy = y1
                elif(x1 < x2 and y1 > y2):
                    orix = x1 
                    oriy = y2
                elif(x1 > x2 and y1 < y2):
                    orix = x2 
                    oriy = y1
                elif(x1 > x2 and y1 > y2):
                    orix = x2 
                    oriy = y2
                else:
                    raise ValueError('Cannot compare the same pawn !')

                sum = 0
                for i in range(1,diffx):
                    x = orix + i
                    y = oriy + i
                    if(otherc == 'white'):
                        sum += self.cells[x,y].is_white()
                    elif(otherc == 'black'):
                        sum += self.cells[x,y].is_black()
                
                sandwich = (sum == diffx-1)
                
            else:
                raise ValueError('Sandwich can only be line, col or diag')
            
        return sandwich

    def coord_playable(self, color):
        if color == 'white':
            otherc = 'black'
        elif color == 'black':
            otherc = 'white' 
        else:
            raise ValueError('Color can only be white or black !')

        playable = []
        adjacents = self.coord_adjacent(otherc)
        same = self.coord_color(color)

        for coord1 in adjacents:
            for coord2 in same:
                if self.is_sandwich(color, coord1, coord2):
                    playable.append(coord1)
        
        return playable


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