import items, enemies, actions, world, Seals
import player

level_one_passed = False

class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError()

    def modify_player(self, player):
        raise NotImplementedError()

    def adjacent_moves(self):
        """Returns all move actions for adjacent tiles."""
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
        return moves

    def available_actions(self):
        """Returns all of the available actions in this room."""
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())
        moves.append(actions.ViewAllSeals())

        return moves


class StartingRoom(MapTile):
    # override the intro_text method in the superclass
    def intro_text(self):
        return """
        
                                                                         
                              .:=+##-..:-==+++++------:                                   
                         :=+##+-:-%%#*+=---::--=**+===+**+.                               
                     -+%@*=:             :+#########*==-.#%                               
                   .===:              .=+@%%%%%%######%%#*                                
                               :-+*#%%%%%%%@@@%#%#####%%@%-                               
                           :=*%%%%######%%%%%@@@%%%@%@@@@@@#+-                            
                        :+%%%#*++*##**+#%#==#%@@@@@@@@@@#+*#%%%*=.                        
                     .=#%%#*==*%#=-----+###%%%%@@@@@@@@#=--==+#%%%*:                      
                   .+%%#*=-==++*+-::::-###%%%%%%%@@@@@%=-----===+#%%*:                    
                :=*%%%%#%%%*+-::::::...-###%%%%%%%@@%@%::::-----==+#%%*:                  
              :+#%%%#**+=--:::::........+###%%%%%%%#@@#::::::-----==+#%%+                 
               +%%#=-----::::.......    -####%%%%%#%%##=:..::::-----==*%%#.               
              *%%*=----::::......        .:-*%%%%##%#####*=-.::::----==+%%%:              
             *%%*=---::::......         .-*#%%%%%#%%#%%%%%%#*=::::----==+%%%:             
            *%%*=---::::....        .-=+###%%%%%%%@@@@@@@@@%%##+=-::---==+%%%.            
           -%%#=---::::....       -*######%%%%%%%%@@@@@@@@@@@@@@%#*+=---==*@@#            
           #%%=----:::....       +#####%%%%%%%%%%@@@@@@@@@@@@@@@@@@%#+---==%@@:           
          :%%#=---:::....       =####%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@#+--==+@@*           
          +%%+----:::...       .####%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@%#=--==%@%           
          *%%=---:::....       -###%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@%##+--==#@@           
          *%%=---:::....       -##%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@%##+--==#@@.          
          *%%=---:::....       +#%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@%####+-==#@@           
          +%%+---:::....      -##%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#+==%@%           
          :%%#----::....     .##%%%%%@@@@@@@@@@@@@@@@@@@@@%%%#%%%%@@@@@@##=+@@*           
           #%%=---:::....    =#%%%%%@@@@@@@@@@@@@@@@@@@@%%%#**#%%%%%@@@@%#+%@@:           
           -@@%=---:::...    =%%%%%@@@@@@@@@@@@@@@@@@@@%%#**+=:##%%%%@@@%##@@#            
            *@@*---:::.....  =%%%%@@@@@@@@@@@@@@@@@@@@@##**+:..:*#%%%%@@%#@@%.            
             #@@*---::::....:#%%%@@@@@@@@@@@@@@@@@@@@@%**+-.....:+#%%%%%%%@%:             
              #@@#----:::...#%%%@@@@@@@@@@@@@@@@@@@@@%***=.....:::#%%%%@@@%:              
               *@@%=---::::+%%%%@@@@@@@@@@@@@@@@@@@@%#****:..::::-+%%%@@@%:               
                =@@@*----:=%%%%%%%%@@@@@@@@@@@@@@@@####***+:::::--=%%@@@*                 
                 .*@@@*---#%%%%%#*%%%@@@@@@@@@@@@@#%@##****-:-----+@@@#:                  
                   .*@@@##%%%%%%**%%%%@@@@@@@@@@@@@@@###***=---=*%@@#:                    
                     .+@@@@@@%%*+#%%%%@@@@@@@@@@@@@@%###%#**=*%@@@*:                      
                        -*@@@@%#=%%%%%@@@@@@@@@@@@@@@@%##%@@@@@#=                         
                           :+%@@@@@@@@@@@@@@@@@@@@%%%%%@@@@%*-                            
                               :=*#%@@@@@@@@@@@@@@@@@%#*=:.                               
                                     .::--====---::.            
        
░██████╗██╗░░██╗░█████╗░██████╗░░█████╗░░██╗░░░░░░░██╗  ███████╗██╗░██████╗░██╗░░██╗████████╗
██╔════╝██║░░██║██╔══██╗██╔══██╗██╔══██╗░██║░░██╗░░██║  ██╔════╝██║██╔════╝░██║░░██║╚══██╔══╝
╚█████╗░███████║███████║██║░░██║██║░░██║░╚██╗████╗██╔╝  █████╗░░██║██║░░██╗░███████║░░░██║░░░
░╚═══██╗██╔══██║██╔══██║██║░░██║██║░░██║░░████╔═████║░  ██╔══╝░░██║██║░░╚██╗██╔══██║░░░██║░░░
██████╔╝██║░░██║██║░░██║██████╔╝╚█████╔╝░░╚██╔╝░╚██╔╝░  ██║░░░░░██║╚██████╔╝██║░░██║░░░██║░░░
╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░░╚════╝░░░░╚═╝░░░╚═╝░░  ╚═╝░░░░░╚═╝░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░                  
        
    Shadow was formerly a powerful combatant but his arrogance led him to defy the rules established by his ancestors 
    and he opened the Gates of Shadows. Upon doing so, he quickly realized his mistake. But it was too late and 
    Shadow lost his flesh and soul and became a mere silhouette of his former self. Shadow must defeat all the six 
    demons and reclaim their demon seals in order to re-seal the Gates of Shadows. 
    To undo the mistake he has made 
    and to seal the Gates of Shadows, the protagonist, Shadow has to re-take the six demon seals. He wins them as a 
    reward by defeating the Demons in every level. He then proceeds to use these seals to close the Gates. Seals are 
    1. Blue seal - Obtained by defeating Lynx. 
    2. Green Seal -Obtained by defeating Hermit. 
    3. Red Seal -Obtained  by defeating Butcher. 
    4. Purple Seal -Obtained by defeating Wasp. 
    5. Orange Seal- Obtained by defeating Widow. 
    6. Jade Seal- Obtained by defeating Shogun. 

    There are 3 Levels. On each 3 levels shadow will get 2 seals by defeating demons.
    You are on now Level 1 -  you have to defeat Lynx, Hermit and their bodyguards to proceed to next level 2 and level 3.
    
    You find yourself in a cave with a flickering torch on the wall.
    You can make out four paths, each equally as dark and foreboding. 
    
    """

    def modify_player(self, player):
        # Room has no action on player
        pass


