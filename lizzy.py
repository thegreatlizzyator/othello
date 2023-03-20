from alone import LonelyMaster

master = LonelyMaster()
master.introduction()
next = True

while next:
    coord = master.ask()
    master.play(coord)
    master.playGollum()
    next = not master.isover()

master.gameover()
