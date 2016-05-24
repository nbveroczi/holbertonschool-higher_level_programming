/* This is a script inside a function func factorial(N: Int) -> (Int)
Return: Factorial number */

func factorial(number: Int) -> (Int) {
    if (number <= 1) {
        return 1
    }
        
    return number * factorial(number - 1)
}
