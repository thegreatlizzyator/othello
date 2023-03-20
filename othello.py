from matplotlib.transforms import BboxBase
from master import DungeonMaster

master = DungeonMaster()
master.introduction()
print(master.isover())
coord = master.ask()
master.play(coord)

#master.ask()


#master.gameover()

