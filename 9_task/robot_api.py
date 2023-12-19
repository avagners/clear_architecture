from typing import List

import pure_robot as pr


class RobotAPI():

    def __init__(self, robot_state, transfer_func, command_func) -> None:
        self.state = robot_state
        self.transfer_func = transfer_func
        self.command_func = command_func

    def run_commands(self, commands: List[str]) -> None:
        for command in commands:
            cmd = command.split()
            command = self.command_func(cmd)
            if cmd[0] == 'move':
                self.state = command(self.transfer_func, int(cmd[1]),
                                     self.state)
            elif cmd[0] == 'turn':
                self.state = command(self.transfer_func, int(cmd[1]),
                                     self.state)
            elif cmd[0] == 'set':
                self.state = command(self.transfer_func, cmd[1],
                                     self.state)
            elif cmd[0] == 'start':
                self.state = command(self.transfer_func, self.state)
            elif cmd[0] == 'stop':
                self.state = command(self.transfer_func, self.state)

    def get_x(self) -> float:
        return self.state.x

    def get_y(self) -> float:
        return self.state.y

    def get_angle(self) -> float:
        return self.state.angle

    def get_state(self):
        return self.state.state


def robot_command(cmd):
    if cmd[0] == 'move':
        return pr.move
    elif cmd[0] == 'turn':
        return pr.turn
    elif cmd[0] == 'set':
        return pr.set_state
    elif cmd[0] == 'start':
        return pr.start
    elif cmd[0] == 'stop':
        return pr.stop
    return None


base_robot_api = RobotAPI(
    robot_state=pr.RobotState(0, 0, 0, pr.WATER),
    transfer_func=pr.transfer_to_cleaner,
    command_func=robot_command
)


if __name__ == "__main__":
    robot = base_robot_api
    commands = ['move 100', 'move 100', 'turn -90', 'set soap', 'start', 'move 50', 'stop']
    robot.run_commands(commands)
    robot.get_x()
    robot.get_y()
    robot.get_angle()
