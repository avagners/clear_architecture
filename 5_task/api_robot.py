from typing import List
import pure_robot as rb


class RobotAPI():

    def __init__(self) -> None:
        self.state = rb.RobotState(x=0, y=0, angle=0, state=rb.WATER)
        self.transfer_func = rb.transfer_to_cleaner

    def run_commands(self, commands: List[str]) -> None:
        for command in commands:
            cmd = command.split()
            if cmd[0] == 'move':
                self.state = rb.move(self.transfer_func, int(cmd[1]),
                                     self.state)
            elif cmd[0] == 'turn':
                self.state = rb.turn(self.transfer_func, int(cmd[1]),
                                     self.state)
            elif cmd[0] == 'set':
                self.state = rb.set_state(self.transfer_func, cmd[1],
                                          self.state)
            elif cmd[0] == 'start':
                self.state = rb.start(self.transfer_func, self.state)
            elif cmd[0] == 'stop':
                self.state = rb.stop(self.transfer_func, self.state)

    def get_x(self) -> float:
        return self.state.x

    def get_y(self) -> float:
        return self.state.y

    def get_angle(self) -> float:
        return self.state.angle

    def get_state(self):
        return self.state.state


if __name__ == "__main__":
    robot = RobotAPI()
    commands = ['move 100', 'turn -90', 'set soap', 'start', 'move 50', 'stop']
    robot.run_commands(commands)
    robot.get_x()
    robot.get_y()
    robot.get_angle()
