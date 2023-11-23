from typing import List
import pure_robot as rb


class RobotAPI():

    def __init__(self) -> None:
        self.state = rb.RobotState(x=0, y=0, angle=0, state=rb.WATER)
        self.transfer_func = rb.transfer_to_cleaner

    def run_commands(self, commands: List[str]) -> None:
        rb.make(self.transfer_func, commands, self.state)


if __name__ == "__main__":
    robot = RobotAPI()
    robot.run_commands(['move 100', 'move 100', 'turn -90', 'set soap', 'start', 'move 50', 'stop'])
