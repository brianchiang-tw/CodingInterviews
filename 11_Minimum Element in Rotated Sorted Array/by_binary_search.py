from typing import List

class Solution:
    def minArray(self, numbers: List[int]) -> int:

        left, right = 0, len(numbers)-1

        while left < right:

            mid = left + (right-left) // 2

            if numbers[mid] > numbers[right]:
                # minimum is on the right half
                left = mid + 1
            
            elif numbers[mid] < numbers[right]:
                # minimum is on the left half, including this element
                right = mid
            
            else:
                # minimum is the the left par, including this element
                right = right - 1
        
        return numbers[right]


import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().minArray(numbers=[3,4,5,1,2])
        self.assertEqual(result, 1)

    
    def test_case_2( self ):

        result = Solution().minArray(numbers=[2,2,2,0,1])
        self.assertEqual(result, 0)


# n : the length of input list, numbers

## Time Complexity: O( n ) on worst, O( log n) on average
#
# The overhead in time is the cost of variant binary search, which is O( n ) on worst, and O( log n ) on average.

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for loop index and temporary viariable, which is of O( 1 )


if __name__ == '__main__':

    unittest.main()
