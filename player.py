class Player:

    def __init__(self, color):
        if color != "black" and color != "white":
            raise ValueError("Players can only be black or white")
        
        else:
            self.__color = color 

    def __set_color(self, color):
        raise AttributeError("Players cannot change sides")

    def __get_color(self):
        return self.__color
    
    color = property(__get_color, __set_color)
