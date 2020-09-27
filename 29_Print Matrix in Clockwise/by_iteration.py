
from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        if not matrix or not matrix[0]:
            # Quick response for empty matrix
            return []

        left, right = 0, len(matrix[0])-1
        top, bottom = 0, len(matrix)-1

        result = []

        while True:

            result.extend( matrix[top][x] for x in range(left,right+1) )
            top += 1
            if top > bottom: break

            result.extend( matrix[y][right] for y in range(top, bottom+1) )
            right -= 1
            if left > right: break

            result.extend( matrix[bottom][x] for x in range(right, left-1, -1) )
            bottom -= 1
            if top > bottom: break

            result.extend( matrix[y][left] for y in range(bottom, top-1, -1) )
            left += 1
            if left > right: break
        
        return result



# m : the height of matrix
# n : the width of matrix

## Time Complexity: O( m * n )
#
# The overhead in time is the cost of for-loop iteration, which is of O( m * n )

## Space Complexity: O( 1 )
#
# The overhead in space is the cost of loop index and temporary variable, which is of O( 1 )



import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().spiralOrder( matrix=[[1,2,3],[4,5,6],[7,8,9]] )
        self.assertEqual(result, [1,2,3,6,9,8,7,4,5] )

    
    def test_case_2( self ):

        result = Solution().spiralOrder( matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12]] )
        self.assertEqual(result, [1,2,3,4,8,12,11,10,9,5,6,7] )


if __name__ == '__main__':

    unittest.main()