from master import DungeonMaster

master = DungeonMaster()
master.introduction()

coord = master.ask()
master.play(coord)
next = not master.isover()

master.gameover()



