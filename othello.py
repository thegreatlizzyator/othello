from master import DungeonMaster

master = DungeonMaster()
master.introduction()

next = True

while next:
    coord = master.ask()
    master.play(coord)
    next = not master.isover()

master.gameover()

