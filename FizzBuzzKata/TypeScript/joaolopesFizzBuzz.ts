function fizzBuzzCalculate(input: number): string[] {
    if (!input || input > 100) throw new Error('Out of range')
  
    const array: string[] = []
  
    for (let index = 1; index <= input; index++) {
      array.push(multipleFizzBuzz(index)) 
    }
  
    return array
  };
  
  
  function multipleFizzBuzz(input: number): string {
    
    if(input % 3 === 0 && input % 5 === 0) {
      return 'FizzBuzz'
    }
  
    if(input % 3 === 0) {
      return 'Fizz'
    }
  
    if(input % 5 === 0) {
      return 'Buzz'
    }
  
    return input.toString()
  }
  
  export {fizzBuzzCalculate, multipleFizzBuzz}