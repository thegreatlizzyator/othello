from matplotlib.transforms import BboxBase
from master import DungeonMaster

master = DungeonMaster()
master.introduction()

coord = master.ask()
master.play(coord)


coord = master.ask()
master.play(coord)

#master.ask()
master.player1.status = "winner"
#master.gameover()

