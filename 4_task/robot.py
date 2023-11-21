'''
Модуль содержит АТД Robot и реализации роботов.
'''
from abc import ABC, abstractmethod
from math import cos, radians, sin
from typing import Tuple

from devices import Device, Water


# АТД Robot
class Robot(ABC):

    # Команды:
    # постусловие: робот передвинулся вперед на заданное число метров
    @abstractmethod
    def move(self, value: int) -> str: ...

    # постусловие: робот повернулся на месте на заданный угол в градусах
    @abstractmethod
    def turn(self, value: int) -> str: ...

    # постусловие: выбрано устройство очистки
    @abstractmethod
    def set(self, device: Device) -> str: ...

    # постусловие: включено устройство очистки
    @abstractmethod
    def start(self) -> str: ...

    # постусловие: выключено устройство очистки
    @abstractmethod
    def stop(self) -> str: ...


class CleanerRobot(Robot):
    '''Робот-дворник'''

    device: Device = Water()
    position: Tuple[float, float] = (0.0, 0.0)
    angle: int = 0

    def move(self, value: int) -> str:
        x = self.position[0]
        y = self.position[1]
        x += round(value * cos(radians(self.angle)), 1)
        y -= round(value * sin(radians(self.angle)), 1)
        self.position = (x, y)
        return f'POS {x}, {y}'

    def turn(self, value: int) -> str:
        self.angle = (self.angle + value) % 360
        return f'ANGLE {self.angle}'

    def set(self, device: Device) -> str:
        self.device = device
        return f'STATE {self.device}'

    def start(self) -> str:
        return f'START WITH {self.device}'

    def stop(self) -> str:
        return 'STOP'
