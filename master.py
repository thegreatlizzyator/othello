import pyfiglet

from board import Board
from player import Player

class DungeonMaster :
    #TODO: make this class a singleton 

    def __init__(self):
        self.player1 = Player("black", "active")
        self.player2 = Player("white", "inactive")
        # self.init_pawns = [Pawn("white", 3, 3), Pawn("black", 3, 4), Pawn("black", 4, 3), Pawn("white", 4, 4)] 
        self.board = Board()
        self.board.cells[3,3].status = 'white'
        self.board.cells[4,4].status = 'white'
        self.board.cells[3,4].status = 'black'
        self.board.cells[4,3].status = 'black'

        # self.who = self.player1 # needs to change after each turn
        # self.gameover = False

    def ask(self):
        if self.player1.status == "active":
            print("Ready player 1" )
        if self.player2.status == "active":
            print("Ready player 2" ) 
        # it is player n 's turn 
        answer = input("your move:")
        print(answer)
        XY = self.board.translate2XY(answer)
        print(XY)
        #if anwser != board.cells == playable : prompt again eventuellement prompter une liste 
        
    def play(self):
        print("PLAY")
        # newpawn = Pawn(anwser[x], anwser(=[y], playercolor)
        # board.place(newpawn)
        # if sandwich:
        #    print(change color of pawn)
        # 
        # where = self.board.check()
        # # ask the player where to place new pawn 
        # new_pawn = Pawn(color= self.who.color, posx, posy)
        # self.board.place(pawn)
        #change player --> set status of player to active / inactive
        self.player1.chg_status()
        self.player2.chg_status()

    def gameover(self):
        pass
        # if condition de victoire -->  self.board 
        #   self.gameover = True
    
    def introduction(self):
        ascii_banner = "\n" + "-"*73 + "\n"
        ascii_banner += str(pyfiglet.figlet_format("OTHELLO", font= "starwars"))
        ascii_banner += "-"*73 + "\n"
        ascii_banner += " "*28 + "Alexandre Appolaire" + " "*20 +"\n"
        ascii_banner += " "*29 + "Lizzy Barthelemy" + " "*20 +"\n"
        ascii_banner += " "*32 + "Aline Cisse" + " "*20 +"\n"
        ascii_banner += "-"*73
        print(ascii_banner)

