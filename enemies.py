class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def is_alive(self):
        return self.hp > 0


# class GiantSpider(Enemy):
#     def __init__(self):
#         super().__init__(name="Lynx", hp=10, damage=2)


class Lynx_Demon(Enemy):
    def __init__(self):
        super().__init__(name="LYNX", hp=20, damage=20)


class Hermit_Demon(Enemy):
    def __init__(self):
        super().__init__(name="HERMIT", hp=20, damage=30)


class Shin(Enemy):
    def __init__(self):
        super().__init__(name="SHIN", hp=30, damage=15)


class Brick(Enemy):
    def __init__(self):
        super().__init__(name="BRICK", hp=20, damage=10)


class Needle(Enemy):
    def __init__(self):
        super().__init__(name="NEEDLE", hp=10, damage=15)


class Ghost(Enemy):
    def __init__(self):
        super().__init__(name="GHOST", hp=10, damage=15)


class Dandy(Enemy):
    def __init__(self):
        super().__init__(name="DANDY", hp=10, damage=15)


class Dragon(Enemy):
    def __init__(self):
        super().__init__(name="DRAGON", hp=10, damage=15)


class Buffalo(Enemy):
    def __init__(self):
        super().__init__(name="BUFFALO", hp=10, damage=15)


class Mantis(Enemy):
    def __init__(self):
        super().__init__(name="MANTIS", hp=10, damage=15)

