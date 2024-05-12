""" The mean people """

from path_finding import find_shortest_path, distance, eucli_dis
from game_object import GameObject
from loot import Loot
from items import *
from utils import cset

class Soldier(GameObject):
    def __init__(self, x: int, y: int, name: str):
        super().__init__(x, y)
        self.name = name
        self.alerted = False
        self.priorities = self.__get_default_prios()
        self.armor = basic_vest
        self.weapon = pistol
        self.usables = set()
        self.last_action = None
    
    def update(self, game_objects, tiles, console):
        self.__update_priorities(game_objects, tiles)
        
        match self.__get_top_priority(game_objects, tiles):
            case "move":
                self.__move(game_objects, tiles, console)
            case "attack":
                self.__attack(game_objects, tiles, console)
            case "loot":
                self.__loot(game_objects, tiles, console)
            case "cover":
                self.__cover(game_objects, tiles, console)
            case "heal":
                self.__heal(game_objects, tiles, console)

    def draw(self, game_objects, tiles):
        cset(self.x, self.y, "█", "red")
        if self.alerted:
            cset(self.x, self.y-1, "!", "red")
        pass

    def draw_name(self):
        cset(self.x, self.y-1, self.name)

    def __update_priorities(self, game_objects, tiles):
        self.priorities = self.__get_default_prios()
        self.alerted = False
        
        # bolean-fest
        if self.__in_range_of_loot(game_objects):
            self.priorities = {
                "move": 0,
                "attack": 0,
                "loot": 50,
                "cover": 0,
                "heal": 0,
            }

        if self.__in_range_of_enemy(game_objects):
            enemy = self.__find_nearest_enemy(game_objects)
            self.alerted = True
            p = ((self.armor.value() - enemy.armor.value()) +
                (self.weapon.value() - enemy.weapon.value())) * 10
            self.priorities["attack"] += (100 + p)
            self.priorities["cover"] += (100 - p)
            self.priorities["heal"] -= 0
            pass
        pass

    def __get_top_priority(self, game_objects, tiles):
        return max(
            self.priorities.keys(),
            key=(lambda k: self.priorities[k])
        )

    def __move(self, game_objects, tiles, console):
        try:
            (x, y) = self.__find_nearest_loot(game_objects).get_pos()
            going_to = "loot"
        except ValueError:
            (x, y) = self.__find_nearest_enemy(game_objects).get_pos()
            going_to = "enemy"

        if self.last_action != "move":
            self.last_action = "move"
            console.print(f"{self.name} is moving to {going_to}")
        
        (x, y) = find_shortest_path(
            (self.x, self.y),
            (x, y),
            tiles,
        )
        
        self.x = x
        self.y = y
        pass
        
    def __attack(self, game_objects, tiles, console):
        d = eucli_dis(self.get_pos(), self.__find_nearest_enemy(game_objects).get_pos())
        if self.last_action != "attack":
            console.print(f"{self.name}: is attacking, {d}", "red")
        self.last_action = "attack"
        pass
        
    def __loot(self, game_objects, tiles, console):
        item = self.__find_nearest_loot(game_objects).search()
        
        if isinstance(item, Usable):
            self.usables.add(item)

        if isinstance(item, Weapon):
            self.weapon = max(
                self.weapon,
                item,
                key=Weapon.value,
            )

        if isinstance(item, Armor):
            self.armor = max(
                self.armor,
                item,
                key=Armor.value,
            )
        
        console.print(f"{self.name}: Looted {item.name}", col="orange")
        self.last_action = "loot"
        pass
        
    def __cover(self, game_objects, tiles, console):
        self.last_action = "cover"
        pass
        
    def __heal(self, game_objects, tiles, console):
        pass
        
    def __find_nearest_loot(self, game_objects):
        return min(
            filter(
                (lambda obj: isinstance(obj, Loot)),
                game_objects,
            ),
            key=(lambda obj: distance(self.get_pos(), obj.get_pos()))
        )

    def __in_range_of_loot(self, game_objects):
        try:
            loot = self.__find_nearest_loot(game_objects)
        except ValueError:
            return False
        return distance(self.get_pos(), loot.get_pos()) <= 1

    def __find_nearest_enemy(self, game_objects):
        return min(
            filter(
                (lambda obj: isinstance(obj, Soldier) and obj != self),
                game_objects,
            ),
            key=(lambda obj: eucli_dis(self.get_pos(), obj.get_pos()))
        )
 

    def __in_range_of_enemy(self, game_objects):
        enemy = self.__find_nearest_enemy(game_objects)
        return eucli_dis(self.get_pos(), enemy.get_pos()) <= 400

    @staticmethod
    def __get_default_prios():
        return {
            "move": 100,
            "attack": 0,
            "loot": 0,
            "cover": 0,
            "heal": 0,
        }

