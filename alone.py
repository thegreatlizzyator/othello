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

