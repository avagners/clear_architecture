'''
Модуль содержит АТД Device и реализации девайсов для роботов.
'''
from abc import ABC


# АТД Device
class Device(ABC):
    name: str

    def __str__(self) -> str:
        return self.name


# Устройства очистки:
class Water(Device):
    '''Полив водой'''
    name: str = 'water'


class Soap(Device):
    '''Полив мыльной пеной'''
    name: str = 'soap'


class Brush(Device):
    '''Чистка метлой'''
    name: str = 'brush'
