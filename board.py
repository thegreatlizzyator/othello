
from tkinter import Y
import numpy as np
from cell import Cell
from colorama import Fore

class Board:

    def __init__(self):
        # self.allpawns = listofpawns # TODO: idiotproof check that list contains objects of class pawn
        self.liste_pos_y = ['a','b','c','d','e','f','g','h']
        self.liste_pos_Y = ['A','B','C','D','E','F','G','H']
        self.liste_pos_x = ['1','2','3','4','5','6','7','8'] 
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

                if((a not in li_coord) and (0 <= xa < 8) and (0 <= ya < 8)):
                    if(self.cells[xa,ya].is_empty()):
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
                if(y1 == y2):
                    raise ValueError('Cannot compare the same pawn !')
                else:
                    ori = np.min([y1,y2])

                sum = 0
                for j in range(1,diffy):
                    y = ori + j
                    if(otherc == 'white'):
                        sum += self.cells[x1,y].is_white()
                    elif(otherc == 'black'):
                        sum += self.cells[x1,y].is_black()
                
                sandwich = (sum == diffy-1)
            
            elif(typesand == 'col'):
                if(x1 == x2):
                    raise ValueError('Cannot compare the same pawn !')
                else:
                    ori = np.min([x1,x2])

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
                    fact_x = -1
                    fact_y = -1
                elif(x1 < x2 and y1 > y2):
                    fact_x = -1
                    fact_y = +1
                elif(x1 > x2 and y1 < y2):
                    fact_x = +1
                    fact_y = -1
                elif(x1 > x2 and y1 > y2):
                    fact_x = +1
                    fact_y = +1
                else:
                    raise ValueError('Cannot compare the same pawn !')

                sum = 0
                for i in range(1,diffx):
                    x = x2 + fact_x*i
                    y = y2 + fact_y*i
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
                    x = coord1[0]
                    y = coord1[1]
                    #update status cell to playable
                    self.cells[x,y].status = 'playable'
        
        return playable


    def place(self, pawn):
        x = pawn.pawn_posx
        y = pawn.pawn_posy
        color = pawn.pawn_color

        #place pawn change color cell
        self.cells[x,y].status = color

        #reset playables not played to empty
        for xc in range(0,8):
            for yc in range(0,8):
                if self.cells[xc,yc].is_playable():
                    self.cells[xc,yc].status = 'empty'

        #change color sandwich
        same = self.coord_color(color)
        coord_pawn = (x,y)
        for coord in same:
            if self.is_sandwich(color, coord, coord_pawn):
                x1 = coord[0]
                y1 = coord[1]
                x2 = coord_pawn[0]
                y2 = coord_pawn[1]
                diffx = np.abs(x2 - x1)
                diffy = np.abs(y2 - y1)
                typesand = self.type_sandwich(coord, coord_pawn)

                if(typesand == 'line'):
                    if(y1 == y2):
                        raise ValueError('Cannot compare the same pawn !')
                    else:
                        ori = np.min([y1,y2])

                    for j in range(1,diffy):
                        y = ori + j
                        self.cells[x1,y].status = color
            
                elif(typesand == 'col'):
                    if(x1 == x2):
                        raise ValueError('Cannot compare the same pawn !')
                    else:
                        ori = np.min([x1,x2])

                    for i in range(1,diffx):
                        x = ori + i
                        self.cells[x,y1].status = color
                    
                elif(typesand == 'diag'):
                    if(x1 < x2 and y1 < y2):
                        fact_x = -1
                        fact_y = -1
                    elif(x1 < x2 and y1 > y2):
                        fact_x = -1
                        fact_y = +1
                    elif(x1 > x2 and y1 < y2):
                        fact_x = +1
                        fact_y = -1
                    elif(x1 > x2 and y1 > y2):
                        fact_x = +1
                        fact_y = +1
                    else:
                        raise ValueError('Cannot compare the same pawn !')

                    sum = 0
                    for i in range(1,diffx):
                        x = x2 + fact_x*i
                        y = y2 + fact_y*i
                        self.cells[x,y].status = color    
     
    def translate2XY(self,AA): #translate A1 --> x,y
        YX = list(AA)
        y = YX[0] ; x = YX[1]
        if y in self.liste_pos_y:
            new_y = self.liste_pos_y.index(y)
        elif y in self.liste_pos_Y:
            new_y = self.liste_pos_Y.index(y)
        else:
            return False #La position indiquée n'existe pas sur le plateau
        if x in self.liste_pos_x:
            new_x = self.liste_pos_x.index(x)
        else:
            return False #La position indiquée n'existe pas sur le plateau
        return (new_x,new_y)

    def translate2A1(self,x,y): # translate x,y --> A1  
        if y in range (0,len(self.liste_pos_Y)) :
            new_y = self.liste_pos_Y[y]
        else:
            return False #La position indiquée n'existe pas sur le plateau
        if x in range (0,len(self.liste_pos_x)):
            new_x = self.liste_pos_x[x]
        else:
            return False #La position indiquée n'existe pas sur le plateau
        return (new_y,new_x)

    def is_coord_ok(self,XY):
        if len(XY) != 2 :
            return False
        elif self.translate2XY(XY) == False :
            return False
        return True

    def __str__(self):
        pass 
        sep = " "*18 + "+----" *8 + "+\n" 
        header = " "*15 + "      A    B    C    D    E    F    G    H  \n" + " "*18 + "+----" *8 + "+\n" 
        rows =""

        for i in range(0,8):
            row = " "*15 + str(i+1)+ "  "
            for j in range(0,8):
                if self.cells[i,j].status == "empty":        
                    row += "|    "
                elif self.cells[i,j].status == "black":
                    row += "| X  "
                elif self.cells[i,j].status == "white":
                    row += "| O  "
                else:
                    row += "| ?  "
                    #row += "| " + Fore.RED + "?" + Fore.BLACK +"  "

            rows += row + "| \n" + sep

        ascii_board = header + rows

        return ascii_board