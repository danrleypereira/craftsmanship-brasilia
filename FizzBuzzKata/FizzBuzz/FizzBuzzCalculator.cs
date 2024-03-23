using System;
using System.Numerics;

namespace FizzBuzz
{
    public class FizzBuzzCalculator
    {
        public string[] returnResult(int width)
        {
            var strings = new string[100];
            int remainingNumbers = width;
            while(remainingNumbers > 0)
                strings[remainingNumbers-1] = check(remainingNumbers--);
            return strings;
        }

        private string check(int number) {
            if ((number % 5 == 0) && (number % 3 == 0))
                return "FizzBuzz";
            else if (number % 5 == 0)
                return "Buzz";
            else if (number % 3 == 0)
                return "Fizz";
            else
                return number.ToString();
        }
    }
}
