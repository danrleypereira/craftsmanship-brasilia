import pytest

import main

@pytest.mark.parametrize("input,expected", [
    ("mmr", False),
    ("MM", True),
    ("mrlm", False),
    ("mm", True)
])
def test_if_input_is_Only_Movement(input, expected):
#act
    isOnlyMovement = main.Mars.checkIfInputHasOnlyMovement(input);

#assert
    assert isOnlyMovement == expected

####################################################################################################

@pytest.mark.parametrize("input,expected", [
    ("r", True),
    ("LRM", False),
    ("L", True),
    ("mm", False)
])
def test_if_input_is_Only_Direction(input, expected):
#act
    isOnlyMovement = main.Mars.checkIfInputHasOnlyDirection(input);

#assert
    assert isOnlyMovement == expected

####################################################################################################

@pytest.mark.parametrize("input,expected", [
    ("rmmm", 3),
    ("LRMm", 2),
    ("mmmLMM", 5),
    ("rm",1)
])
def test_count_movements(input, expected):
#act
    movements = main.Mars.countMovements(input);

#assert
    assert movements == expected

####################################################################################################

@pytest.mark.parametrize("caracter,expected", [
    ("r", False),
    ("L", False),
    ("M", True),
    ("m",True)
])
def test_if_caracter_is_movement(caracter,expected):
#act
    isCaracterMovement = main.Mars().checkIfCaracterIsMovement(caracter);
#assert
    assert isCaracterMovement == expected

####################################################################################################

@pytest.mark.parametrize("cardialDirection, caracter ,expected", [
    ("n", "r", "E"),
    ("S", "l", "E"),
    ("e", "l", 'N' ),
    ("W","R", "N"),
    ("N","r", "E")
])
def test_which_cardial_direcation(cardialDirection, caracter, expected):
#act
    newCardialDirection = main.Mars().whichCardialDirection(cardialDirection, caracter);
#assert
    assert newCardialDirection == expected

####################################################################################################

@pytest.mark.parametrize("input,expected", [
    ("rmmm", [0]),
    ("LRMm", [0, 0]),
    ("mmmLMM", [3]),
    ("mmlmmrMrm", [2, 2, 1])
])
def test_count_movements_before_direction_changes(input, expected):
#act
    movements = main.Mars().countMovementsBeforeDirectionChanges(input);
#assert
    assert movements == expected

####################################################################################################
# [X, Y]
@pytest.mark.parametrize("cardialDirection, initialPosition, input, expected", [
    ("N", [0, 0], "rmmm", "3:0:E"),
    ("N", [0, 1], "rrm", "0:0:S"),
    ("N", [0, 1], "rrmllmm", "0:2:N"),
    ("N", [0, 0], "MMRMMLM", "2:3:N")
])
def test_calulate_new_position(cardialDirection, initialPosition, input, expected):
#act
    newPosition = main.Mars().calculateNewPosition(cardialDirection, initialPosition, input);
#assert
    assert newPosition == expected
