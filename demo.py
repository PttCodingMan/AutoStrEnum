from enum import auto

from AutoStrEnum import AutoStrEnum


class Fruit(AutoStrEnum):
    BANANA = auto()
    WATERMELON = auto()
    DURIAN = auto()


class MagicFruit(AutoStrEnum):
    BANANA = auto()
    WATERMELON = auto()
    DURIAN = auto()


if __name__ == '__main__':
    print(Fruit.BANANA, Fruit.WATERMELON, Fruit.DURIAN)

    print('should be True:', Fruit.BANANA in Fruit)
    print('should be True:', Fruit.BANANA is Fruit.BANANA)
    print('should be True:', Fruit.BANANA == Fruit.BANANA)
    print('should be True:', isinstance(Fruit.BANANA, Fruit))
    print('should be False:', isinstance(Fruit.BANANA, str))
    print('should be False:', isinstance(Fruit.BANANA, MagicFruit))

    # We also can use as dict key!
    test_dict = {
        Fruit.BANANA: 2,
        Fruit.DURIAN: 10,
        Fruit.WATERMELON: 0
    }

    print(test_dict)
