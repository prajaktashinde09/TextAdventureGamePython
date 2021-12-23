class Seals():
    # __init__ is the contructor method
    def __init__(self, name, description):
        self.name = name  # attribute of the Item class and any subclasses
        self.description = description  # attribute of the Item class and any subclasses

    # __str__ method is used to print the object
    def __str__(self):
        return "{}\n=====\n{}\n\n".format(self.name, self.description)


class BlueSeal(Seals):
    # __init__ is the contructor method
    def __init__(self):  # attribute of the Gold class
        super().__init__(name="Blue",
                         description="A round Blue seal coloured metal with stamped on the front.")


class GreenSeal(Seals):
    # __init__ is the contructor method
    def __init__(self):  # attribute of the Gold class
        super().__init__(name="Green",
                         description="A round Green seal coloured metal with stamped on the front.")


class RedSeal(Seals):
    # __init__ is the contructor method
    def __init__(self):  # attribute of the Gold class
        super().__init__(name="Red",
                         description="A round Red coloured metal seal with stamped on the front.")


class PurpleSeal(Seals):
    # __init__ is the contructor method
    def __init__(self):  # attribute of the Gold class
        super().__init__(name="Purple",
                         description="A round Purple coloured metal seal with stamped on the front.")


class OrangeSeal(Seals):
    # __init__ is the contructor method
    def __init__(self):  # attribute of the Gold class
        super().__init__(name="Orange",
                         description="A round Orange coloured Metal seal with stamped on the front.")


class JadeSeal(Seals):
    # __init__ is the contructor method
    def __init__(self):  # attribute of the Gold class
        super().__init__(name="Purple",
                         description="A round Jade coloured metal seal with stamped on the front.")
