# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

require 'set'

def smallestPositiveNumberDivisibleByAllNumbersUpTo(limit)
  allPrimeFactors = {}
  for number in 2..limit do
    primeFactors = primeFactors(number)
    primeFactors.each do |factor, amount|
      if amount > allPrimeFactors[factor].to_i
        allPrimeFactors[factor] = primeFactors[factor]
      end
    end
  end
  product = 1
  allPrimeFactors.each do |factor, amount|
    product *= factor ** amount
  end
  return product
end

def primeFactors(number)
  allPrimeFactors = []
  originalNumber = number
  primes = primeNumbersUpTo(number + 1)
  while number > 1 do
    for prime in primes do
      if number % prime == 0
        number /= prime
        allPrimeFactors << prime
        break
      end
    end    
  end
  allPrimeFactorsFrequencyHash = {}
  for factor in allPrimeFactors do
    allPrimeFactorsFrequencyHash[factor] = allPrimeFactorsFrequencyHash[factor].to_i + 1
  end
  return allPrimeFactorsFrequencyHash
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


puts smallestPositiveNumberDivisibleByAllNumbersUpTo(20)

