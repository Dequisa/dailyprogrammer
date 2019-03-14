
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def sumOfAllMultiples(multiples = [3,5], limit = 1000)
  sum = 0
  (0...limit).each do |element|
    sum += isMultiple(element, multiples) ? element : 0
  end
  return sum
end

def isMultiple(element, multiples)
  multiples.each do |multiple|
    if element % multiple == 0
      return true
    end
  end
  return false
end
      

puts sumOfAllMultiples
