import json
from enum import auto

from AutoStrEnum import AutoStrEnum, AutoJsonEncoder


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
    print(Fruit, MagicFruit)
    print(Fruit.BANANA, Fruit.WATERMELON, Fruit.DURIAN)

    print('should be True:', Fruit.BANANA in Fruit)
    print('should be True:', Fruit.BANANA is Fruit.BANANA)
    print('should be True:', Fruit.BANANA == Fruit.BANANA)
    print('should be True:', isinstance(Fruit.BANANA, Fruit))
    print('should be False:', isinstance(Fruit.BANANA, str))
    print('should be False:', isinstance(Fruit.BANANA, MagicFruit))
    print('should be False:', isinstance(False, Fruit))

    # We also can use as dict key!
    test_dict = {
        Fruit: {
            Fruit.BANANA: 2,
            Fruit.DURIAN: 10,
            Fruit.WATERMELON: 0,
            'Love': Fruit.KIWI
        }}

    print(test_dict)

    # json dumps is also fine!
    print('json dumps', json.dumps(test_dict, indent=4, cls=AutoJsonEncoder))
