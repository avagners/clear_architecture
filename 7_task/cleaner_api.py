from robot import CleanerRobot


class CleanerApi:

    def __init__(self):
        self.cleaner = CleanerRobot(self.transfer_to_cleaner)  # внедрение зависимости

    def transfer_to_cleaner(self, message):
        print(message)

    def get_x(self):
        return self.cleaner.x

    def get_y(self):
        return self.cleaner.y

    def get_angle(self):
        return self.cleaner.angle

    def get_state(self):
        return self.cleaner.state

    def activate_cleaner(self, code):
        self.cleaner.make(code)
