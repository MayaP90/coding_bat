# Problem
# Given an array of ints, return the number of 9's in the array.

array_count9([1, 2, 9]) → 1
array_count9([1, 9, 9]) → 2
array_count9([1, 9, 9, 3, 9]) → 3

# For this problem what I have to do is within a given array I have to return thenumber of 9's
# in the list

#To do this
def array_count9(nums):
  count=0
  # start with zero and the item in the array
  for num in mums:
    # The assignment of one of the numeber's in the list equalls 9
    # then add the following increment from count which equals zero.
    if nums == 9:
      count +=1
    # simply return count
  return count;
  
