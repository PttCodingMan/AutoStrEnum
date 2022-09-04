import json
from enum import auto

from AutoStrEnum import AutoStrEnum, AutoJsonEncoder


class Fruit(AutoStrEnum):
    BANANA = auto()
    WATERMELON = auto()
    DURIAN = auto()
    KIWI = auto()


if __name__ == '__main__':
    # We also can use as dict key!
    test_dict = {
        Fruit.BANANA: 6,
        Fruit: {
            Fruit.BANANA: 2,
            Fruit.DURIAN: 10,
            Fruit.WATERMELON: 0,
            'Love': Fruit.KIWI
        }}

    print(test_dict)

    print('json dumps', string_obj := json.dumps(test_dict, indent=4, cls=AutoJsonEncoder))
    print('json loads', json_obj := json.loads(string_obj))

    print(json_obj[Fruit.BANANA])

    test_dict = [
        {
            'name': Fruit.BANANA,
            'price': 10,
            Fruit.BANANA: [
                1, 2, 3
            ],
            Fruit.WATERMELON: [
                Fruit.BANANA,
                Fruit.KIWI
            ]
        },
        {
            Fruit.BANANA: "good"
        }
    ]

    print(test_dict)

    print('json dumps', json.dumps(test_dict, indent=4, cls=AutoJsonEncoder))