class LootRoom(MapTile):
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)

    def add_loot(self, player):
        player.inventory.append(self.item)

    def modify_player(self, player):
        self.add_loot(player)


class CollectGold(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Gold(20))

    def intro_text(self):
        return """
        Your notice something shiny in the corner.
        It's a coins! You pick it up.
        """


class getWeapons(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Kunais())

    def intro_text(self):
        return """
        Your notice something shiny in the corner.
        It's a coins! You pick it up.
        """


class RewardsRoom(MapTile):
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)

    def add_coins(self, player):
        player.inventory.append(self.item)

    def modify_player(self, player):
        self.add_coins(player)


class CollectCoins(RewardsRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Coins(20))

    def intro_text(self):
        return """
        Your notice something shiny in the corner.
        It's a coins! You pick it up.
        """


class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)

    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, the_player.hp))

    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.Flee(tile=self), actions.Attack(enemy=self.enemy)]
        else:
            return self.adjacent_moves()


class EmptyCavePath(MapTile):
    def intro_text(self):
        return """
        Another unremarkable part of the cave. You must forge onwards.
        """

    def modify_player(self, player):
        # Room has no action on player
        pass


class LynxDemon_Kingdom(EnemyRoom):  # Lynx
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Lynx_Demon())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            Lynx is a first demon boss is in front of you!!!
            He is the only enemy who has the Time Bomb enchantment on a weapon !!!
            Defeat him to collect Blue seal !!!
            """
        else:
            # player.collect_Blue_seal(Seals.BlueSeal())
            return """
            The corpse of a dead Lynx rots on the ground.
            You have collected Blue Seal !!!
            You can proceed to defeat second demon called Hermit and collect  green seal !!!!. 
            """


class Hermits_Cage(EnemyRoom):  # Lynx
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Hermit_Demon())

    def intro_text(self):
        if self.enemy.is_alive():
            return """Hermit is a second demon boss is in front of you. Hermit is an elderly and wise teacher who is 
            feared for his devastating, mysterious powers. Defeat him and collect Green Seal from him then you will 
            be able to go next level 2. """
        else:
            player.collect_Blue_seal(Seals.BlueSeal())

            return """
            The corpse of a dead Hermit rots on the ground.
            You won the Green seal !!!!. 
            """


class BrickGate(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Brick())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            You are in front of Brick Bodyguard. Bodyguard armed with Steel Batons.
            """
        else:
            return """
            The corpse of a dead Brick rots on the ground.
            """


class NeedlePath(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Needle())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
             A Bodyguard named 'Needle' armed with Sai jumps down in front of you!
             """
        else:
            return """
             The corpse of a dead Needle is on the ground.
             """


class GhostShell(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Ghost())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A giant Ghost with powerful black magic weapons jumps down from  in front of you!
            """
        else:
            return """
            The Ghost has vanished in the air because of your powerful stroke.
            """


class DandyPlace(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Dandy())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            You are in front of Dandy. A Bodyguard armed with Swords.
            """
        else:
            return """
            The corpse of a dead Dandy is on the ground.
            """


class DragonPark(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Dragon())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            You waking through A dragon Park. A giant Dragon Fire is in front of you !!! 
            """
        else:
            return """
            you  killed giant Dragon. The corpse of a dead Dragon is on the ground.
            """


class Buffalo(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Buffalo())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            Be careful, Angry Buffalo is looking at you. !!
            """
        else:
            return """
             you  killed Buffalo. The corpse of a dead Buffalo is on the ground.
            """


class Mantis(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Ghost())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            You are surrounded by Mantis bodyguard armed with Oriental Sabers.
            """
        else:
            return """
             you  killed Mantis. The corpse of a dead Mantis is on the ground.
            """


class LeaveDemonsFirstlevel(MapTile):
    def intro_text(self):
        if len(player.all_seals) == 2:
            return """
            You see a bright light in the distance...
            ... it grows as you get closer! It's sunlight!
            
            Victory is yours!
            """
        else:
            return """You still need to search seals to go ahead"""

    def modify_player(self, player1):
        if len(player.all_seals) == 2:
            level_one_passed = True
            player1.victory = True
        else:
            player1.victory = False
