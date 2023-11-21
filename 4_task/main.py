from devices import Water, Brush, Soap
from robot import CleanerRobot

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
