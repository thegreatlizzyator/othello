class Pawn :

    def __init__(self, color, posx, posy):
        self.color = color #TODO: idiotproof - color can be 'black' or 'white'
        self.posx = posx #TODO: idiotproof - position cannot be outside the board 
        self.posy = posy

    def setcol(self, new):
        print("changing cell from", self.color, "to", new) #TODO: idiotproof - new must be 'black' or 'white' 
        self.color = new