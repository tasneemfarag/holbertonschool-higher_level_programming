//compute the Factorial of a number

func factorial(N: Int) -> (Int) {
  var n : Int = N
  var fact : Int = 1
  while(n > 1)
  {
    fact = fact * (n)
    n = n - 1
  }
  return fact
}