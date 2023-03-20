import pyfiglet

from board import Board
from player import Player
from pawn import Pawn

class DungeonMaster :
    #TODO: make this class a singleton 

    def __init__(self):
        self.player1 = Player("black", "active", "Player 1")
        self.player2 = Player("white", "inactive", "Player 2")
        # self.init_pawns = [Pawn("white", 3, 3), Pawn("black", 3, 4), Pawn("black", 4, 3), Pawn("white", 4, 4)] 
        self.board = Board()
        self.board.cells[3,3].status = 'white'
        self.board.cells[4,4].status = 'white'
        self.board.cells[3,4].status = 'black'
        self.board.cells[4,3].status = 'black' #TODO : add playabe cells
        self.board.cells[3,2].status = 'playable'
        self.board.cells[2,3].status = 'playable'
        self.board.cells[5,4].status = 'playable'
        self.board.cells[4,5].status = 'playable'


    def ask(self):
        if self.player1.status == "active":
            print("\n"+ ">"*29 + "     Player 1     " +"<"*26 + "\n")
        if self.player2.status == "active":
            print("\n"+ ">"*29 + "     Player 2     " +"<"*26 + "\n")
        # it is player n 's turn 

        print(self.board) 
        
        if self.player1.status == "active":
            prompt = "your move, " + self.player1.name + ": "
        if self.player2.status == "active":
            prompt = "your move, " + self.player2.name + ": "
        
        answer = input(prompt)
        XY = self.board.translate2XY(answer)
        print(XY)
        #TODO: do not allow non playable moves -- add while loop if player is stupide RTFM and rage quit 
        return XY
        
    def play(self, coord):
        print("PLAY")

        if self.player1.status == "active":
            newpawn = Pawn(self.player1.color, coord[0], coord[1])
        elif self.player2.status == "active":
            newpawn = Pawn(self.player2.color, coord[0], coord[1])
        print(newpawn)
        self.board.place(newpawn)


        print(self.board)

        # if sandwich:
        #    print(change color of pawn)
        # 
        #change player --> set status of player to active / inactive
        self.player1.chg_status()
        self.player2.chg_status()

    
    def isover(self):
        allstatus = [self.board.cells[i,j].status for i in range(0,8) for j in range(0,8)]
        nbpl = allstatus.count("playable")
        if nbpl > 0:
            ret = False
        else:
            ret = True

        return ret
       
    def gameover(self):

        isdraw = False 

        allstatus = [self.board.cells[i,j].status for i in range(0,8) for j in range(0,8)]
        
        nbW = allstatus.count("white")
        nbB = allstatus.count("black")
        nbB = 1 ; nbW = 10
        if nbB > nbW :
            self.player1.status = "winner"
        elif nbB < nbW :
            self.player2.status = "winner"
        else:
            isdraw = True
        print(isdraw)
        ascii_banner = "\n" + "-"*73 + "\n"
        ascii_banner += str(pyfiglet.figlet_format("     GAME OVER", font= "big"))
        ascii_banner += "-"*73 + "\n"*2

        if isdraw:
            ascii_banner += " "*26 + "  ~~~ IT'S A TIE ~~~ \n\n"
            ascii_banner += " "*19 + " “A tie game is like kissing your sister.”"
            ascii_banner += "\n" + " "*32 + "[J. C. Humes] \n"
        else:
            if self.player1.status == "winner":
                ascii_banner += " "*25 + "Congratulations " + self.player1.name + " ! \n"
                ascii_banner += "\n" + " "*28 + "~ " + self.player2.name +" you suck ~\n"
            elif self.player2.status == "winner":
                ascii_banner += " "*25 + "Congratulations " + self.player2.name + " ! \n"
                ascii_banner += "\n" + " "*28 + "~ " + self.player1.name +" you suck ~ \n"
        
        ascii_banner += "\n"+ " "*27 + "Thank you for playing \n "

        ascii_banner += "\n"+ " "*28 + "Alexandre Appolaire" + " "*20 +"\n"
        ascii_banner += " "*29 + "Lizzy Barthelemy" + " "*20 +"\n"
        ascii_banner += " "*32 + "Aline Cisse" + " "*20 +"\n"

        print(ascii_banner)
    
    def introduction(self):
        ascii_banner = "\n" + "-"*73 + "\n"
        ascii_banner += str(pyfiglet.figlet_format("OTHELLO", font= "starwars"))
        ascii_banner += "-"*73 + "\n"
        ascii_banner += " "*28 + "Alexandre Appolaire" + " "*20 +"\n"
        ascii_banner += " "*29 + "Lizzy Barthelemy" + " "*20 +"\n"
        ascii_banner += " "*32 + "Aline Cisse" + " "*20 +"\n"
        ascii_banner += "-"*73
        print(ascii_banner)
        self.player1.name = input("What is your name, Player 1?")
        print("Welcome " + self.player1.name + "!\n")
        
        newname = input("What is your name, Player 2?")
        while newname == self.player1.name:
            print("This name is taken. Stop being so basic! \n")
            newname = input("What is your name, Player 2?")
        self.player2.name = newname
        print("Welcome " + self.player2.name + "!\n")
