
from typing import List

class Solution:


    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:

        # --------------------------------------------------

        def binary_search(arr, target):

            left, right = 0, len(arr)-1

            while left <= right:

                mid = left + (right - left) // 2

                if target == arr[mid]:
                    # target is found
                    return True

                elif target < arr[mid]:
                    right = mid - 1
                
                else:
                    left = mid + 1
            
            # target does not exist in arr
            return False

        # --------------------------------------------------

        if matrix in ([], [ [] ]):
            # Quick rejection for empty matrix
            return False

        h, w = len(matrix), len(matrix[0])

        min_val, max_val = matrix[0][0], matrix[-1][-1]

        if target < min_val or target > max_val:
            # Qucik rejection for target out of possible range in matrix
            return False


        for y in range(h):
            # locate possible row and launch binary search
            if matrix[y][0] <= target <= matrix[y][w-1] and binary_search(matrix[y], target):
                return True

        return False



# m : the dimension of height of input matrix
# n : the dimension of width of input matrix

## Time Complexity: O( m log n )
#
# The overhead in time is the cost of binary search for each row, which is of O( m log n)

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for loop index and temporary variable, which are of O( 1 ).


import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().findNumberIn2DArray( matrix=[ 
        [1,   4,  7, 11, 15],
        [2,   5,  8, 12, 19],
        [3,   6,  9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30] ], target=5 )

        self.assertEqual(result, True)
    

    def test_case_2( self ):

        result = Solution().findNumberIn2DArray( matrix=[ 
        [1,   4,  7, 11, 15],
        [2,   5,  8, 12, 19],
        [3,   6,  9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30] ], target=20 )
        
        self.assertEqual(result, False)





if __name__ == '__main__':

    unittest.main()