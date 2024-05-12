""" Main """

from arena import Arena, get_empty_position
from console import Console
from soldier import Soldier
from random import choice
from cover import Cover
from loot import Loot
from time import sleep
from names import names
from utils import move

MAX_LOOT: int = 10
MAX_COVERS: int = 7

def main():
    console = Console()
    arena = Arena(console)
    
    ## Game init
    # Spawn in some loot
    for _ in range(MAX_LOOT):
        (x, y) = get_empty_position(arena.tiles, 0, 0, 100, 50)
        arena.add_game_object(Loot(x, y))
        
    # Spawn some cover
    for _ in range(MAX_COVERS):
        while True:
            (x, y) = get_empty_position(arena.tiles, 25, 13, 75, 37)
            if (
                arena.tiles[y+1][x].is_empty() and 
                arena.tiles[y+1][x+1].is_empty() and
                arena.tiles[y][x+1].is_empty()
                    ):
                break
        arena.add_game_object(Cover(x, y, "▛"))
        arena.add_game_object(Cover(x+1, y, "▜"))
        arena.add_game_object(Cover(x, y+1, "▙"))
        arena.add_game_object(Cover(x+1, y+1, "▟"))
        
    # Spawn four soldiers in four quadrants
    (x, y) = get_empty_position(arena.tiles, 0, 25, 50, 50)
    arena.add_game_object(Soldier(x, y, f"{choice(names)} {choice(names)}"))
    
    (x, y) = get_empty_position(arena.tiles, 0, 0, 50, 25)
    arena.add_game_object(Soldier(x, y, f"{choice(names)} {choice(names)}"))
    
    (x, y) = get_empty_position(arena.tiles, 50, 0, 100, 25)
    arena.add_game_object(Soldier(x, y, f"{choice(names)} {choice(names)}"))
    
    (x, y) = get_empty_position(arena.tiles, 50, 25, 100, 50)
    arena.add_game_object(Soldier(x, y, f"{choice(names)} {choice(names)}"))

    ## Game start
    # Presentation
    arena.draw()
    for obj in arena.game_objects:
        if isinstance(obj, Soldier):
            obj.draw_name()

    print("", end="", flush=True)
    sleep(4)
    
    # Main loop
    while True:
        arena.draw()
        arena.update()
        move(106 + console.restingx, console.cursor-1)
        print("", end="", flush=True)
        sleep(0.5)

if __name__ == "__main__":
    main()
    
