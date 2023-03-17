class Player:

    def __init__(self, color):
        self.__color = color 
                                    #TODO : idiotproof color can only be black or white

    def __set_color(self, color):
        raise AttributeError("Players cannot change sides")

    def __get_color(self):
        return self.__color
    
    color = property(__get_color, __set_color)
