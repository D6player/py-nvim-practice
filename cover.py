""" Covers for the soldiers """

from game_object import GameObject
from utils import cset

class Cover(GameObject):
    def __init__(self, x: int, y: int, char: str):
        super().__init__(x, y)
        self.char = char

    def update(self, game_objects, tiles, console):
        pass

    def draw(self, game_objects, tiles):
        cset(self.x, self.y, self.char, "green")

