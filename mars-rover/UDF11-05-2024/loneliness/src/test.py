import pytest
from src.index import Rover, directions_enum

@pytest.fixture
def rover():
    return Rover()

class TestRover:
    # Fixture to reset rover state before each test method in this class
    @pytest.fixture(autouse=True)
    def reset_rover(self, rover):
        rover.position = [0, 0]
        rover.facing_direction = directions_enum.NORTH
        return rover
    
    @pytest.mark.parametrize("command, expected_output", [
        ("L", "0:0:W"),
        ("R", "0:0:E"),
        ("M", "0:1:N"),
        ("MM", "0:2:N"),
        ("RMRRMMMMLMMMMMM", "7:4:S"),
        ("RMM", "2:0:E"),
        ("RRM", "0:9:S"),
        ("RRRRM", "0:1:N"),
        ("MMLMLLMM", "1:2:E"),
    ])
    def test_command_output(self, rover, command, expected_output, capsys):
        output = rover.command(command)
        assert output == expected_output

    @pytest.mark.parametrize("command, expected_position, expected_direction", [
        ("MMM", [0, 3], directions_enum.NORTH),
        ("L", [0, 0], directions_enum.WEST),
        ("R", [0, 0], directions_enum.EAST),
        ("RMM", [2, 0], directions_enum.EAST),
        ("RRM", [0, 9], directions_enum.SOUTH),
        ("RRRRM", [0, 1], directions_enum.NORTH),
        ("RMRRMMMMLMMMMMM", [7, 4], directions_enum.SOUTH),
        ("MMLMLLMM", [1, 2], directions_enum.EAST),
    ])
    def test_command(self, rover, command, expected_position, expected_direction):
        rover.command(command)
        assert rover.position == expected_position
        assert rover.facing_direction == expected_direction

    # Parametrized test for turning left
    @pytest.mark.parametrize("start_direction, expected_directions", [
        # test every direction for each starting direction
        (directions_enum.NORTH, [directions_enum.WEST, directions_enum.SOUTH, directions_enum.EAST, directions_enum.NORTH]),
        (directions_enum.WEST, [directions_enum.SOUTH, directions_enum.EAST, directions_enum.NORTH, directions_enum.WEST]),
        (directions_enum.SOUTH, [directions_enum.EAST, directions_enum.NORTH, directions_enum.WEST, directions_enum.SOUTH]),
        (directions_enum.EAST, [directions_enum.NORTH, directions_enum.WEST, directions_enum.SOUTH, directions_enum.EAST])
    ])
    def test_turn_left(self, rover, start_direction, expected_directions):
        rover.facing_direction = start_direction
        for expected_direction in expected_directions:
            rover.turn_left()
            assert rover.facing_direction == expected_direction

    # Parametrized test for turning right
    @pytest.mark.parametrize("start_direction, expected_directions", [
        # test every direction for each starting direction
        (directions_enum.NORTH, [directions_enum.EAST, directions_enum.SOUTH, directions_enum.WEST, directions_enum.NORTH]),
        (directions_enum.EAST, [directions_enum.SOUTH, directions_enum.WEST, directions_enum.NORTH, directions_enum.EAST]),
        (directions_enum.SOUTH, [directions_enum.WEST, directions_enum.NORTH, directions_enum.EAST, directions_enum.SOUTH]),
        (directions_enum.WEST, [directions_enum.NORTH, directions_enum.EAST, directions_enum.SOUTH, directions_enum.WEST])
    ])
    def test_turn_right(self, rover, start_direction, expected_directions):
        rover.facing_direction = start_direction
        for expected_direction in expected_directions:
            rover.turn_right()
            assert rover.facing_direction == expected_direction

    @pytest.mark.parametrize("direction, expected_position", [
        (directions_enum.NORTH, [0, 1]),
        (directions_enum.EAST, [1, 0]),
        (directions_enum.SOUTH, [0, 9]),
        (directions_enum.WEST, [9, 0])
    ])
    def test_move_forward(self, rover, direction, expected_position):
        rover.facing_direction = direction
        rover.move_forward()
        assert rover.position == expected_position

    def test_invalid_direction(self, rover):
        rover.facing_direction = "INVALID"
        with pytest.raises(Exception):
            rover.move_forward()
            rover.turn_left()
            rover.turn_right()

    def test_end_of_plateau_wraps_around(self, rover):
        rover.position = [9, 9]
        rover.facing_direction = directions_enum.EAST
        rover.move_forward()
        assert rover.position == [0, 9]
        rover.position = [9, 9]
        rover.facing_direction = directions_enum.NORTH
        rover.move_forward()
        assert rover.position == [9, 0]
        rover.position = [0, 0]
        rover.facing_direction = directions_enum.WEST
        rover.move_forward()
        assert rover.position == [9, 0]
        rover.position = [0, 0]
        rover.facing_direction = directions_enum.SOUTH
        rover.move_forward()
        assert rover.position == [0, 9]

    def test_invalid_command(self, rover):
        with pytest.raises(Exception):
            rover.command("INVALID")
    
