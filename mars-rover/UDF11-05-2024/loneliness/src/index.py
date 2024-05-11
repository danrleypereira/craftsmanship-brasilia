# enum for directions
from enum import Enum


class directions_enum(Enum):
    NORTH = 'N'
    EAST = 'E'
    SOUTH = 'S'
    WEST = 'W'


class Rover:
    position = [0, 0]
    facing_direction = directions_enum.NORTH

    def command(self, command) -> str:
        for c in command:
            if c == 'L':
                self.turn_left()
            elif c == 'R':
                self.turn_right()
            elif c == 'M':
                self.move_forward()
            else:
                raise Exception("Invalid command")
        return f"{self.position[0]}:{self.position[1]}:{self.facing_direction.value}"

    def move_forward(self):
        # switch case for directions
        if self.facing_direction == directions_enum.NORTH:
            self.position[1] = (self.position[1] + 1) % 10 # wrap around if end of plateau, 10x10 grid
        elif self.facing_direction == directions_enum.EAST:
            self.position[0] = (self.position[0] + 1) % 10
        elif self.facing_direction == directions_enum.SOUTH:
            self.position[1] = (self.position[1] - 1) % 10
        elif self.facing_direction == directions_enum.WEST:
            self.position[0] = (self.position[0] - 1) % 10
        else:
            raise Exception("Invalid direction")

    def turn_left(self):
        # switch case for directions
        if self.facing_direction == directions_enum.NORTH:
            self.facing_direction = directions_enum.WEST
        elif self.facing_direction == directions_enum.WEST:
            self.facing_direction = directions_enum.SOUTH
        elif self.facing_direction == directions_enum.SOUTH:
            self.facing_direction = directions_enum.EAST
        elif self.facing_direction == directions_enum.EAST:
            self.facing_direction = directions_enum.NORTH
        else:
            raise Exception("Invalid direction")
        
    def turn_right(self):
        # switch case for directions
        if self.facing_direction == directions_enum.NORTH:
            self.facing_direction = directions_enum.EAST
        elif self.facing_direction == directions_enum.EAST:
            self.facing_direction = directions_enum.SOUTH
        elif self.facing_direction == directions_enum.SOUTH:
            self.facing_direction = directions_enum.WEST
        elif self.facing_direction == directions_enum.WEST:
            self.facing_direction = directions_enum.NORTH
        else:
            raise Exception("Invalid direction")