import re

class Rover:

    array_directions = ["N", "E", "S", "W"]


    def __init__(self):
        self.x = 0
        self.y = 0
        self.direction_index = 0


    def __str__(self):
        return f"{self.x}.{self.y}:{Rover.array_directions[self.direction_index]}"


    def validate_command(self, command):
        return bool(re.match(r'^[MLR]*$', command))


    def receive_command(self, command) :
        if self.validate_command(command):
            for i in command:
                if i == "M":
                    if self.direction_index == 0:
                        self.x = (self.x + 1) % 10
                    if self.direction_index == 1:
                        self.y = (self.y + 1) % 10
                    if self.direction_index == 2:
                        self.x = (self.x - 1) % 10
                    if self.direction_index == 3:
                        self.y = (self.y - 1) % 10
                if i == "L":
                    self.direction_index = (self.direction_index - 1) % 4
                if i == 'R':
                    self.direction_index = (self.direction_index + 1) % 4

        return (str(self))
