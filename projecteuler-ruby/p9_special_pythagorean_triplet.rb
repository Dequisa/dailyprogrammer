# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def pythagoreanTriplet(targetSum)
  for a in 1..((targetSum - 3) / 3) do
    for b in (a + 1)..(targetSum - 1 - a) / 2 do
      c = targetSum - a - b
      if c ** 2 == (a ** 2) + (b ** 2)
        return a * b * c
      end
    end
  end
end

puts pythagoreanTriplet(1000)
