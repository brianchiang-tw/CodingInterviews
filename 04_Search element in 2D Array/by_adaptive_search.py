class Solution(object):
    def findNumberIn2DArray(self, matrix, target):

        if matrix in ([], [ [] ]):
            # Quick rejection for empty matrix
            return False

        h, w = len(matrix), len(matrix[0])

        # start search from top-right corner
        y, x = 0, w-1

        # keep searching until out of boundary
        while y < h and x >= 0:
            
            cur_element = matrix[y][x]

            if target == cur_element:
                # target is found
                return True

            elif target < cur_element:
                # target is smaller than current element, go left
                x -= 1

            else:
                # target is larger than current element, go down
                y += 1
        
        return False


# m : the dimension of height of input matrix
# n : the dimension of width of input matrix

## Time Complexity: O( m + n )
#
# The overhead in time is the cost of adaptive search within the boundary, which is of O( m + n).

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

