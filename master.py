class DungeonMaster :
    #TODO: make this class a singleton 

    def __init__(self):
        self.player1 = Player("black")
        self.player2 = Player("white")
        self.init_pawns = [Pawn("white", 3, 3), Pawn("black", 3, 4), Pawn("black", 4, 3), Pawn("white", 4, 4)] 
        self.board = Board(init_pawns)
        self.who = self.player1 # needs to change after each turn
        self.gameover = False

    def ask(self):
        pass
        where = self.board.check()
        # ask the player where to place new pawn 
        new_pawn = Pawn(color= self.who.color, posx, posy)
        self.board.place(pawn)
    

    def gameover(self):
        # if condition de victoire -->  self.board 
        #   self.gameover = True
