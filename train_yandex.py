from datetime import datetime as dt
class Player:

    __LVL, __HEALTH = 1 , 100
    __slots__ = ['__level', '__health', '__born']

    def __init__(self):
        self.__level = Player.__LVL
        self.__health = Player.__HEALTH
        self.__born = dt.now()

    @property
    def level(self):
        return self.__level, f'{dt.now() - self.__born}'

    @level.setter
    def level(self, numbers):
        self.__level += Player.__typeTest(numbers)
        if self.__level >= 100: self.__level = 100

    @classmethod
    def set_cls_fields(cls, level=1, health=100):
        cls.__LVL = Player.__typeTest(level)
        cls.HEALTH = Player.__typeTest(health)

    @staticmethod
    def __typeTest(value):
        if isinstance(value, int):
            return value
        else:
            raise TypeError('Must be int')