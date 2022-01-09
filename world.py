import tiles

_world = {}
starting_position = (0, 0)


def load_tiles(game_level):
    print(" game level = {}".format(game_level))
    if game_level == 1:
        print(" condition checked game level = {}".format(game_level))
        with open('Map1.txt', 'r') as f:
            rows = f.readlines()
    if game_level == 2:
        print(" condition checked game level = {}".format(game_level))
        with open('map2.txt', 'r') as f:
            rows = f.readlines()
    if game_level == 3:
        print(" condition checked game level = {}".format(game_level))
        with open('map3.txt', 'r') as f:
            rows = f.readlines()
    else:
        pass
        # with open('map3.txt', 'r') as f:
        #     rows = f.readlines()

    x_max = len(rows[0].split('|'))  # Assumes all rows contain the same number of tabs
    for y in range(len(rows)):
        cols = rows[y].split('|')
        for x in range(x_max):
            tile_name = cols[x].replace('\n', '')  # Windows users may need to replace '\r\n'
            if tile_name == 'StartingRoom':
                global starting_position
                starting_position = (x, y)
            _world[(x, y)] = None if tile_name == '' else getattr(__import__('tiles'), tile_name)(x, y)


def tile_exists(x, y):
    return _world.get((x, y))
