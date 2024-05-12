""" Console to make prints along ongoing game """

from utils import cset

class Console:
    def __init__(self) -> None:
        self.cursor = 0
        self.restingx = 0

    def print(self, s, col = "normal"):
        y = self.cursor % 50
        cset(102, y, str(self.cursor), "purple")
        cset(106, y, s, col) 
        self.cursor += 1
        self.restingx = len(s)
        
