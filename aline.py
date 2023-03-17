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
<<<<<<< HEAD

print (master.board.translate2A1('a',4))
print (master.board.translate2XY(1,9))
=======
print(board.coord_color('black'))

>>>>>>> bff6d7d21b7988d40425b4232a7a6498e685a473
