import { fizzBuzzCalculate, multipleFizzBuzz } from './joaolopesFizzBuzz'


describe("fizzbuzz test", () => {
  describe('validate fizzBuzzCalculate function', () => {
    it("should return 1 when pass one as parameter", () => {
      // arrange
      const inputNumber = 1;
      const expectReturn = ['1'];
  
      // act
      const functionReturn = fizzBuzzCalculate(inputNumber);
  
      // assert
      expect(expectReturn.toString()).toEqual(functionReturn[0]);
    })
    it('should return if is valid when pass parameter out of range', () => {
      // arrange, act and assert
      expect(() => fizzBuzzCalculate(0)).toThrow('Out of range')
    })
  
    it('should return "Fizz" if exist in range multiple of 3', () => {
      // arrange
  
      const inputNumer = 3;
      const expectReturn = ['1', '2', 'Fizz']
  
      // act
  
      const functionReturn = fizzBuzzCalculate(inputNumer);
  
      // assert
  
      expect(expectReturn).toStrictEqual(functionReturn)
    })
  
    it('should return "Buzz" if exist in range multiple of 5', () => {
      // arrange
  
      const inputNumer = 5;
      const expectReturn = ['1', '2', 'Fizz', '4', 'Buzz']
  
      // act
  
      const functionReturn = fizzBuzzCalculate(inputNumer);
  
      // assert
  
      expect(expectReturn).toStrictEqual(functionReturn)
    })

    it('should return "FizzBuzz" if exist in range multiple of 3 and of 5', () => {
      // arrange
  
      const inputNumer = 15;
      const expectReturn = ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8' , 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']
  
      // act
  
      const functionReturn = fizzBuzzCalculate(inputNumer);
  
      // assert
  
      expect(expectReturn).toStrictEqual(functionReturn)
    })
  })

  describe('validate multipleFizzBuzz function', () => {
    it.each`
      a       | expected
      ${3}    | ${'Fizz'}
      ${5}    | ${'Buzz'}
      ${1}    | ${'1'}
      ${15}   | ${'FizzBuzz'}
    `('returns $expected when parameter is $a', ({a, expected}) => {
      expect(multipleFizzBuzz(a)).toBe(expected);
    });
  })

})
