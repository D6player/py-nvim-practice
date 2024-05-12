""" Game object definition """

class GameObject():
    def __init__(self, x, y):
        self.dead = False
        self.x = x
        self.y = y
    
    def update(self, game_objects, tiles, console):
        pass

    def draw(self):
        pass

    def get_pos(self):
        return (self.x, self.y)
