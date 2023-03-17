class Pawn :

    def __init__(self, color, posx, posy):
        self.pawn_color = color
        self.pawn_posx = posx 
        self.pawn_posy = posy

    @property
    def pawn_color(self):
        return self.__pawn_color

    @pawn_color.setter #permet d'éviter qu'un pion puisse être d'une autre couleur que noir ou blanc
    def pawn_color(self,color):
        if color != 'white' and color != 'black' : 
            raise ValueError (" Attention ! Un pion ne peut être que blanc ou noir ! ")
        self.__pawn_color = color

    @property
    def pawn_posx(self):
        return self.__pawn_posx

    @pawn_posx.setter #permet d'éviter qu'un pion puisse placé en dehors du plateau
    def pawn_posx(self,posx):
        if posx < 0 or posx > 7 :
            raise ValueError (" Attention ! Le pion est en dehors du plateau ! ")
        self.__pawn_posx = posx

    @property
    def pawn_posy(self):
        return self.__pawn_posy

    @pawn_posy.setter
    def pawn_posy(self,posy):
        if posy < 0 or posy > 7 :
            raise ValueError (" Attention ! Le pion est en dehors du plateau ! ")
        self.__pawn_posy = posy
    
    def setcolor(self, new):
        #print("changing cell from", self.color, "to", new) #TODO: idiotproof - new must be 'black' or 'white' 
        self.pawn_color = new

    def __repr__(self):
        return f"{self.pawn_color}, posx = {self.pawn_posx}, posy = {self.pawn_posy}"
    
    def __str__(self):
        return f"{self.pawn_color}, posx = {self.pawn_posx}, posy = {self.pawn_posy}"