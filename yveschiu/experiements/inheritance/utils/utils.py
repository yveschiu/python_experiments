from yveschiu.experiements.inheritance.entities.abstracts import Role


def dummy_func() -> None:
    print("A dummy function that should not be exported to be used by others")


def say_hi(name: str = None) -> None:
    name = name if name is not None else "there"
    print(f"Hi, {name}")


def draw_fight(role: Role) -> None:
    """
    Just an example function to test type hint

    Print out the attack that a role should perform
    :param role: A subclass of a role
    :return: None
    """
    print(role, end=' ')
    role.fight()
