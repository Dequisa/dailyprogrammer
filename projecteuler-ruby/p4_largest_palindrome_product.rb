# coding: utf-8
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

def largestPalindromeProduct()
  largestProduct = -1
  for firstNumber in 100..999 do
    for secondNumber in 100..999 do
      product = firstNumber * secondNumber
      if product > largestProduct && isPalindrome(product)
        largestProduct = product
      end
    end
  end
  return largestProduct
end

def isPalindrome(number)
  numberStr = number.to_s
  reversedNumberStr = ''
  for c in numberStr.split('') do
    reversedNumberStr = c + reversedNumberStr
  end
  return numberStr == reversedNumberStr
end

puts largestPalindromeProduct

