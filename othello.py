from matplotlib.transforms import BboxBase
from master import DungeonMaster

master = DungeonMaster()
master.introduction()
print(master.isover())

next = True

while next:
    coord = master.ask()
    master.play(coord)
    next = not master.isover()
    print(next)

#master.gameover()

