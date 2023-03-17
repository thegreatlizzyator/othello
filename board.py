class Board:

    def __init__(self, listofpawns):
        self.allpawns = listofpawns # TODO: idiotproof check that list contains objects of class pawn 
    
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
        pass #TODO: print the ascii board with the is_sandwinch/check as ? 