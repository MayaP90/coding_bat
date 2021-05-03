# Problem:
# Given 2 int values, return True if one is negative and one is positive.
# Except if the parameter "negative" is True, then return True only if both are negative.

# This exapmple is the direction instruction from the coding bat website
def pos_neg(a, b, negative):
 # If the value is negative which is both are less than 0
  if negative:
    return (a < 0 and b < 0)
  # Then return True. However if both a and b are different in terms of which one is negative and one is positive then return false
  else:
    return ((a < 0 and b > 0) or (a > 0 and b < 0))

