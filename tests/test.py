import platform
from enum import auto

from AutoStrEnum import AutoStrEnum


class Fruit(AutoStrEnum):
    BANANA = auto()
    WATERMELON = auto()
    DURIAN = auto()
    KIWI = auto()


class MagicFruit(AutoStrEnum):
    BANANA = auto()
    WATERMELON = auto()
    DURIAN = auto()


if __name__ == '__main__':
    print(platform.python_version())
    print(Fruit, MagicFruit)
    print(Fruit.BANANA, Fruit.WATERMELON, Fruit.DURIAN)

    print('should be True:', Fruit.BANANA in Fruit)
    print('should be True:', Fruit.BANANA is Fruit.BANANA)
    print('should be True:', Fruit.BANANA == Fruit.BANANA)
    print('should be True:', isinstance(Fruit.BANANA, Fruit))
    print('should be False:', isinstance(Fruit.BANANA, str))
    print('should be False:', isinstance(Fruit.BANANA, MagicFruit))

    fruits = [Fruit.BANANA, Fruit.WATERMELON, Fruit.DURIAN, Fruit.KIWI]

    if Fruit.BANANA in fruits:
        print('Banana is in fruits')

    if 'BANANA' in fruits:
        print('BANANA is in fruits')
