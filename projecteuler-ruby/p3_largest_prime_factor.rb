# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

require 'set'

def largestPrimeFactor(number)
  primes = primeNumbersUpTo(Math.sqrt(number).round).to_set
  biggestPrimeFactor = -1
  for potentialPrimeFactor in primes do
    puts potentialPrimeFactor
    if number % potentialPrimeFactor == 0 && potentialPrimeFactor > biggestPrimeFactor
      biggestPrimeFactor = potentialPrimeFactor
    end
  end
  return biggestPrimeFactor
end

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

puts largestPrimeFactor(600851475143)
