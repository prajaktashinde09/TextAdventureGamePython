import random
from typing import List, Any

import Seals
import items, world

all_seals = []


def collect_Blue_seal(Seals):
    all_seals.append(Seals)


class Player():
    def __init__(self):
        self.inventory = [items.Gold(15), items.Pillow(), items.Rock(), items.Sword(),
                          items.Coins(20)]  # Inventory on startup
        self.hp = 1000  # Health Points
        self.player_seals = all_seals
        self.location_x, self.location_y = world.starting_position  # (0, 0)
        self.victory = False  # no victory on start up

    def flee(self, tile):
        """Moves the player randomly to an adjacent tile"""
        available_moves = tile.adjacent_moves()
        r = random.randint(0, len(available_moves) - 1)
        self.do_action(available_moves[r])

    # is_alive method
    def is_alive(self):
        return self.hp > 0  # Greater than zero value then you are still alive

    def print_inventory(self):
        for item in self.inventory:
            print(item, '\n')

    def print_allSeals(self):
        if self.player_seals:
            for item in self.player_seals:
                print(item, '\n')
        else:
            print("------------You dont have any seals---------")

    def move(self, dx, dy):
        self.location_x += dx
        self.location_y += dy
        print(world.tile_exists(self.location_x, self.location_y).intro_text())

    def move_north(self):
        self.move(dx=0, dy=-1)

    def move_south(self):
        self.move(dx=0, dy=1)

    def move_east(self):
        self.move(dx=1, dy=0)

    def move_west(self):
        self.move(dx=-1, dy=0)

    def attack(self, enemy):
        best_weapon = None
        max_dmg = 0
        for i in self.inventory:
            if isinstance(i, items.Weapon):
                if i.damage > max_dmg:
                    max_dmg = i.damage
                    best_weapon = i

        print("\n You use {} against {}!".format(best_weapon.name, enemy.name))
        enemy.hp -= best_weapon.damage
        if not enemy.is_alive():
            print("\nYou killed demon {}!".format(enemy.name))
            if enemy.name == "LYNX":
                print("!!!!!!!!You won BLUE Seal !!!!")
                collect_Blue_seal(Seals.BlueSeal())
            if enemy.name == "HERMIT":
                print("!!!!!!!!! You won GREEN Seal !!!!!!")
                print("you can move forword to next level")
                collect_Blue_seal(Seals.GreenSeal())
            else:
                pass
            if enemy.name == "GHOST":
                print("!!!!!!!!! You won RED Seal !!!!!!")
                collect_Blue_seal(Seals.RedSeal())
            else:
                pass
            if enemy.name == "DANDY":
                print("!!!!!!!!! You won Purple Seal !!!!!!")
                print("you can move forword to next level")
                collect_Blue_seal(Seals.PurpleSeal())
            else:
                pass
            if enemy.name == "DRAGON":
                print("!!!!!!!!! You won ORANGE Seal !!!!!!")
                print("you can move forword to next level")
                collect_Blue_seal(Seals.OrangeSeal())
            else:
                pass
            if enemy.name == "BUFFALO":
                print("!!!!!!!!! You won JADE Seal !!!!!!")
                print("you can move forword to next level")
                collect_Blue_seal(Seals.JadeSeal())
            else:
                pass

        else:
            print("{} HP is {}.".format(enemy.name, enemy.hp))

    def do_action(self, action, **kwargs):
        action_method = getattr(self, action.method.__name__)
        if action_method:
            action_method(**kwargs)
