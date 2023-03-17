class Cell:

    def __init__(self, x, y, status):
        self.x = x 
        self.y = y
        if(status == 'empty' or status == 'black' or status == 'white' or status == 'playable'):
            self.status = status
        else:
            raise NameError('Cell can be only empty, black, white or playable, check your spelling !')

    def is_empty(self):
        if(self.status == 'empty'):
            return True
        else:
            return False

    def is_white(self):
        if(self.status == 'white'):
            return True
        else:
            return False

    def is_black(self):
        if(self.status == 'black'):
            return True
        else:
            return False

    def is_playable(self):
        if(self.status == 'playable'):
            return True
        else:
            return False
