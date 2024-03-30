import pytest

import src.index as index

def test_suceeds_when_number_is_one():
    # arrange
    expectedResult = 1
    param = 1
    # act - ret = return
    calculator = index.FizzBuzzCalculator()
    ret = calculator.calculate(param)
    assert ret[0] == expectedResult

def test_is_buzz_when_result_is_five():
    # arrange
    expectedResult = "Buzz"
    param = 5
    #act
    calculator = index.FizzBuzzCalculator()
    ret = calculator.calculate(param)
    assert ret[4] == expectedResult

def test_is_fizz_when_result_is_six():
    # arrange
    expectedResult = "Fizz"
    param = 6
    # act
    calculator = index.FizzBuzzCalculator()
    ret = calculator.calculate(param)
    assert ret[5] == expectedResult

@pytest.mark.parametrize("param,expected", [
    (3, 'Fizz'),
    (6, 'Fizz'),
    (9, 'Fizz'),
    (33, 'Fizz')
])
def test_is_divisible_only_by_3(param, expected):
    # act
    calculator = index.FizzBuzzCalculator()
    ret = calculator.calculate(param)
    # assert
    assert ret[-1] == expected

@pytest.mark.parametrize("param,expected", [
    (5, 'Buzz'),
    (10, 'Buzz'),
    (20, 'Buzz'),
    (25, 'Buzz')
])
def test_is_divisible_only_by_5(param, expected):
    # act
    calculator = index.FizzBuzzCalculator()
    ret = calculator.calculate(param)
    # assert
    assert ret[-1] == expected

@pytest.mark.parametrize("param,expected", [
    (15, 'FizzBuzz'),
    (30, 'FizzBuzz'),
    (45, 'FizzBuzz'),
    (60, 'FizzBuzz'),
    (90, 'FizzBuzz')
])
def test_is_divisible_by_3_5(param, expected):
    # act
    calculator = index.FizzBuzzCalculator()
    ret = calculator.calculate(param)
    # assert
    assert ret[-1] == expected