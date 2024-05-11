import pytest

from main import Rover


def test_starting_position():
    # Arrange
    r = Rover()
    expected_x = 0
    expected_y = 0
    expected_direction_index = 0
    # Assert
    assert r.x == expected_x
    assert r.y == expected_y
    assert r.direction_index == expected_direction_index


def test_if_input_is_right():
    r = Rover()
    success_input = "MMMMMLLRRRMLRLRL"
    r.validate_command(success_input)

def test_if_input_is_wrong():
    r = Rover()
    success_input = "UMMM"
    r.validate_command(success_input)


def test_moving_wrap_plato_to_west():
    r = Rover()
    input_move = "LM"
    expected_x = 0
    expected_y = 9
    expected_direction_index = 3

    r.receive_command(input_move)
    assert r.x == expected_x
    assert r.y == expected_y
    assert r.direction_index == expected_direction_index

def test_moving_wrap_plato_to_east():
    r = Rover()
    input_move = "RMMMMMMMMMM"
    expected_x = 0
    expected_y = 0
    expected_direction_index = 1

    r.receive_command(input_move)
    assert r.x == expected_x
    assert r.y == expected_y
    assert r.direction_index == expected_direction_index

def test_moving_wrap_plato_to_south():
    r = Rover()
    input_move = "LLM"
    expected_x = 9
    expected_y = 0
    expected_direction_index = 2

    r.receive_command(input_move)
    assert r.x == expected_x
    assert r.y == expected_y
    assert r.direction_index == expected_direction_index

def test_moving_wrap_plato_to_north():
    r = Rover()
    input_move = "M"
    expected_x = 0
    expected_y = 0
    expected_direction_index = 0

    r.receive_command(input_move)
    assert str(r) == "1:0:N"

@pytest.mark.parametrize("param,expected_x, expected_y, expected_direction_index", [
    ('MMMLLMMMMMMRMMMMMMLLLLLLMMMMMRRM', 7, 8, 3),
    ('MMRMMLMM', 4, 2, 0),
])
def test_random_move(param, expected_x, expected_y, expected_direction_index):
    r = Rover()

    r.receive_command(param)
    assert r.x == expected_x
    assert r.y == expected_y
    assert expected_direction_index == r.direction_index


