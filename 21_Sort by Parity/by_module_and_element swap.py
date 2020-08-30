from typing import List

class Solution:
    def exchange(self, nums: List[int]) -> List[int]:

        i, j = 0, 0

        while i < len(nums):

            if nums[i] % 2 == 1:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1

            i += 1
        
        return nums


# n : the length of input list

## Time Complexity: O( n )
#
# The overhead in time is the cost of while-loop iteration, which is of O( n )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for loop index, which is of O( 1 )