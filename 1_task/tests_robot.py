import unittest

from robot import CleanerRobot, Soap, Water, Brush


class TestCleanerRobot(unittest.TestCase):

    def setUp(self):
        self.robot = CleanerRobot()

    def test_init(self):
        self.assertEqual(self.robot.position, (0, 0))
        self.assertEqual(self.robot.device.name, "water")
        self.assertEqual(self.robot.angle, 0)

    def test_move(self):
        response = self.robot.move(10)
        self.assertEqual(self.robot.position, (10, 0))
        self.assertEqual(response, "POS 10.0, 0.0")
        response = self.robot.move(60)
        self.assertEqual(self.robot.position, (70, 0))
        self.assertEqual(response, "POS 70.0, 0.0")

    def test_turn(self):
        response = self.robot.turn(90)
        self.assertEqual(self.robot.angle, 90)
        self.assertEqual(response, "ANGLE 90")
        response = self.robot.turn(90)
        self.assertEqual(self.robot.angle, 180)
        self.assertEqual(response, "ANGLE 180")

    def test_turn_and_move(self):
        self.robot.turn(90)
        self.assertEqual(self.robot.angle, 90)
        response = self.robot.move(10)
        self.assertEqual(self.robot.position, (0, -10))
        self.assertEqual(response, "POS 0.0, -10.0")
        self.robot.turn(180)
        self.assertEqual(self.robot.angle, 270)
        response = self.robot.move(10)
        self.assertEqual(self.robot.position, (0.0, 0.0))
        self.assertEqual(response, "POS 0.0, 0.0")
        self.robot.turn(90)
        self.assertEqual(self.robot.angle, 0)
        response = self.robot.move(10)
        self.assertEqual(self.robot.position, (10.0, 0.0))
        self.assertEqual(response, "POS 10.0, 0.0")
        self.robot.turn(45)
        self.assertEqual(self.robot.angle, 45)
        response = self.robot.move(10)
        self.assertEqual(self.robot.position, (17.1, -7.1))
        self.assertEqual(response, "POS 17.1, -7.1")

    def test_set(self):
        response = self.robot.set(Soap())
        self.assertEqual(self.robot.device.name, "soap")
        self.assertEqual(response, "STATE soap")
        response = self.robot.set(Brush())
        self.assertEqual(self.robot.device.name, "brush")
        self.assertEqual(response, "STATE brush")
        response = self.robot.set(Water())
        self.assertEqual(self.robot.device.name, "water")
        self.assertEqual(response, "STATE water")

    def test_start(self):
        response = self.robot.start()
        self.assertEqual(response, "START WITH water")
        self.robot.set(Soap())
        response = self.robot.start()
        self.assertEqual(response, "START WITH soap")
        self.robot.set(Brush())
        response = self.robot.start()
        self.assertEqual(response, "START WITH brush")

    def test_stop(self):
        response = self.robot.stop()
        self.assertEqual(response, "STOP")


if __name__ == '__main__':
    unittest.main()
