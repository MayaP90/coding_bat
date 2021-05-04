# Problem
# Given an array of ints, return the number of 9's in the array.

array_count9([1, 2, 9]) → 1
array_count9([1, 9, 9]) → 2
array_count9([1, 9, 9, 3, 9]) → 3

# For this problem what I have to do is within a given array I have to return thenumber of 9's
# in the list

#To do this
def array_count9(nums):
  an = 0
  for i in range(0, len(nums), 1):
  
    if nums[i] == 9:
      an = an + 1
    
  return an;
  
