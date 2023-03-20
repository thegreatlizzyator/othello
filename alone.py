import pyfiglet

from board import Board
from player import Player
from pawn import Pawn
import time
import random

class LonelyMaster :
    #TODO: make this class a singleton 

    def __init__(self):
        self.player1 = Player("black", "active", "Player 1")
        self.player2 = Player("white", "inactive", "Gollum")
        
        self.board = Board()
        self.board.cells[3,3].status = 'white'
        self.board.cells[4,4].status = 'white'
        self.board.cells[3,4].status = 'black'
        self.board.cells[4,3].status = 'black' 
        self.li_playable = self.board.coord_playable('black')
        for coord in self.li_playable:
            x = coord[0]
            y = coord[1]
            self.board.cells[x,y].status = 'playable'

    def ask(self):
        print("\n"+ ">"*29 + "     BLACK     " +"<"*26 + "\n")
        print(self.board) 

        
        stupid_count = 0 
        while stupid_count <= 10 :
            if stupid_count == 10 :
                print ("\n"*2," "*5, "RTFM !!!!!!! It seems", self.player1.name, "is too stupid to play this game.","\n"*3)
                time.sleep(5)
                self.gameover()
                raise ValueError (" Please read the manual first and come back when you are less stupid ")
            
            prompt = "your move, " + self.player1.name + ": "
            answer = input(prompt)
            if self.board.is_coord_ok(answer) == False :
                print ("Caution ! Please enter valid coordinates !")
                stupid_count += 1
                continue
            else :
                XY = self.board.translate2XY(answer)
                if XY in self.li_playable :
                    stupid_count = 11
                    return XY
                else :
                    print ("Caution ! Please enter a valid move !")
                    continue  

    def play(self, coord):
        newpawn = Pawn(self.player1.color, coord[0], coord[1])
        self.board.place(newpawn)
        self.li_playable = self.board.coord_playable(self.player2.color)

    def playGollum(self):
        options = self.li_playable
        move = random.choice(options)
        moveA1 = self.board.translate2A1(move[0], move[1])
        print("\nGollum plays: " + moveA1[0] + moveA1[1])


        newpawn = Pawn(self.player2.color, move[0], move[1])
        self.board.place(newpawn)
        self.li_playable = self.board.coord_playable(self.player1.color)
    
    def isover(self):
        allstatus = [self.board.cells[i,j].status for i in range(0,8) for j in range(0,8)]
        nbpl = allstatus.count("playable")
        if nbpl > 0:
            ret = False
        else:
            ret = True

        return ret

    def introduction(self):
        ascii_banner = "\n" + "-"*73 + "\n"
        ascii_banner += str(pyfiglet.figlet_format("OTHELLO", font= "starwars"))
        ascii_banner += "-"*73 + "\n"
        ascii_banner += " "*28 + "Alexandre Appolaire" + " "*20 +"\n"
        ascii_banner += " "*29 + "Lizzy Barthelemy" + " "*20 +"\n"
        ascii_banner += " "*32 + "Aline Cisse" + " "*20 +"\n"
        ascii_banner += "-"*73
        print(ascii_banner)
        self.player1.name = input("What is your name?")
        print("Welcome " + self.player1.name + "!\n")

    def gameover(self):

        isdraw = False 

        allstatus = [self.board.cells[i,j].status for i in range(0,8) for j in range(0,8)]
        nbW = allstatus.count("white")
        nbB = allstatus.count("black")

        if nbB > nbW :
            self.player1.status = "winner"
        elif nbB < nbW :
            self.player2.status = "winner"
        else:
            isdraw = True
        ascii_banner = "\n" + "-"*73 + "\n"
        ascii_banner += str(pyfiglet.figlet_format("     GAME OVER", font= "big"))
        ascii_banner += "-"*73 + "\n"*2

        if isdraw:
            ascii_banner += " "*26 + "  ~~~ IT'S A TIE ~~~ \n\n"
            ascii_banner += " "*19 + " “A tie game is like kissing your sister.”"
            ascii_banner += "\n" + " "*32 + "[J. C. Humes] \n"
        else:
            ascii_banner += " "*32 + "Final Score: \n"
            ascii_banner += " "*26 + self.player1.name + ": " + str(nbB) + "    |    " + "Gollum: " + str(nbW) +  "\n \n"
            
            if self.player1.status == "winner":
                ascii_banner += " "*28 + "Congratulations " + self.player1.name + " ! \n"
                ascii_banner += "\n" + " "*25 + "~ Gollum is a little bitch ~\n"
            elif self.player2.status == "winner":
                ascii_banner += " "*28 + "Congratulations " + self.player2.name + " ! \n"
                ascii_banner += "\n" + " "*21 + "~ " + self.player1.name +" go back to the Shire, punk! \n"
        
        ascii_banner += "\n"+ " "*27 + "Thank you for playing \n "

        ascii_banner += "\n"+ " "*28 + "Alexandre Appolaire" + " "*20 +"\n"
        ascii_banner += " "*29 + "Lizzy Barthelemy" + " "*20 +"\n"
        ascii_banner += " "*32 + "Aline Cisse" + " "*20 +"\n"

        print(ascii_banner)
