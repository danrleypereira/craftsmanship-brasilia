using FizzBuzz;

namespace FizzBuzz.Tests;
public class FizzBuzzSpecs
{
    [Fact]
    public void isNumberOne()
    {
        // Arrange
        var number = 1;
        var fizzBuzz = new FizzBuzzCalculator();

        //  Act
        String[] result = fizzBuzz.returnResult(number);

        // Assert
        Assert.Equal(number.ToString(), result[0]);
    }

    [Fact]
    public void isNumberTwoAndOne()
    {
        // Arrange
        int number = 2;
        // string[] expectedResult = new int[] { 1, 2 };
        var fizzBuzz = new FizzBuzzCalculator();

        //  Act
        String[] result = fizzBuzz.returnResult(number);

        // Assert
        Assert.Equal("1", result[0]);
        Assert.Equal("2", result[1]);
    }

    [Fact]
    public void isFizz() {
        // Arrange
        var fizzBuzz = new FizzBuzzCalculator();
        // Act
        String[] result = fizzBuzz.returnResult(10);

        // Assert
        Assert.Equal("Fizz", result[2]);
        Assert.Equal("Fizz", result[5]);
        Assert.Equal("Fizz", result[8]);
    }

    [Fact]
    public void isNumberFour()
    {
        // Arrange
        var number = 4;
        var fizzBuzz = new FizzBuzzCalculator();

        //  Act
        String[] result = fizzBuzz.returnResult(number);

        // Assert
        Assert.Equal(number.ToString(), result[3]);
    }

    [Fact]
    public void isBuzz()
    {
        // Arrange
        var fizzBuzz = new FizzBuzzCalculator();

        //  Act
        String[] result = fizzBuzz.returnResult(21);

        // Assert
        Assert.Equal("Buzz", result[4]);
        Assert.Equal("Buzz", result[9]);
        Assert.Equal("Buzz", result[19]);
    }

    [Fact]
    public void isFizzBuzz()
    {
        // Arrange
        var fizzBuzz = new FizzBuzzCalculator();

        //  Act
        String[] result = fizzBuzz.returnResult(90);

        // Assert
        Assert.Equal("FizzBuzz", result[14]);
        Assert.Equal("FizzBuzz", result[29]);
        Assert.Equal("FizzBuzz", result[44]);
    }

}