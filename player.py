class Player:

    def __init__(self, color, status, name):
        if color != "black" and color != "white":
            raise ValueError("Players can only be black or white")
        
        else:
            self.__color = color 
        
        self.status = status
        self.name = name

    def __set_color(self, color):
        raise AttributeError("Players cannot change sides")

    def __get_color(self):
        return self.__color
    
    def chg_status(self):
        if self.status == "active":
            self.status = "inactive"
        elif self.status == "inactive":
            self.status = "active"
    
    color = property(__get_color, __set_color)
