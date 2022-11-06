from yveschiu.experiements.inheritance.entities import SwordsMan, Magician
from yveschiu.experiements.inheritance.utils import draw_fight


def test() -> None:
    print('文件測試')
    help(draw_fight)

    print('#' * 50)

    swords_man = SwordsMan(name='John', level=25, blood=800)
    magician = Magician(name='Helene', level=40, blood=600)
    draw_fight(swords_man)
    draw_fight(magician)


if __name__ == '__main__':
    test()
