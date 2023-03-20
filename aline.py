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
print("DEBUG")
board.cells[1,2].status = 'black'
board.cells[1,4].status = 'black'

board.cells[2,2].status = 'white'
board.cells[2,3].status = 'black'
board.cells[2,4].status = 'white'
board.cells[2,5].status = 'white'

board.cells[3,2].status = 'white'
board.cells[3,3].status = 'white'
board.cells[3,4].status = 'black'

board.cells[4,2].status = 'white'
board.cells[4,3].status = 'white'
board.cells[4,4].status = 'white'
board.cells[4,5].status = 'black'

board.cells[5,2].status = 'white'
board.cells[5,3].status = 'white'
board.cells[5,4].status = 'black'
board.cells[5,5].status = 'white'

print(board)

board.coord_playable('white')

print(board)