""" Loot implementation """

from random import choice
from game_object import GameObject
from items import items
from utils import cset

chars = ["▗", "▖", "▘", "▝"]

class Loot(GameObject):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self.loot = choice(items)
        self.char = choice(chars)

    def update(self, game_objects, tiles, console):
        pass

    def draw(self, game_objects, tiles):
        cset(self.x, self.y, self.char, "orange")

    def search(self):
        self.dead = True
        return self.loot

