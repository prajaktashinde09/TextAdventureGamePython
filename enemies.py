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
        super().__init__(name="Lynx", hp=60, damage=20)


class Hermit_Demon(Enemy):
    def __init__(self):
        super().__init__(name="Hermit", hp=120, damage=30)


class Shin(Enemy):
    def __init__(self):
        super().__init__(name="Ogre", hp=30, damage=15)


class Brick(Enemy):
    def __init__(self):
        super().__init__(name="Dog", hp=20, damage=10)


class Needle(Enemy):
    def __init__(self):
        super().__init__(name="Needle", hp=10, damage=15)


class Ghost(Enemy):
    def __init__(self):
        super().__init__(name="Ghost", hp=10, damage=15)


class Dandy(Enemy):
    def __init__(self):
        super().__init__(name="Dandy", hp=10, damage=15)


class Dragon(Enemy):
    def __init__(self):
        super().__init__(name="Dragon", hp=10, damage=15)


class Buffalo(Enemy):
    def __init__(self):
        super().__init__(name="Buffalo", hp=10, damage=15)


class Mantis(Enemy):
    def __init__(self):
        super().__init__(name="Needle", hp=10, damage=15)

