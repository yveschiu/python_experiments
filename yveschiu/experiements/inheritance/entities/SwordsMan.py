from overrides import overrides

from yveschiu.experiements.inheritance.entities.abstracts.Role import Role


class SwordsMan(Role):
    def fight(self):
        print('揮劍攻擊')

    @overrides
    def __str__(self):
        return f"SwordMan{super().__str__()}"
