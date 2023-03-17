
from board import Board
from cell import Cell
from master import DungeonMaster

cell1 = Cell(0,0,'empty')
cell2 = Cell(0,1,'black')

#print(cell1.is_empty())
#print(cell2.is_empty())

master = DungeonMaster()
board = master.board
#print(board.cells[3,3].x,board.cells[3,3].y, board.cells[3,3].status)



board.cells[1,1].status = "playable"

print(board)

board.cells[1,5].status = "playable"

print(board)

