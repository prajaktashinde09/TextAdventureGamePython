# import tiles
import world
from player import Player

level_1 = False
game_level = 1


def play():
    global game_level
    world.load_tiles(game_level)
    player = Player()
    # These lines load the starting room and display the text
    room = world.tile_exists(player.location_x, player.location_y)
    print(room.intro_text())
    while player.is_alive() and not player.victory:
        room = world.tile_exists(player.location_x, player.location_y)
        room.modify_player(player)
        # Check again since the room could have changed the player's state
        if player.is_alive() and not player.victory:
            print("Choose an action:\n")
            available_actions = room.available_actions()
            for action in available_actions:
                print(action)
            action_input = input('Action: ')
            print("\n \n")
            for action in available_actions:
                if action_input == action.hotkey:
                    player.do_action(action, **action.kwargs)
                    break
    global level_1
    level_1 = player.victory
    if level_1:
        game_level = game_level + 1


if __name__ == "__main__":
    # if not tiles.level_one_passed:
    #     play()
    # else:
    #     print("----------------Level one passed ----------------")
    #     play()
    play()
    if level_1 == True and game_level == 2:
        print("----------------Level {} passed ----------------".format(game_level))
        level_1 = False
        play()
    if level_1 == True and game_level == 3:
        print("----------------Level {} passed ----------------".format(game_level))
        play()


