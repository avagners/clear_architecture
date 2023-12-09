from typing import List

import pure_robot as pr


class RobotAPI():

    def __init__(self, robot_state, transfer_func, move_func, turn_func,
                 state_func, start_func, stop_func) -> None:
        self.state = robot_state
        self.transfer_func = transfer_func
        self.move = move_func
        self.turn = turn_func
        self.set_state = state_func
        self.start = start_func
        self.stop = stop_func

    def run_commands(self, commands: List[str]) -> None:
        for command in commands:
            cmd = command.split()
            if cmd[0] == 'move':
                self.state = self.move(self.transfer_func, int(cmd[1]),
                                       self.state)
            elif cmd[0] == 'turn':
                self.state = self.turn(self.transfer_func, int(cmd[1]),
                                       self.state)
            elif cmd[0] == 'set':
                self.state = self.set_state(self.transfer_func, cmd[1],
                                            self.state)
            elif cmd[0] == 'start':
                self.state = self.start(self.transfer_func, self.state)
            elif cmd[0] == 'stop':
                self.state = self.stop(self.transfer_func, self.state)

    def get_x(self) -> float:
        return self.state.x

    def get_y(self) -> float:
        return self.state.y

    def get_angle(self) -> float:
        return self.state.angle

    def get_state(self):
        return self.state.state


base_robot_api = RobotAPI(
    robot_state=pr.RobotState(0, 0, 0, pr.BRUSH),
    transfer_func=pr.transfer_to_cleaner,
    move_func=pr.move,
    turn_func=pr.turn,
    state_func=pr.set_state,
    start_func=pr.start,
    stop_func=pr.stop
)


if __name__ == "__main__":
    robot = base_robot_api
    commands = ['move 100', 'move 100', 'turn -90', 'set soap', 'start', 'move 50', 'stop']
    robot.run_commands(commands)
    robot.get_x()
    robot.get_y()
    robot.get_angle()
