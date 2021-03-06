# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

def sumOfFibTerms(limit = 4000000)
  memoizedFibNumbers = {}
  currentTerm = 0
  sum = 0
  while true    
    currentFibNum = fibNumber(currentTerm, memoizedFibNumbers)
    memoizedFibNumbers[currentTerm] = currentFibNum
    if currentFibNum > limit
      break
    else
      sum += currentFibNum % 2 == 0 ? currentFibNum : 0
    end
    currentTerm += 1
  end
  return sum
end

def fibNumber(n, memoizedNums)
  case n
  when 0,1
    return 1
  else
    if memoizedNums[n]
      return memoizedNums[n]
    else
      return fibNumber(n - 1, memoizedNums) + fibNumber(n - 2, memoizedNums)
    end
  end
end

puts sumOfFibTerms

