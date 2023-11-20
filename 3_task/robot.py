from abc import ABC, abstractmethod
from math import cos, radians, sin
from typing import Tuple


# АТД Device
class Device(ABC):
    name: str

    def __str__(self) -> str:
        return self.name


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


if __name__ == '__main__':

    devices = {
        'water': Water(),
        'brush': Brush(),
        'soap': Soap()
    }

    robot = CleanerRobot()

    print("Enter commands: ")
    while True:
        input_command = input("> ")

        command = input_command.split()
        if command[0] == "move":
            print(robot.move(int(command[1])))
        elif command[0] == "turn":
            print(robot.turn(int(command[1])))
        elif command[0] == "set":
            print(robot.set(devices[command[1]]))
        elif command[0] == "start":
            print(robot.start())
        elif command[0] == "stop":
            print(robot.stop())
        else:
            print(f"Command '{input_command}' invalid")
