require 'set'

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

def primeNumbersUpTo(limit)
  nonPrimeSet = Set[]
  primeArr = [2]
  currentPrime = 2

  while currentPrime < limit do
    currentMultiple = 2
    while currentMultiple * currentPrime <= limit do
      nonPrimeSet.add(currentMultiple * currentPrime)
      currentMultiple += 1
    end
    nextPrime = currentPrime + 1
    while nonPrimeSet.include?(nextPrime) do
      nextPrime += 1
    end
    if nextPrime < limit
      primeArr << nextPrime
    end
    currentPrime = nextPrime
  end
  return primeArr
end

def sumOfAllPrimesBelow(num)
  primeNumbersUpTo(num).inject(:+)
end

puts sumOfAllPrimesBelow(2000000)
