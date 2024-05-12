""" Arena for mean people to fight in """

from interpolated_noise import InterpolatedNoise
from game_object import GameObject
from enum import Enum
from utils import move, cset
from random import randrange
from console import Console

WIDTH: int = 100
HEIGHT: int = 50
DEPTH: int = 8
SIZE: int = 6
THRESHOLD: float = 0.65

class Tile(Enum):
    EMPTY = 1
    WALL = 2

    def to_string(self):
        return "█" if not self.is_empty() else " "

    def is_empty(self) -> bool:
        return self is Tile.EMPTY
        
class Arena():
    def __init__(self, console: Console):
        self.tiles = Arena.__get_random_walls()
        self.game_objects = list()
        self.console = console

    @staticmethod
    def __get_random_walls():
        noise = InterpolatedNoise(WIDTH, HEIGHT, DEPTH, SIZE)
        return [
            [
                Arena.__get_wall(
                    noise.get_interpolated_noise(x, y)
                ) for x in range(WIDTH)
            ] for y in range(HEIGHT)
        ]

    @staticmethod
    def __get_wall(r: float) -> Tile:
        return Tile.WALL if r > THRESHOLD else Tile.EMPTY

    def __print_walls(self):
        for y in range(HEIGHT):
            for x in range(WIDTH):
                cset(x, y, self.tiles[y][x].to_string())

    def add_game_object(self, object: GameObject):
        self.game_objects.append(object)

    def update(self):
        for object in self.game_objects:
            object.update(self.game_objects, self.tiles, self.console)
            if object.dead:
                self.game_objects.remove(object)

    def draw(self):
        move(0, 0)
        self.__print_walls()
        
        for object in self.game_objects:
            object.draw(self.game_objects, self.tiles)
            
def get_empty_position(tiles, x0, y0, x1, y1):
    while True:
        (x, y) = (
            randrange(x0, x1), randrange(y0, y1)
        )

        if tiles[y][x].is_empty():
            break
    
    return (x, y)

