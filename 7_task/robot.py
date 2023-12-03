from abc import ABC, abstractmethod
from math import cos, sin, pi


# Интерфейс IRobot
class IRobot(ABC):

    # режимы работы устройства очистки
    WATER = 1  # полив водой
    SOAP = 2  # полив мыльной пеной
    BRUSH = 3  # чистка щётками

    # Команды:
    # постусловие: робот передвинулся вперед на заданное число метров
    @abstractmethod
    def move(self, value: int) -> None: ...

    # постусловие: робот повернулся на месте на заданный угол в градусах
    @abstractmethod
    def turn(self, value: int) -> None: ...

    # постусловие: выбрано устройство очистки
    @abstractmethod
    def set_state(self, device: str) -> None: ...

    # постусловие: включено устройство очистки
    @abstractmethod
    def start(self) -> None: ...

    # постусловие: выключено устройство очистки
    @abstractmethod
    def stop(self) -> None: ...

    # выполнение набора команд
    @abstractmethod
    def make(self, code) -> None: ...


class CleanerRobot(IRobot):

    def __init__(self, transfer):
        self.x = 0.0
        self.y = 0.0
        self.angle = 0
        self.state = self.WATER
        self.transfer = transfer

    def move(self, dist):
        angle_rads = self.angle * (pi / 180.0)
        self.x += dist * cos(angle_rads)
        self.y += dist * sin(angle_rads)
        self.transfer(('POS(', self.x, ',', self.y, ')'))

    def turn(self, turn_angle):
        self.angle += turn_angle
        self.transfer(('ANGLE', self.angle))

    def set_state(self, new_state):
        if new_state == 'water':
            self.state = self.WATER
        elif new_state == 'soap':
            self.state = self.SOAP
        elif new_state == 'brush':
            self.state = self.BRUSH
        self.transfer(('STATE', self.state))

    def start(self):
        self.transfer(('START WITH', self.state))

    def stop(self):
        self.transfer(('STOP',))

    def make(self, code):
        for command in code:
            cmd = command.split(' ')
            if cmd[0] == 'move':
                self.move(int(cmd[1]))
            elif cmd[0] == 'turn':
                self.turn(int(cmd[1]))
            elif cmd[0] == 'set':
                self.set_state(cmd[1])
            elif cmd[0] == 'start':
                self.start()
            elif cmd[0] == 'stop':
                self.stop()
