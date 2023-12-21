import pure_robot as pr


class RobotAPI:

    def __init__(self) -> None:
        self.state = pr.RobotState(x=0, y=0, angle=0, state=pr.WATER)
        self.transfer_func = pr.transfer_to_cleaner
        self._stack = []

    def run(self, commands: str):
        commands_list = commands.split()
        for itm in commands_list:
            self.run_command(itm)

    def run_command(self, item_command) -> None:
        if item_command == 'move':
            param = self._stack.pop()
            self.state = pr.move(self.transfer_func, int(param),
                                 self.state)
        elif item_command == 'turn':
            param = self._stack.pop()
            self.state = pr.turn(self.transfer_func, int(param),
                                 self.state)
        elif item_command == 'set':
            param = self._stack.pop()
            self.state = pr.set_state(self.transfer_func, param,
                                      self.state)
        elif item_command == 'start':
            self.state = pr.start(self.transfer_func, self.state)
        elif item_command == 'stop':
            self.state = pr.stop(self.transfer_func, self.state)
        else:
            self._stack.append(item_command)

    def get_x(self) -> float:
        return self.state.x

    def get_y(self) -> float:
        return self.state.y

    def get_angle(self) -> float:
        return self.state.angle

    def get_state(self):
        return self.state.state


if __name__ == '__main__':
    commands = '100 move 100 move -90 turn soap set start 50 move stop'
    api = RobotAPI()
    api.run(commands)
    print(api.get_angle())
    print(api.get_state())
    print(api.get_y())
    print(api.get_x())
