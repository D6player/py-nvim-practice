""" Utils """

colors = {
    "red": 31,
    "green": 32,
    "orange": 33,
    "blue": 34,
    "purple": 35,
    "cyan": 36,
    "white": 37,
    "normal": 39,
}

def move(x: int, y: int):
    print(f"\033[{y+1};{x+1}H", end="")

def cset(x:int, y: int, c: str, col: str = "normal"):
    move(x, y)
    print(f"\033[{colors[col]}m", end="")
    print(c, end="")
    print(f"\033[{colors['normal']}m", end="")
