import numpy as np
from board import Board
from cell import Cell
from master import DungeonMaster

cell1 = Cell(0,0,'empty')
cell2 = Cell(0,1,'black')

print(cell1.is_empty())
print(cell2.is_empty())

cells = np.array([[1, 2], [3, 4]])
print(cells[0,1])

master = DungeonMaster()
board = master.board
print(board.cells[3,3].x,board.cells[3,3].y, board.cells[3,3].status)

####
print("NEW")
board.cells[4,4].status = 'black'
board.cells[4,5].status = 'black'
print(board.cells[3,5].status)

cW = board.coord_color('white')
print("les blancs : ", cW)

cAdj = board.coord_adjacent('black')
print("les adjacents : ", cAdj)

cP = board.coord_playable('white')
print("les playables : ", cP)
print(board.cells[3,5].status)
