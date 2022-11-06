from overrides import overrides

from yveschiu.experiements.inheritance.entities.abstracts.Role import Role


class Magician(Role):
    def fight(self):
        print('魔法攻擊')

    @overrides
    def __str__(self):
        return f"Magician{super().__str__()}"
