import numpy as np
from board import Board
from cell import Cell

cell1 = Cell(0,0,'empty')
cell2 = Cell(0,1,'black')

print(cell1.is_empty())
print(cell2.is_empty())

cells = np.array([[1, 2], [3, 4]])
print(cells[0,1])
