from math import cos, radians, sin
from typing import Tuple

# доступные средства очистки
devices: set = {'water', 'brush', 'soap'}

# текущий режим работы устройства очистки
state: str = 'water'

# текущие позиция и угол (ориентация) робота
position: Tuple[float, float] = (0.0, 0.0)
angle: int = 0


def move(value: int) -> str:
    global position
    x = position[0]
    y = position[1]
    x += round(value * cos(radians(angle)), 1)
    y -= round(value * sin(radians(angle)), 1)
    position = (x, y)
    return f'POS {x}, {y}'


def turn(value: int) -> str:
    global angle
    angle = (angle + value) % 360
    return f'ANGLE {angle}'


def set(device) -> str:
    global state
    if device not in devices:
        raise BaseException(f'Нет такого средства очистки: {device}.')
    state = device
    return f'STATE {state}'


def start() -> str:
    return f'START WITH {state}'


def stop() -> str:
    return 'STOP'


if __name__ == '__main__':

    print("Enter commands: ")
    while True:
        input_command = input("> ")

        command = input_command.split()
        if command[0] == "move":
            print(move(int(command[1])))
        elif command[0] == "turn":
            print(turn(int(command[1])))
        elif command[0] == "set":
            print(set(command[1]))
        elif command[0] == "start":
            print(start())
        elif command[0] == "stop":
            print(stop())
        else:
            print(f"Command '{input_command}' invalid")
