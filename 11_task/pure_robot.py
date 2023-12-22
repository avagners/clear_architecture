import math
from collections import namedtuple

from pymonad import State, List, curry, unit

RobotState = namedtuple("RobotState", "x y angle state")

# режимы работы устройства очистки
WATER = 1  # полив водой
SOAP = 2  # полив мыльной пеной
BRUSH = 3  # чистка щётками


# взаимодействие с роботом вынесено в отдельную функцию
def transfer_to_cleaner(message):
    print(message)


# перемещение
@curry
def move(dist, state):

    @State
    def compute_state(log: List) -> State:
        angle_rads = state.angle * (math.pi / 180.0)
        new_state = RobotState(
            state.x + dist * math.cos(angle_rads),
            state.y + dist * math.sin(angle_rads),
            state.angle,
            state.state
        )
        message = f'POS({new_state.x}, {new_state.y})'
        log += List(message)
        return (new_state, log)

    return compute_state


# поворот
@curry
def turn(turn_angle, state):

    @State
    def compute_state(log: List) -> State:
        new_state = RobotState(
            state.x,
            state.y,
            state.angle + turn_angle,
            state.state)
        message = f'ANGLE {new_state.angle}'
        log += List(message)
        return (new_state, log)

    return compute_state


# установка режима работы
@curry
def set_state(new_internal_state, state):

    @State
    def compute_state(log: List) -> State:
        if new_internal_state == 'water':
            self_state = WATER
        elif new_internal_state == 'soap':
            self_state = SOAP
        elif new_internal_state == 'brush':
            self_state = BRUSH
        else:
            raise 'Такого инструмента нет.'
        new_state = RobotState(
            state.x,
            state.y,
            state.angle,
            self_state
        )
        message = f'STATE {self_state}'
        log += List(message)
        return (new_state, log)

    return compute_state


# начало чистки
@curry
def start(state):

    @State
    def compute_state(log: List) -> State:
        message = f'START WITH {state.state}'
        log += List(message)
        return (state, log)

    return compute_state


# конец чистки
@curry
def stop(state):

    @State
    def compute_state(log: List) -> State:
        message = 'STOP'
        log += List(message)
        return (state, log)

    return compute_state


if __name__ == '__main__':
    init_state = unit(State, RobotState(0.0, 0.0, 0, WATER))
    cleaner_steps: State = (init_state
                            >> move(100)
                            >> turn(-90)
                            >> turn(90)
                            >> set_state("soap")
                            >> start
                            >> move(50)
                            >> stop)

    transfer_to_cleaner(cleaner_steps(List('START_COMMANDS')))
