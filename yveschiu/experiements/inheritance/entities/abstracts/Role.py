from abc import ABCMeta, abstractmethod


class Role(metaclass=ABCMeta):

    def __init__(self, name: str = 'Default Name', level: int = 1, blood: int = 100) -> None:
        self.name = name
        self.level = level
        self.blood = blood

    @abstractmethod
    def fight(self):
        pass

    def __str__(self):
        return "('{name}', '{level}', '{blood}')".format(**vars(self))

    def __repr__(self):
        return self.__str__()
